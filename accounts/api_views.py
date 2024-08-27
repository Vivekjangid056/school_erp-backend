from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

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
        all_childrens = StudentProfile.objects.filter(parent = parent)
        all_childrens_serializer = AllStudentSerializer(all_childrens, many=True)

        refresh = RefreshToken.for_user(user)
        return Response({
            'error': False,
            'code': 200,
            'data': {
                'access_token': str(refresh.access_token),
                'student': student_serializer.data,
                'all_childs': all_childrens_serializer.data
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
    subject_id = data.get('subject_id')
    
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
        subject_id=subject_id, student_id=student_id, session_id=session_id, branch_id=branch_id
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

    custom_menu_data = CustomMenuSerializer(custom_menu).data if custom_menu else None
    
    # Prepare the response data
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
                'holidays': 5  # Replace with actual holiday count if available
            },
            'custom_menu': custom_menu_data
        }
    }
    
    return Response(student_data, status=status.HTTP_200_OK)

