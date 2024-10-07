from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.core.exceptions import ValidationError
import calendar
from institute.models import Subjects
from datetime import datetime
from collections import defaultdict
from django.core.exceptions import ObjectDoesNotExist
from teacher_management.models import Employee, LiveClass, Assignments
from django.utils import timezone
from .models import AssignmentSubmission
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
                    'code': 200,
                    'error': False,
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
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_activity(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')

    if not (institute_id and branch_id and session_id and student_id):
        return Response({
            'code': 400,
            'error': True,
            'message': "Institute, Branch, session, student ID's, are required.",
            'data': {}
        })

    user = request.user

    try:
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID or parameters.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if student and user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })
    
    leave_applications = StudentLeaveApplication.objects.filter(institute_id=institute_id,
                                        branch_id=branch_id, session_id=session_id, student_id=student_id)
    
    serializer = StudentLeaveApplicationSerializer(leave_applications, many=True, context={'request':request})

    return Response({
        'code': 200,
        'error': False,
        'message': 'Student Activities Fetched Successfully',
        'data': serializer.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_leave(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')
    leaving_reason = data.get("leaving_reason")
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    attachment = data.get('attachment')


    # Ensure all required fields are provided
    if not (institute_id and branch_id and session_id and start_date and end_date and student_id and leaving_reason):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Branch, session, standard, section, student ID, leaving reason, attachments, start date, and end date are required.',
            'data': {}
        })

    user = request.user

    # Validate if the student exists
    try:
        print(student_id)
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID or parameters.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if student and user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })

    # Update the data to include the student object instead of student_id
    leave_data = {
        'student': student.id,  # pass the student instance or its ID
        'start_date': start_date,
        'end_date': end_date,
        'branch': branch_id,
        'session': session_id,
        'institute': institute_id,
        'leaving_reason':leaving_reason,
        'attachment':attachment
    }

    # Serialize and validate leave application data
    serializer = StudentLeaveApplicationSerializerSaveData(data=leave_data, context={'request':request})
    if serializer.is_valid(raise_exception=False):
        try:
            serializer.save()
            return Response({
                'code': 200,
                'error': False,
                'message': 'Leave applied successfully',
                'data': {}
            })
        except Exception as e:
            return Response({
                'code': 500,
                'error': True,
                'message': f'Error saving leave application please check if any wrong Id is passed',
                'data': {}
            })
    else:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Validation error for wrong Id',
            'data': {}
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_leave_applications(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    employee_id = data.get('employee_id')

    if not (branch_id and session_id and institute_id and employee_id):
        return Response({
            'code': 400,
            'error': True,
            'message': "institute, branch, session and employee id's are required.",
            'data': {}
        })
    user = request.user

    try:
        teacher = Employee.objects.get(id = employee_id)
    except:
        return Response({
            'code':200,
            'error':True,
            'message':"employee does not exist",
            'data':{}
        })
    if teacher and user != teacher.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Teacher must belong to the currently logged-in User.',
            'data': {}
        })
    
    applications= StudentLeaveApplication.objects.filter(institute_id=institute_id,
                                                           branch_id=branch_id, session_id=session_id)
    serializer = StudentLeaveApplicationSerializer(applications, many=True, context={'request':request})
    
    return Response({
            'code': 400,
            'error': True,
            'message': 'Leave Applications fetched Successfully',
            'data': serializer.data
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_leave_approval(request):
    data = request.data
    teacher_id = data.get('teacher_id')
    application_id = data.get('application_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    is_approved = data.get('is_approved')

    # Ensure all required fields are provided
    if not (application_id and branch_id and session_id and teacher_id):
        return Response({
            'status': 400,
            'error': True,
            'message': 'Institute, branch, session, standard, and student IDs are required.',
            'data': {}
        })

    user = request.user

    # Validate if the teacher exists
    try:
        teacher = Employee.objects.get(id=teacher_id)
    except Employee.DoesNotExist:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': True,
            'message': 'Teacher related to the teacher ID does not exist.',
            'data': {}
        })

    # Check if the teacher belongs to the currently logged-in user
    if teacher and user != teacher.user:
        return Response({
            'status': 400,
            'error': True,
            'message': 'Teacher must belong to the currently logged-in user.',
            'data': {}
        })

    # Retrieve the leave application
    try:
        application = StudentLeaveApplication.objects.get(id=application_id)
    except StudentLeaveApplication.DoesNotExist:
        return Response({
            'status': 404,
            'error': True,
            'message': 'Leave application not found.',
            'data': {}
        })

    # Convert the string representation of boolean values to actual booleans
    if is_approved is not None:
        if isinstance(is_approved, str):
            if is_approved.lower() == 'true':
                is_approved = True
            elif is_approved.lower() == 'false':
                is_approved = False
            else:
                return Response({
                    'status': 400,
                    'error': True,
                    'message': 'Invalid value for is_approved. Must be true or false.',
                    'data': {}
                })

        # Update the is_approved field based on the provided value
        application.is_approved = is_approved
        application.checked_by = teacher  # Optionally update the teacher who approved the leave
        application.save()

        return Response({
            'status': 200,
            'error': False,
            'message': 'Leave application status updated successfully.',
            'data': {
                'application_id': application.id,
                'is_approved': application.is_approved
            }
        })
    else:
        return Response({
            'status': 400,
            'error': True,
            'message': 'is_approved value is required.',
            'data': {}
        })



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_attendance(request):
    data = request.data
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    standard_id = data.get('standard_id')
    month = int(data.get('month'))
    year = int(data.get('year'))
    student_id = data.get('student_id')

    if not (branch_id and session_id and standard_id and month and year and student_id):
        return Response({
            'status': 400,
            'error': True,
            'message': 'Institute, branch, session, standard, month, year and student IDs are required'
        })
    user = request.user
    try:
        student = StudentProfile.objects.get(id= student_id)
    except ObjectDoesNotExist as e:
        return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'error': True,
                'message': 'Student related to the student id does not exist',
                'data': {}
            })
    if student:
        if user == student.parent.user:
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
    attendance = Attendance.objects.filter(
        session=session_id, branch=branch_id, standard=standard_id, student=student_id, 
        date__month=month, date__year=year
    )
    serializer = StudentAttendanceSerializer(attendance, many=True)

    def refine_attendance_data(attendance_data, month, year):
        # Create a dictionary to store attendance for each day
        attendance_by_day = defaultdict(lambda: {
            'day': None,
            'is_present': False,
            'subjects_attended': defaultdict(lambda: False)  # Initialize subjects as False
        })
        # Iterate through the attendance data to group by date and determine presence
        for record in attendance_data:
            day = datetime.strptime(record['date'], "%Y-%m-%d").day
            is_present = record['present']
            subject_name = Subjects.objects.get(id=record['subject']).name  # Use subject name as key

            # Store the day in the dictionary
            attendance_by_day[day]['day'] = day

            # Update the presence flag and mark subject attendance
            if is_present:
                attendance_by_day[day]['is_present'] = True  # If present in any subject, mark overall presence
                attendance_by_day[day]['subjects_attended'][subject_name] = True
            else:
                attendance_by_day[day]['subjects_attended'][subject_name] = False

        # Get the total number of days in the month
        total_days = calendar.monthrange(year, month)[1]

        # Create a list for all days of the month, with the default value of False for missing days
        refined_data = []
        for day in range(1, total_days + 1):
            if day in attendance_by_day:
                refined_data.append(attendance_by_day[day])
            else:
                # If there's no attendance data for the day, add it with default values
                refined_data.append({
                    'day': day,
                    'is_present': False,
                    'subjects_attended': {}
                })

        return refined_data

    response_data = refine_attendance_data(serializer.data, month, year)

    return Response({
        'code': 200,
        'error': False,
        'message': 'Attendance data retrieved successfully',
        'data': response_data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def faculty_list(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')

    if not (institute_id and branch_id and session_id and student_id and standard_id and section_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Branch, session, standard, section, student ID, leaving reason, attachments, start date, and end date are required.',
            'data': {}
        })
    try:
        print(student_id)
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID or parameters.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if student and request.user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })

    teacher_data = Employee.objects.filter(institute_id=institute_id)
    serializer = TeacherDataSerializer(teacher_data, many=True, context={'request':request})
    print(teacher_data)

    return Response({
        'code': 200,
        'error': False,
        'message': 'Teacher List Fetched successfully',
        'data': serializer.data
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fetch_live_classes_data(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    date = data.get('date')

    if not (institute_id and branch_id and session_id and student_id and standard_id and section_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Branch, session, standard, section, student ID, leaving reason, attachments, start date, and end date are required.',
            'data': {}
        })
    try:
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID or parameters.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if student and request.user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })
    
    live_classes = LiveClass.objects.filter(institute_id=institute_id, branch_id=branch_id, 
                        session_id=session_id, standard_id=standard_id, section_id=section_id, class_date=date)
    
    serializer = LiveClassesSerializer(live_classes, many=True)
    return Response({
            'code': 200,
            'error': False,
            'message': 'Live classes fetched Successfully',
            'data': serializer.data
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_assignments_for_student(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')

    if not (institute_id and branch_id and session_id and student_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Institutde, Branch, session, student ID are required.',
            'data': {}
        })
    try:
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID or parameters.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if student and request.user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })

    # Fetch all assignments for the student's standard, section, and subject
    assignments = Assignments.objects.filter(
        branch= branch_id,
        session = session_id,
        standard=student.standard,
        section=student.section,
        institute_id = institute_id
    )

    # Serialize the assignments
    serializer = AssignmentSerializer(assignments, many=True, context={'request':request})

    return Response({
        'code': 200,
        'error': False,
        'message': "Assignments fetched successfully.",
        'data': serializer.data
    }, status=status.HTTP_200_OK)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_assignment(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')
    assignment_id = data.get('assignment_id')
    attachment = request.FILES.get('attachment')

    # Check for required fields
    if not (institute_id and branch_id and session_id and student_id and assignment_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Institute, Branch, session, student, and Assignment ID are required.',
            'data': {}
        })

    try:
        # Validate that the student exists
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID.',
            'data': {}
        })

    # Check if the student belongs to the logged-in parent user
    if request.user != student.parent.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })

    try:
        # Fetch the existing assignment submission for the student
        submission = AssignmentSubmission.objects.get(
            student=student,
            assignment_id=assignment_id,
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id
        )

        # Update the existing submission with attachment and status
        submission.status = 'Submitted'
        submission.date = timezone.now().date()  # Set submission date
        if attachment:
            submission.attachment = attachment  # Update the attachment if provided

        submission.save()

        return Response({
            'code': 200,
            'error': False,
            'message': 'Assignment submitted successfully.',
            'data': AssignmentSubmissionSerializer(submission).data
        }, status=status.HTTP_200_OK)

    except AssignmentSubmission.DoesNotExist:
        return Response({
            'code': 404,
            'error': True,
            'message': "Assignment submission not found for the provided parameters.",
            'data': {}
        })

    except Exception as e:
        return Response({
            'code': 500,
            'error': True,
            'message': f"An error occurred while submitting the assignment: {str(e)}",
            'data': {}
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
