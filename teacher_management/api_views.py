from rest_framework.response import Response

from scholar_register.models import StudentProfile
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def today_live_class_create(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    employee_id = data.get('employee_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    subject_id = data.get('subject_id')
    chapter = data.get('chapter')
    message = data.get('message')
    class_date = data.get('class_date')
    class_time = data.get('class_time')

    # Check for required fields
    if not (institute_id and branch_id and session_id and standard_id and section_id and subject_id and chapter and message and class_date and class_time):
        return Response({
            'code': 400,
            'error': True,
            'message': 'all fields are required (institute_id, branch_id, session_id, standard_id, section_id, subject_id, chapter, message, class_date, class_time).',
            'data': {}
        })

    serializer = TodayLiveClassSerializer(data=data)

    # Validate the serializer
    if serializer.is_valid():
        try:
            serializer.save()
            return Response({
                'code': 200,
                'error': False,
                'message': "Live class schedule created successfully.",
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'code': 500,
                'error': True,
                'message': f"An error occurred while saving the live class schedule: {str(e)}",
                'data': {}
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Customizing error message format
        errors = []
        for field, field_errors in serializer.errors.items():
            for error in field_errors:
                errors.append(f"{error}")

        return Response({
            'code': 400,
            'error': True,
            'message': "".join(errors),
            'data': {},
            'errors': " ".join(errors)  # Join all error messages into a single string
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_assignment(request):
    data = request.data
    # Serialize the assignment data
    assignment_serializer = AssignmentSerializer(data=data)
    if assignment_serializer.is_valid():
        assignment = assignment_serializer.save()

        # Retrieve all students from the standard and section for this assignment
        standard_id = assignment.standard_id
        section_id = assignment.section_id

        # Assuming there's a StudentProfile model with standard and section fields
        students = StudentProfile.objects.filter(standard_id=standard_id, section_id=section_id)

        if not students.exists():
            return Response({
                'code': 400,
                'error': True,
                'message': "No students found in the selected standard and section.",
            }, status=status.HTTP_400_BAD_REQUEST)

        # Create an AssignmentSubmission entry for each student
        submission_errors = []
        for student in students:
            submission_data = {
                'institute': assignment.institute_id,
                'branch': assignment.branch_id,
                'session': assignment.session_id,
                'assignment': assignment.id,
                'student': student.id,  # Assigning to each student
                'status': 'Pending',  # Default status
                'date': timezone.now().date(),  # Current date
            }
            submission_serializer = AssignmentSubmissionSerializer(data=submission_data)
            
            if submission_serializer.is_valid():
                submission_serializer.save()
            else:
                submission_errors.append(submission_serializer.errors)

        # Check if there were any errors while creating assignment submissions
        if submission_errors:
            return Response({
                'code': 400,
                'error': True,
                'message': "Some submissions could not be created.",
                'data': submission_errors  # Return the errors if any
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'code': 200,
            'error': False,
            'message': "Assignment and submissions created successfully.",
            'data': assignment_serializer.data
        }, status=status.HTTP_201_CREATED)

    # Handle errors in assignment creation
    errors = []
    for field, field_errors in assignment_serializer.errors.items():
        for error in field_errors:
            errors.append(f"{error}")
    return Response({
        'code': 400,
        'error': True,
        'message': " ".join(errors),
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def filter_data_for_teacher_assignment_list(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    employee_id = data.get('employee_id')

    if not (institute_id and branch_id and session_id and employee_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Institute, Branch, session, required fields are missing.',
            'data': {}
        })
    
    standards= Standard.objects.filter(institute_id=institute_id, branch_id =branch_id)
    sections = Section.objects.filter(institute_id=institute_id, branch_id=branch_id)
    subjects = Subjects.objects.filter(institute_id=institute_id, branch_id=branch_id, session_id=session_id)
    assignments = Assignments.objects.filter(institute_id = institute_id, branch_id=branch_id, session_id=session_id, employee_id=employee_id)

    standard_serializer = StandardSerializer(standards, many=True)
    section_serializer = SectionSerializer(sections, many= True)
    subject_serializer = SubjectSerializer(subjects, many= True)
    assignment_serializer = AssignmentsDropdownListSerializer(assignments, many=True)

    return Response({
        'code': 200,
        'error': False,
        'message': f'Assignment successfully.',
        'data': {
            'standards':standard_serializer.data,
            'sections': section_serializer.data,
            'subjects': subject_serializer.data,
            'assignments': assignment_serializer.data
        }
    })



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_submission_details(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    standard_id = data.get('standard_id')
    section_id = data.get('section_id')
    subject_id = data.get('subject_id')
    teacher_id = data.get('teacher_id')

    if not (institute_id and branch_id and session_id and teacher_id and standard_id and section_id and subject_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Institute, Branch, session, teacher, standard, section, subject IDs are required.',
            'data': {}
        })

    try:
        teacher = Employee.objects.get(id=teacher_id)
    except Employee.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Teacher does not exist for the provided teacher ID.',
            'data': {}
        })

    # Check if the logged-in user matches the teacher
    if request.user != teacher.user:
        return Response({
            'code': 403,
            'error': True,
            'message': 'You are not authorized to view these assignments.',
            'data': {}
        })

    # Fetch all assignments for the teacher and given criteria
    assignments = Assignments.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        employee_id=teacher_id,
        standard_id=standard_id,
        section_id=section_id,
        subject_id=subject_id
    )

    if not assignments.exists():
        return Response({
            'code': 404,
            'error': True,
            'message': 'No assignments found for the given parameters.',
            'data': []
        })

    data_list = []

    for assignment in assignments:
        # Get all submissions for this assignment
        submissions = AssignmentSubmission.objects.filter(assignment=assignment)
        submission_list = []
        for submission in submissions:
            student = submission.student
            submission_data = {
                "student_name": f"{student.first_name} {student.last_name}",
                "student_roll_no": student.roll_number,
                "status": submission.status
            }
            submission_list.append(submission_data)
        assignment_info = {
            "assignment_id": assignment.id,
            "assignment_message": assignment.message,
            "submission_date": assignment.submission_date.strftime('%Y-%m-%d') if assignment.submission_date else None,
            "submissions": submission_list
        }
        data_list.append(assignment_info)

    return Response({
        "code": 200,
        "error": False,
        "message": "Students list for assignments fetched successfully",
        "data": data_list
    }, status=status.HTTP_200_OK)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assignment_approve_reject(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id =  data.get('branch_id')
    session_id = data.get('session_id')
    assignment_id = data.get('assignment_id')
    teacher_id = data.get('teacher_id')
    status = data.get('status')
    remarks = data.get('remarks')


    if not (institute_id and branch_id and session_id and teacher_id and assignment_id and status):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Institute, Branch, session, teacher, assignment ID, and status are required.',
            'data': {}
        })

    # Validate teacher existence
    try:
        teacher = Employee.objects.get(id=teacher_id)
    except Employee.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Teacher does not exist for the provided teacher ID.',
            'data': {}
        })

    # Check if the logged-in user matches the teacher
    if request.user != teacher.user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'You are not authorized to approve/reject this assignment.',
            'data': {}
        })

    # Validate that the assignment submission exists
    try:
        assignment_submission = AssignmentSubmission.objects.get(
            assignment_id=assignment_id,
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id
        )
    except AssignmentSubmission.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'The assignment submission may be deleted or does not exist.',
            'data': {}
        })

    # Update the status of the assignment submission
    if status not in ['Approved', 'Reject']:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Invalid status value. Status must be either "Approved" or "Reject".',
            'data': {}
        })

    # Update the submission status and reviewed_by field
    assignment_submission.status = status
    assignment_submission.reviewed_by = teacher
    assignment_submission.remarks = remarks
    assignment_submission.save()

    # Serialize the updated submission
    serializer = AssignmentSubmissionSerializer(assignment_submission, context={'request': request})

    return Response({
        'code': 200,
        'error': False,
        'message': f'Assignment {status.lower()} successfully.',
        'data': serializer.data
    })



