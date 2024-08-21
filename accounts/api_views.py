from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from scholar_register.models import StudentProfile
from django.contrib.auth.decorators import login_required
from scholar_register.models import *
from fees_module.models import PaymentSchedule, StudentFeePayment


@api_view(['POST'])
def student_login_view(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        # Fetch the student profile after authentication
        try:
            parent = StudentParents.objects.get(user=user)
            print("parent data :",parent)
            students = StudentProfile.objects.filter(parent=parent).first()
            print("Students data",students)
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


# @login_required
@api_view(['GET'])
def student_dashboard_view(request):
    # fees_date = 
    student_data ={
        'message':'student data fetched successfully',
        'code':200,
        'error':False,
        'data' : {"fees_data": {'annual':40000, 'deposit':10000, 'total due': 30000},
                'attendance_data' : {'total':30, 'present':22, 'absent':3, 'leaves':5},
                'custom_menu' : "custom menu data"}
                },
        
        
    return Response(student_data, status=status.HTTP_200_OK)

