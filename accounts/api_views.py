from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from teacher_management.models import Employee, EmployeeAttendance
from institute.models import CustomMenu
from .serializers import *
from scholar_register.models import StudentProfile
from rest_framework.permissions import IsAuthenticated
from scholar_register.models import *
from fees_module.models import PaymentSchedule, StudentFeePayment
from datetime import datetime
from calendar import monthrange
from django.db.models import Sum
from rest_framework.exceptions import PermissionDenied

#======================================== Student Login ==========================================
@api_view(['POST'])
def student_login_view(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        try:
            parent = StudentParents.objects.get(user=user)
            institute = Institute.objects.filter(student_parent_institute_id = parent)
            student = StudentProfile.objects.filter(parent=parent).first()
            print(student.id)
        except StudentProfile.DoesNotExist:
            return Response({
                'error': True,
                'code': 404,
                'message': 'Student profiles not found',
                'data': {}
            }, status=status.HTTP_404_NOT_FOUND)

        
        refresh = RefreshToken.for_user(user)
        return Response({
            'error': False,
            'code': 200,
            'message': 'Student login successful',
            'data': {
                'access_token': str(refresh.access_token),
                'user':{'id':user.id,
                         'email':user.email},
                'student': {'student_id':student.id,
                            'instutute_id':parent.institute.registration_number,
                            'branch_id':student.branch.id,
                            'session_id':student.session.id,
            }
                }
        }, status=status.HTTP_200_OK)
    else:
        # Extract the first validation error message and format it
        error_message = next(iter(serializer.errors.values()))[0]
        return Response({
            'error': True,
            'code': 400,
            'message': error_message,
            'data': {}
        }, status=status.HTTP_400_BAD_REQUEST)


#======================================== Student Dashboard ==========================================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_dashboard_view(request):
    data = request.data
    student_id = data.get('student_id')
    session_id = data.get('session_id')
    branch_id = data.get('branch_id')

    if not all([branch_id, session_id, student_id]):
        return Response({
            'error': True,
            'code': 400,
            'message': 'Missing session_id, branch_id, or student_id. Please provide all required parameters.',
            'data': {}
        }, status=status.HTTP_400_BAD_REQUEST)

    student = StudentProfile.objects.filter(id=student_id, branch_id=branch_id, session_id=session_id).first()
    if not student or request.user != student.parent.user:
        return Response({
            'error': True,
            'code': 400,
            'message': 'Student not found or does not belong to the logged-in parent.',
            'data': {}
        }, status=status.HTTP_400_BAD_REQUEST)

    student_fee_payment = StudentFeePayment.objects.filter(
        student_id=student_id, branch_id=branch_id, session_id=session_id
    ).select_related('fee_structure').first()

    if not student_fee_payment:
        return Response({
            'error': True,
            'code': 404,
            'message': 'No fee payment information found for this student.',
            'data': {}
        }, status=status.HTTP_404_NOT_FOUND)

    amount_paid = PaymentSchedule.objects.filter(student_fee_payment=student_fee_payment).aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
    due_amount = student_fee_payment.paying_amount - amount_paid

    attendances = Attendance.objects.filter(student_id=student_id, session_id=session_id, branch_id=branch_id)
    present = attendances.filter(present=True).count()
    absent = attendances.filter(absent=True).count()

    # Serialize the custom menus first
    custom_menus = CustomMenu.objects.filter(url_for='student', is_active=True)
    custom_menu_data = CustomMenuSerializer(custom_menus, many=True, context={'request': request}).data

    # Loop through the serialized data and replace the placeholders in the URLs
    for menu in custom_menu_data:
        menu['url'] = menu['url'].replace('institute_id', str(student.parent.institute.registration_number)).replace(
            'branch_id', str(branch_id)).replace(
            'session_id', str(session_id)).replace(
            'student_id', str(student_id)
        )
    
    all_childs = StudentProfile.objects.filter(parent=student.parent)
    sessions = AcademicSession.objects.filter(student_profile_session=student)

    student_data = {
        'message': 'Student data fetched successfully',
        'code': 200,
        'error': False,
        'data': {
            'student': StudentSerializer(student, context={'request': request}).data,
            'fees_data': {
                'total_anual_fee': student_fee_payment.fee_structure.total_fee,
                'paying_amount': student_fee_payment.paying_amount,
                'fees_deposited': amount_paid,
                'due_amount': due_amount
            },
            'attendance_data': {
                'total_working_days': attendances.count(),
                'present': present,
                'absent': absent,
            },
            'all_childs': AllStudentSerializer(all_childs, many=True, context={'request': request}).data,
            'custom_menu': custom_menu_data,  # Use the updated serialized menu data here
            'sessions': AcademicSessionSerializer(sessions, many=True).data,
        }
    }

    return Response(student_data)


#======================================== Teacher Login ==========================================
@api_view(['POST'])
def teacher_login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)

    if user is not None:
        try:
            employee = Employee.objects.get(user=user)
            print(employee)
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Get the image URL if user_image is an ImageField
            image_url = employee.employee_image.url if employee.employee_image else None

            sessions = AcademicSession.objects.filter(employee_session = employee)
            session_serializer = AcademicSessionSerializer(sessions, many=True)

            branches = InstituteBranch.objects.filter(employee_branch = employee.branch.id)
            branch_serializer = InstituteBranchSerializer(branches, many=True)

            institute_data = {
                'id':employee.institute.registration_number,
                'name' : employee.institute.institute_name
            }

            user_data={
                'id':employee.user.id,
                'email':employee.user.email
            }


            response_data = {
                'token': access_token,
                'user': user_data,
                'id': employee.id,
                'first_name': employee.first_name,
                'last_name': employee.last_name,
                'image': image_url,
                'email': employee.personal_email,
                'mobile': user.phone_number,
                'institute':institute_data,
                'sessions':session_serializer.data,
                'branches':branch_serializer.data
            }

            return Response({
                'code': 200,
                'error': False,
                'message': 'Successfully logged in',
                'data': response_data
            })
        except Employee.DoesNotExist:
            return Response({
                'code': 200,
                'error': True,
                'message': 'Employee profile not found'
            })
    else:
        return Response({
            'code': 200,
            'error': True,
            'message': 'Invalid credentials'
        })

#======================================== Teacher Logout ==========================================
@api_view(['POST'])
def teacher_logout_view(request):
    return Response({
        'code' : 200,
        'error' : False,
        'message' : 'Logged Out Successfully'
    })

#======================================== Teacher Dashboard ==========================================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def teacher_dashboard(request):
    data = request.data
    session_id = data.get('session_id')
    teacher_id = data.get('teacher_id')
    branch_id = data.get('branch_id')

    teacher = Employee.objects.get(pk = teacher_id)
    teacher_data = Employee.objects.get(employee_profile_details=teacher)

    attendances = EmployeeAttendance.objects.filter(employee = teacher_data.id, session = session_id, branch= branch_id)

    present = attendances.filter(present=True).count()
    absent = attendances.filter(absent=True).count()

    attendance_data = {
                'total_working_days': attendances.count(),
                'present': present,
                'absent': absent,
            }
    return Response(attendance_data)


# ======================================== Teacher Profile ==========================================
@api_view(['POST'])
def teacher_profile(request):
    data = request.data
    session_id = data.get('session_id')
    teacher_id = data.get('teacher_id')

    teacher = Employee.objects.get(pk = teacher_id)
    session = AcademicSession.objects.get(pk = session_id)
    teacher_data = Employee.objects.get(employee_profile_details=teacher)
    session_data = AcademicSession.objects.filter(employee_session = teacher_data)

    session_serializer = AcademicSessionSerializer(session_data, many=True)

    teacher_data_serializer = EmployeeMasterSerializer(teacher_data)

    return