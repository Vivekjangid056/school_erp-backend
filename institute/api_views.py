from rest_framework.response import Response
from .models import GalleryItems, NotificationModel
from .serializers import GallerySerializer, NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def notification_list(request):
    if request.method == 'GET':
        notifications = NotificationModel.objects.all()
        if notifications:
            serializer = NotificationSerializer(notifications, many=True)
            data = {
                'error': False,
                'code': 200,
                'message': "Notifications fetched successfully",
                'data': serializer.data
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
            'error': True,
            'code': 404,
            'message': "Notification with given id is not found"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotificationSerializer(notification)
        data = {
            'error': False,
            'code': 200,
            'message': "Notification fetched successfully",
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = NotificationSerializer(notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'error': False,
                'code': 200,
                'message': "Notification updated successfully",
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            'error': True,
            'code': 400,
            'errors': serializer.errors,
            'message': "Failed to update notification"
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        notification.delete()
        data = {
            'error': False,
            'code': 200,
            'message': "Notification deleted successfully"
        }
        return Response(data, status=status.HTTP_200_OK)
    
    
# @api_view(['GET'])
# def gallery_list(request):
#     if request.method == 'GET':
#         gallery = GalleryItems.objects.all()
        
#         serializer = GallerySerializer(gallery, many = True, context={'request': request})
        
        
#         data = {
#             'code':200,
#             'error':False,
#             'data':serializer.data,
#         }
#         return Response(data, status=status.HTTP_200_OK)


# following api is for custom grouping , like all images , videos , and urls
@api_view(['GET'])
def gallery_list(request):
    if request.method == 'GET':
        gallery = GalleryItems.objects.all()
        
        # filter the gallery items based on the presence of media types
        images = gallery.filter(image__isnull=False)
        videos = gallery.filter(video__isnull=False) | gallery.filter(url_tag__isnull=False)  # Combine video and URL items
        
        # serialize each media type separately
        image_serializer = GallerySerializer(images, many=True, context={'request': request})
        video_serializer = GallerySerializer(videos, many=True, context={'request': request})
        
        data = {
            'image': [{'name': item['name'], 'image': item['image']} for item in image_serializer.data],
            'video': [
                {
                    'name': item['name'],
                    'video': item['video'] if item['video'] else None,
                    'url': item['url_tag'] if item['url_tag'] else None
                } for item in video_serializer.data
            ]
        }
        
        return Response({
            'status': 200,
            'error': False,
            'message': 'gallery list fetched successfully',
            'data': data
        })