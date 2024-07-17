from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import StudentLoginSerializer, StudentSerializer
from scholar_register.models import StudentProfile
from django.contrib.auth.decorators import login_required


@api_view(['POST'])
def student_login_view(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']

        # Fetch the student profile after authentication
        try:
            student = StudentProfile.objects.get(user=user)
        except StudentProfile.DoesNotExist:
            return Response({
                'status': False,
                'code': 404,
                'message': 'Student profile not found'
            }, status=status.HTTP_404_NOT_FOUND)

        student_serializer = StudentSerializer(student)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'status': True,
            'code': 200,
            'data': student_serializer.data,
            'message': 'Student login successfully'
        }, status=status.HTTP_200_OK)
    
    return Response({
        'status': False,
        'code': 400,
        'errors': serializer.errors,
        'message': 'Invalid credentials'
    }, status=status.HTTP_400_BAD_REQUEST)


# @login_required
@api_view(['GET'])
def student_dashboard_view(request):
    student_data ={
        'message':'student data fetched successfully',
        'code':200,
        'status':True,
        'data' : {"fees_data": {'annual':40000, 'deposit':10000, 'total due': 30000},
                'attendance_data' : {'total':30, 'present':22, 'absent':3, 'leaves':5},
                'custom_menu' : "custom menu data"}
                },
        
        
    return Response(student_data, status=status.HTTP_200_OK)