from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Institute, User
from hr.models import TimeTable
from .models import ChatMessage, GalleryItems, NotificationModel
from .serializers import ChatMessageSerializer, GallerySerializer, NotificationSerializer, TimeTableSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['GET', 'POST'])
def notification_list(request):
    if request.method == 'GET':
        print(request.user)
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
        
# API for time table

@api_view(['GET'])
def timetable_list(request):
    standard_id = request.GET.get('standard_id')  # Get the standard ID from the request
    institute_id = request.GET.get('institute_id')  # Get the institute ID from the request
    
    if not standard_id or not institute_id:
        return Response({
            'status': 400,
            'error': True,
            'message': 'Standard ID and Institute ID are required'
    })

    days_of_week = {
        'Monday': 'MON',
        'Tuesday': 'TUE',
        'Wednesday': 'WED',
        'Thursday': 'THU',
        'Friday': 'FRI',
        'Saturday': 'SAT',
        'Sunday': 'SUN'
    }
    
    # Filter timetable entries by standard ID and institute ID
    timetables = TimeTable.objects.filter(
        standard_id=standard_id,
        institute_id=institute_id
    )
    
    # Organize data by day of the week
    response_data = {}
    
    for display_name, db_value in days_of_week.items():
        filtered_timetables = timetables.filter(day_of_week=db_value)
        serializer = TimeTableSerializer(filtered_timetables, many=True)
        response_data[display_name] = serializer.data
    
    return Response({
        'status': 200,
        'error': False,
        'message': 'Time Table fetched successfully',
        'data': response_data
    })

# api view for chat application

class CreateChatMessageView(APIView):
    # permission_classes = [IsAuthenticated] token authentication
    def post(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'error':False,
                'message':'chat sent successfully',
                'data':serializer.data
            })
        return Response({
            'status':status.HTTP_400_BAD_REQUEST,
            'error':serializer.errors,
            'message':'server side error while sending chat'
        })
        
# API class for group messages
class ClassChatMessageView(APIView):
    def post(self,request):
        data = request.data
        institute_id = data.get('institute')
        standard_id = data.get('standard')
        section_id = data.get('section')
        
        if not (institute_id and standard_id and section_id):
            return Response({
                'status':400,
                'error':True,
                'message':'Institute, standard, section Ids are required!!!!'
            })
            
        messages = ChatMessage.objects.filter(
            institute_id = institute_id,
            standard_id = standard_id,
            section_id = section_id,
            is_individual = False
        ).order_by('time_stamp')
        
        serializer = ChatMessageSerializer(messages, many=True)
        return Response({
            'status':200,
            'error':False,
            'message':'class chat messages fetched successfully',
            'data':serializer.data
        })
        
        # API class for individual chat messages
class IndividualChatMessageView(APIView):
    def post(self, request):
        data = request.data
        institute_id = data.get('institute')
        standard_id = data.get('standard')
        section_id = data.get('section')
        sender_id = data.get('sender')
        receiver_id = data.get('receiver')
        
        if not (institute_id and standard_id and section_id and sender_id and receiver_id):
            return Response({
                'status':400,
                'error':True,
                'message':'Institute, standard, section, sender and receiver IDs are required'
            })
            
        messages = ChatMessage.objects.filter(
            institute_id = institute_id,
            standard_id = standard_id,
            section_id = section_id,
            sender_id = sender_id,
            receiver_id = receiver_id,
            is_individual = True
        ).order_by('time_stamp')
        
        serializer = ChatMessageSerializer(messages, many = True)
        return Response({
            'status':200,
            'error':False,
            'message':'Individual Chat messages fetched successfully',
            'data':serializer.data
        })