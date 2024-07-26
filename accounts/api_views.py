from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from scholar_register.models import StudentProfile
from django.contrib.auth.decorators import login_required
from scholar_register.models import *


@api_view(['POST'])
def student_login_view(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        # Fetch the student profile after authentication
        try:
            parent = StudentParents.objects.get(user=user)
            students = StudentProfile.objects.filter(parent=parent)
        except StudentProfile.DoesNotExist:
            return Response({
                'status': False,
                'code': 404,
                'message': 'Student profiles not found'
            }, status=status.HTTP_404_NOT_FOUND)

        parent_serializer = ParentSerializer(parent)
        student_serializer = StudentSerializer(students, many=True)

        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'status': True,
            'code': 200,
            'data': {
                'students': student_serializer.data,
                'parent': parent_serializer.data
            },
            'message': 'Student login successful'
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'status': False,
            'code': 400,
            'message': 'Invalid data',
            'errors': serializer.errors
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

