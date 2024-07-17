from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentSerializer
from .models import StudentProfile, User
from django.core.exceptions import ValidationError

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        try:
            students = StudentProfile.objects.all()
            serializer = StudentSerializer(students, many=True)
            data = {
                'status': True,
                'code': 200,
                'data': serializer.data,
                'message': "Students fetched successfully"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                'status': False,
                'code': 500,
                'message': f"An error occurred: {str(e)}"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'status': True,
                    'code': 201,
                    'data': serializer.data,
                    'message': "Student created successfully"
                }
                return Response(data, status=status.HTTP_201_CREATED)
            data = {
                'status': False,
                'code': 400,
                'errors': serializer.errors,
                'message': "Failed to create student"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {
                'status': False,
                'code': 500,
                'message': f"An error occurred: {str(e)}"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = StudentProfile.objects.get(pk=pk)
    except StudentProfile.DoesNotExist:
        data = {
            'status': False,
            'code': 404,
            'message': "Student not found"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            serializer = StudentSerializer(student)
            data = {
                'status': True,
                'code': 200,
                'data': serializer.data,
                'message': "Student details fetched successfully"
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            data = {
                'status': False,
                'code': 500,
                'message': f"An error occurred: {str(e)}"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'PUT':
        try:
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'status': True,
                    'code': 200,
                    'data': serializer.data,
                    'message': "Student details updated successfully"
                }
                return Response(data, status=status.HTTP_200_OK)
            data = {
                'status': False,
                'code': 400,
                'errors': serializer.errors,
                'message': "Failed to update student details"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            data = {
                'status': False,
                'code': 400,
                'message': f"Validation error: {str(e)}"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {
                'status': False,
                'code': 500,
                'message': f"An error occurred: {str(e)}"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        try:
            user = student.user
            student.delete()
            user.delete()  # Also delete the associated user
            data = {
                'status': True,
                'code': 204,
                'message': "Student deleted successfully"
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            data = {
                'status': False,
                'code': 500,
                'message': f"An error occurred: {str(e)}"
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def student_activity(request):
    pass