from rest_framework.response import Response
from .models import NotificationModel
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def notification_list(request):
    if request.method == 'GET':
        notifications = NotificationModel.objects.all()
        if notifications:
            serializer = NotificationSerializer(notifications, many=True)
            data = {
                'status': True,
                'code': 200,
                'data': serializer.data,
                'message': "Notifications fetched successfully"
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                'status': False,
                'code': 404,
                'message': "Notifications not found"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': True,
                'code': 201,
                'data': serializer.data,
                'message': "Notification created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = {
            'status': False,
            'code': 400,
            'errors': serializer.errors,
            'message': "Failed to create notification"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def notification_detail(request, pk):
    try:
        notification = NotificationModel.objects.get(pk=pk)
    except NotificationModel.DoesNotExist:
        data = {
            'status': False,
            'code': 404,
            'message': "Notification with given id is not found"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        data = {
            'status': True,
            'code': 200,
            'data': serializer.data,
            'message': "Notification fetched successfully"
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': True,
                'code': 200,
                'data': serializer.data,
                'message': "Notification updated successfully"
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'status': False,
            'code': 400,
            'errors': serializer.errors,
            'message': "Failed to update notification"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        notification.delete()
        data = {
            'status': True,
            'code': 200,
            'message': "Notification deleted successfully"
        }
        return Response(data, status=status.HTTP_200_OK)