from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
from datetime import datetime
from calendar import monthrange
from .models import StudentFeePayment, PaymentSchedule
from.serializers import *
from scholar_register.models import StudentParents, StudentProfile

@api_view(['POST'])
def get_student_fees_details(request):
    data=request.data
    # institute_id=data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')

    if not all([branch_id, session_id, student_id]):
        return Response({
            'error':True,
            'code':500,
            'message':'branch id , session id and student are required',
            'data':{}
        })
    
    user = request.user
    parent = StudentParents.objects.get(user=user)
    students = StudentProfile.objects.filter(parent=parent)

    # Check if the given student_id belongs to this parent
    if not students.filter(id=student_id).exists():
        return Response({
            'error': True,
            'code': 200,
            'message': "You do not have permission to access this student's data.",
            'data': {}
        })

    fees_details1 = StudentFeePayment.objects.filter(branch_id= branch_id, 
                                                    session_id=session_id, student_id=student_id).first()
    
    if not fees_details1:
        return Response({
        'error':True,
            'code':200,
            'message':'fees data not found for the current student',
            'data':{}
    })

    fees_details2= PaymentSchedule.objects.filter(student_fee_payment=fees_details1)

    if not fees_details2:
        return Response({
        'error':True,
            'code':200,
            'message':'fees data not found for the current student',
            'data':{}
    })

    fees_serializer=PaymentScheduleSerializer(fees_details2, many=True)
    formatted_fees_data = []
    for fee in fees_serializer.data:
        payment_due_date_str = fee['payment_due_date']
        payment_date_str = fee['payment_date']
    
    # Parse the due_date and reformat it
        if payment_due_date_str and payment_date_str:
            fee['payment_due_date'] = datetime.strptime(payment_due_date_str, "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d")
            fee['payment_date'] = datetime.strptime(payment_date_str, "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d")
            formatted_fees_data.append(fee)

    return Response({
        'error':False,
            'code':200,
            'message':'fees data fetched successfully',
            'data':{'total_amount':fees_details1.paying_amount,
                    'installment_frequency':fees_details1.installment_frequency,
                    'fees_data':fees_serializer.data}
    })


    