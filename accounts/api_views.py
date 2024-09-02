from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from teacher_management.models import Employee, EmployeeMaster
from institute.models import CustomMenu
from .serializers import *
from scholar_register.models import StudentProfile
from django.contrib.auth.decorators import login_required
from scholar_register.models import *
from fees_module.models import PaymentSchedule, StudentFeePayment
from datetime import datetime
from calendar import monthrange


@api_view(['POST'])
def student_login_view(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        # Fetch the student profile after authentication
        try:
            parent = StudentParents.objects.get(user=user)
            students = StudentProfile.objects.filter(parent=parent).first()
        except StudentProfile.DoesNotExist:
            return Response({
                'error': True,
                'code': 200,
                'message': 'Student profiles not found'
            })
        student_serializer = StudentSerializer(students, context={'request': request})
        

        refresh = RefreshToken.for_user(user)
        return Response({
            'error': False,
            'code': 200,
            'data': {
                'access_token': str(refresh.access_token),
                'student': student_serializer.data,
            },
            'message': 'Student login successful'
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'error': True,
            'code': 200,
            'message': 'Invalid data',
            'errors': serializer.errors,
            'data':{}
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def student_dashboard_view(request):
    data = request.data
    student_id = data.get('student_id')
    session_id = data.get('session_id')
    branch_id = data.get('branch_id')
    standard_id = data.get('standard_id')
    
    # Check for required parameters
    if not (branch_id and session_id):
        return Response({
            'error': True,
            'code': 200,
            'message': 'Missing session_id or branch_id. Please select both to get the data.',
            'data': {}
        })

    # Get the student's fee payment information
    student_fee_payment = StudentFeePayment.objects.filter(
        student_id=student_id, branch=branch_id, session_id=session_id
    ).select_related('fee_structure').first()
    
    if not student_fee_payment:
        return Response({
            'error': True,
            'code': 200,
            'message': 'No fee payment information found for this student.',
            'data': {}
        })

    # Calculate the amount paid and due amount
    payment_schedule = PaymentSchedule.objects.filter(
        student_fee_payment=student_fee_payment
    ).aggregate(amount_paid=models.Sum('amount_paid')) or {'amount_paid': 0}
    
    amount_paid = payment_schedule['amount_paid'] or 0
    due_amount = student_fee_payment.paying_amount - amount_paid
    
    # Get attendance information
    attendances = Attendance.objects.filter(
        standard_id = standard_id, student_id=student_id, session_id=session_id, branch_id=branch_id
    )
    
    present = attendances.filter(present=True).count()
    absent = attendances.filter(absent=True).count()
    
    # Get the student's profile and custom menu data
    try:
        student = StudentProfile.objects.select_related('parent__institute').get(id=student_id)
        custom_menu = CustomMenu.objects.filter(institute=student.parent.institute).first()
    except StudentProfile.DoesNotExist:
        return Response({
            'error': True,
            'code': 404,
            'message': 'Student profile not found.',
            'data': {}
        })

    custom_menu_data = CustomMenuSerializer(custom_menu, context={'request':request}).data if custom_menu else None
    
    # Prepare the response data
    # all childs data
    student = StudentProfile.objects.get(id= student_id)
    parent = StudentParents.objects.get(id = student.parent.id)

    all_childs = StudentProfile.objects.filter(parent = parent)
    all_childrens_serializer = AllStudentSerializer(all_childs, many=True, context={'request':request})
    student_data = {
        'message': 'Student data fetched successfully',
        'code': 200,
        'error': False,
        'data': {
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
            'custom_menu': custom_menu_data,
            'all_childs': all_childrens_serializer.data
        }
    }
    
    return Response(student_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def teacher_login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, username=email, password=password)

    if user is not None:
        try:
            employee = Employee.objects.get(user=user)
            data = EmployeeMaster.objects.get(employee_profile=employee.id)
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Get the image URL if user_image is an ImageField
            image_url = employee.user_image.url if employee.user_image else None
            
            response_data = {
                'id': employee.id,
                'token': access_token,
                'first_name': data.first_name,
                'middle_name': employee.middle_name,
                'last_name': data.last_name,
                'image': image_url,
                'email': employee.email,
                'mobile': user.phone_number,
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
        
@api_view(['POST'])
def teacher_logout_view(request):
    return Response({
        'code' : 200,
        'error' : False,
        'message' : 'Logged Out Successfully'
    })

@api_view(['POST'])
def teacher_dashboard(request):
    data = request.data