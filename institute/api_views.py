from django.conf import settings
from django.http import JsonResponse
import jwt
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Institute, User
from django.db.models import Q
from hr.models import TimeTable
from scholar_register.models import StudentParents
from .models import ChatMessage, GalleryItems, NotificationModel
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_notifications(request):
    data = request.data
    type = data.get("type")
    if type == "student":
        notifications = NotificationModel.objects.filter(
            Q(receiver__contains="all_students"))
        if not notifications:
            response_data = {
                'error': True,
                'code': 200,
                'data': {},
                'message': 'No notification Here'
            }
            return Response(response_data)
        else:
            notification_serializer = NotificationSerializer(
                notifications, many=True, context={"request": request})
            response_data = {
                'error': False,
                'code': 200,
                'data': {
                    'notifications': notification_serializer.data,
                },
                'message': 'Notification Fetched Successfully'
            }
            return Response(response_data)

    elif type == "teacher":
        notifications = NotificationModel.objects.filter(
            Q(receiver__contains="all_teachers"))
        if not notifications:
            response_data = {
                'error': True,
                'code': 200,
                'data': {},
                'message': 'No notification Here'
            }
            return Response(response_data)
        else:
            notification_serializer = NotificationSerializer(
                notifications, many=True, context={"request": request})
            response_data = {
                'error': False,
                'code': 200,
                'data': {
                    'notifications': notification_serializer.data,
                },
                'message': 'Notification Fetched Successfully'
            }
            return Response(response_data)
    else:
        return Response({
            'error': True,
            'code': 200,
            'data': {},
            'message': "Invalid Type Sent please only 'teacher' and 'student' are accepted"
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gallery_items_view(request):
    # Extract data from request body
    institute_id = request.data.get('institute_id')
    branch_id = request.data.get('branch_id')
    session_id = request.data.get('session_id')

    if not (institute_id and branch_id and session_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'institute id, branch id and session id is required',
            'data': {}
        }, status=status.HTTP_400_BAD_REQUEST)

    # Filter GalleryItems based on the provided data
    gallery_items = GalleryItems.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id
    )

    # Serialize the data
    serializer = GalleryItemSerializer(
        gallery_items, many=True, context={'request': request})

    # Separate serialized data into images, videos, and URLs (YouTube links)
    image_data = []
    video_data = []
    url_data = []

    for item in serializer.data:
        if item['image_url']:
            image_data.append(
                {'id': item['id'], 'name': item['name'], 'type': 'image', 'url': item['image_url']})
        elif item['video_url']:
            video_data.append(
                {'id': item['id'], 'name': item['name'], 'type': 'video', 'url': item['video_url']})
        elif item['url_tag']:
            url_data.append({'id': item['id'], 'name': item['name'],
                            'type': 'you_tube_link', 'url': item['url_tag']})

    # Format the response
    response_data = {
        'code': 200,
        'error': False,
        'message': 'Image and video data fetched successfully',
        'data': {
            'images': image_data,
            'videos': video_data,
            'url': url_data
        }
    }

    return Response(response_data)

# API for time table


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_timetable(request):
    institute_id = request.data.get('institute_id')
    branch_id = request.data.get('branch_id')
    session_id = request.data.get('session_id')
    standard_id = request.data.get('standard_id')
    section_id = request.data.get('section_id')

    # Validate required parameters
    if not all([institute_id, branch_id, session_id, standard_id, section_id]):
        return JsonResponse({
            'code': 400,
            'error': True,
            'message': 'institute id, branch id, session id, standard id and section id are required',
            'data': []
        })

    # Fetch timetable data
    timetables = TimeTable.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard_id=standard_id,
        section_id=section_id
    )

    # Prepare the response data grouped by day of the week
    grouped_data = {}
    for timetable in timetables:
        day = timetable.get_day_of_week_display()
        if day not in grouped_data:
            grouped_data[day] = []

        grouped_data[day].append({
            'period_no': timetable.period.period_no,
            'subject': timetable.subject.name,
            'start_time': timetable.period.start_time,
            'end_time': timetable.period.end_time,
            'faculty': timetable.faculty.user.first_name
        })

    # Convert the grouped data into a list format
    response_data = []
    for day, schedules in grouped_data.items():
        response_data.append({
            'day': day,
            'schedules': schedules
        })

    return Response({
        'code': 200,
        'error': False,
        'message': 'Timetable data fetched successfully',
        'data': response_data
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chat_messages(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    sender_id = data.get('sender_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    message_type = data.get('message_type')
    message = data.get('message')
    is_individual = data.get(
        'is_individual', 'False').lower() == 'true'  # Convert to boolean
    student_id = data.get('student_id')
    receiver_id = data.get('receiver_id') if is_individual else None

    # Validate required fields
    required_fields = [institute_id, branch_id, session_id,
                       sender_id, standard_id, section_id, student_id]
    if any(field is None for field in required_fields):
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': 'institute id, branch id, session id, sender id, standard id, section id, student id and receiver id are required',
            'data': {}
        })

    user = request.user
    try:
        data_sender = User.objects.get(id=sender_id)
    except ObjectDoesNotExist as e:
        return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': True,
                'message': 'User corresponding to the sender id does not exist',
                'data': {}
            })
    data_sender = User.objects.get(id=sender_id)
    if user.role == data_sender.role:
        pass
    else:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': 'sender id and login user id must be same',
            'data': {}
        })
    
    if user.role =="3":
        pass
    elif user.role == "5":
        parent = StudentParents.objects.get(user=user)
        students= StudentProfile.objects.filter(parent = parent)
        if not students.filter(id=student_id).exists():
            return Response({
            'error': True,
            'code': 200,
            'message': "this student is not associated with you",
            'data': {}
            })

    if is_individual and not receiver_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': 'Receiver id is required if is_individual is set to True',
            'data': {}
        })

    if not is_individual and receiver_id:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': 'Receiver id should not be provided when is_individual is False',
            'data': {}
        })

    # Retrieve model instances
    try:
        institute = Institute.objects.get(registration_number=institute_id)
        branch = InstituteBranch.objects.get(id=branch_id)
        session = AcademicSession.objects.get(id=session_id)
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id) if is_individual else None
        standard = Standard.objects.get(id=standard_id)
        section = Section.objects.get(id=section_id)
        student = StudentProfile.objects.get(id=student_id)
    except ObjectDoesNotExist as e:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': f'Error retrieving data: {str(e)}',
            'data': {}
        })

    # Create and save new chat message
    new_chat_message = ChatMessage.objects.create(
        institute=institute,
        branch=branch,
        session=session,
        sender=sender,
        receiver=receiver,  # Only used if is_individual is True
        standard=standard,
        section=section,
        student=student,
        message_type=message_type,
        message=message,
        is_individual=is_individual
    )

    serializer = ChatMessageSerializer(
        new_chat_message, context={'request': request})
    return Response({
        'status': status.HTTP_201_CREATED,
        'error': False,
        'message': 'Chat message created successfully',
        'data': serializer.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def claas_chat_messages(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    if not (institute_id and branch_id and standard_id and section_id):
        return Response({
            'status': 400,
            'error': True,
            'message': 'Institute, branch, session, standard, section Ids are required!!!!'
        })
    messages = ChatMessage.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard_id=standard_id,
        section_id=section_id,
        is_individual=False
    ).order_by('time_stamp')

    serializer = ClassChatMessageSerializer(
        messages, many=True, context={'request': request})

    return Response({
        'status': 200,
        'error': False,
        'message': 'class chat messages fetched successfully',
        'data': serializer.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def individual_chat_messages(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    student_id = data.get('student_id')

    if not (institute_id and branch_id and session_id and standard_id and section_id and sender_id and receiver_id and student_id):
        return Response({
            'status': 400,
            'error': True,
            'message': 'Institute, branch, session, standard, section, sender, student, and receiver IDs are required'
        })

    user = request.user
    print(user)
    try:
        data_sender = User.objects.get(id=sender_id)
    except ObjectDoesNotExist as e:
        return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': True,
                'message': 'User corresponding to the sender id does not exist',
                'data': {}
            })
    print(data_sender)
    if data_sender:
        if user.role == data_sender.role:
            pass
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': True,
                'message': 'sender id and login user id must be same',
                'data': {}
            })
    else:
        return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': True,
                'message': 'the sender Id does not belong to any valid user',
                'data': {}
            })
    
    if user.role =="3":
        pass
    elif user.role == "5":
        parent = StudentParents.objects.get(user=user)
        students= StudentProfile.objects.filter(parent = parent)
        if not students.filter(id=student_id).exists():
            return Response({
            'error': True,
            'code': 200,
            'message': "You do not have permission to access this student's data.",
            'data': {}
            })

    messages1 = ChatMessage.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard_id=standard_id,
        section_id=section_id,
        sender_id=sender_id,
        receiver_id=receiver_id,
        student_id=student_id,  # Filter by student if provided
        is_individual=True
    ).order_by('time_stamp')

    messages2 = ChatMessage.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard_id=standard_id,
        section_id=section_id,
        sender_id=receiver_id,
        receiver_id=sender_id,
        student_id=student_id,  # Filter by student if provided
        is_individual=True
    ).order_by('time_stamp')
    messages = messages1 | messages2
    serializer = ChatMessageSerializer(
        messages, many=True, context={'request': request})
    return Response({
        'status': 200,
        'error': False,
        'message': 'Individual Chat messages fetched successfully',
        'data': serializer.data
    })
