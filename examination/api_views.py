from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from institute.models import Standard, GradingSystem
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ExamTimeTableSerializer
from scholar_register.models import StudentProfile
from .models import ExamTimeTable, ExaminationMarks
from collections import defaultdict
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Value
from django.db.models.functions import Cast
from django.db import models

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def examination_marks_details_students(request):
    data = request.data
    institute_id = data.get('institute_id')
    branch_id = data.get('branch_id')
    session_id = data.get('session_id')
    student_id = data.get('student_id')
    standard_id = data.get('standard_id')

    if not (institute_id and branch_id and session_id and student_id and standard_id):
        return Response({
            'code': 400,
            'error': True,
            'message': 'Branch, session, standard, and student ID are required.',
            'data': {}
        })

    # Fetch student
    try:
        student = StudentProfile.objects.get(id=student_id)
    except StudentProfile.DoesNotExist:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student does not exist for the provided student ID.',
            'data': {}
        })

    # Verify if the student belongs to the logged-in parent user
    user = request.user
    if student.parent.user != user:
        return Response({
            'code': 400,
            'error': True,
            'message': 'Student must belong to the currently logged-in parent.',
            'data': {}
        })

    # Fetch the exam marks of all students in the same class
    all_student_marks = ExaminationMarks.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard_id=standard_id,
        student__section=student.section,
        exam_type__in=ExaminationMarks.objects.values('exam_type')
    ).values('student_id').annotate(total_obtained_marks=Sum(Cast('obtained_marks', output_field=models.IntegerField()))).order_by('-total_obtained_marks')
    # Fetch current student's marks and rank
    student_marks = all_student_marks.filter(student_id=student_id).first()
    rank = list(all_student_marks).index(student_marks) + 1 if student_marks else None

    # Fetch the result type for the standard
    standard = Standard.objects.get(id=standard_id)
    result_type = standard.result_type

    # If the result type is GRADE, calculate the grade
    grade = None
    if result_type == "GRADE":
        total_obtained_marks = student_marks['total_obtained_marks']
        grading_system = GradingSystem.objects.filter(
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id,
            marks_from__lte=total_obtained_marks,
            marks_to__gte=total_obtained_marks
        ).first()

        if grading_system:
            grade = grading_system.grade

    # Prepare response data
    response_data = {
        'rank': rank,
        'total_obtained_marks': student_marks['total_obtained_marks'] if student_marks else None,
        'result_type': result_type,
        'grade': grade if result_type == "GRADE" else None,
    }

    return Response({
        'code': 200,
        'error': False,
        'message': 'Examination marks and rank fetched successfully',
        'data': response_data
    })
