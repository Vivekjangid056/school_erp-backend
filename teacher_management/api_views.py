from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Employee
from .serializers import EmployeeSerializer



@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, username=email, password=password)

    if user is not None:
        try:
            employee = Employee.objects.get(user=user)
            serializer = EmployeeSerializer(employee)
            
            refresh = RefreshToken.for_user(user)
            return Response({
                'code':200,
                'error': False,
                'message': 'Login successful',
                'access token': str(refresh.access_token),
                'data': serializer.data,
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
def logout_view(request):
    return Response({
        'code' : 200,
        'error' : False,
        'message' : 'Logged Out Successfully'
    })