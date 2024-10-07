from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
import json
from scholar_register.models import StudentProfile
from .models import ExamTimeTable, ExamType, ExaminationMarks
from institute.models import Subjects, Standard, Section, GradingSystem
from django.contrib import messages
from accounts.models import InstituteBranch, Institute, AcademicSession
from .forms import ExamTimeTableForm, ExamTypeForm, ExaminationMarksForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Min, Count
from django.http import HttpResponse

def exam_type_list(request):
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session to view Exam Time Table')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch to view Time Table')
        return redirect('some_error_page')
    
    exam_types = ExamType.objects.filter(institute=institute, branch=active_branch, session=active_session)

    context = {
        'exam_types': exam_types
    }
    return render(request, 'exam_types_list.html', context=context)

def exam_type_create(request):
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session to view Exam Time Table')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch to view Time Table')
        return redirect('some_error_page')
    if request.method == "POST":
        form = ExamTypeForm(request.POST, user =request.user, session = request.session)
        if form.is_valid():
            exam_type = form.save(commit=False)
            exam_type.institute=institute
            exam_type.branch = active_branch
            exam_type.session=active_session
            exam_type.save()
            return redirect('examination:exam_type_list')
        else:
            return render(request, 'exam_type_create.html', {'form': form})
    else:
        form = ExamTypeForm(user=request.user)
        return render(request, 'exam_type_create.html', {'form': form})

def exam_type_update(request, pk):
    exam_type= get_object_or_404(ExamType, pk=pk)
    if request.method == "POST":
        form = ExamTypeForm(request.POST, instance=exam_type, user=request.user, session=request.session)
        if form.is_valid():
            exam_type_form = form.save(commit=False)
            exam_type_form.institute = request.user.institute_id.first()
            exam_type_form.branch = InstituteBranch.objects.filter(institute=exam_type.institute, is_active=True).first()
            exam_type_form.session = AcademicSession.objects.filter(institute=exam_type.institute, is_active=True).first()

            exam_type_form.save()
            return redirect('examination:exam_type_list')
        else:
            return render(request, 'exam_type_create.html', {'form': form})
    else:
        form = ExamTypeForm(instance=exam_type, user=request.user)
        return render(request, 'exam_type_create.html', {'form': form})
    
def exam_type_delete(request, pk):
    exam_type = get_object_or_404(ExamType, pk=pk)
    exam_type.delete()
    return redirect('examination:exam_type_list')


def exam_time_table_list(request):
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session to view Exam Time Table')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch to view Time Table')
        return redirect('some_error_page')

    # Grouping by both standard and exam_type and then aggregating data
    time_tables = ExamTimeTable.objects.filter(institute=institute, branch=active_branch, session=active_session)\
        .values('standard', 'standard__name',  # Fetch both standard ID and name
                'exam_type', 'exam_type__name'  # Fetch both exam type ID and name)\
        )\
        .annotate(
            first_exam_date=Min('date'),  # Get the first exam date for the combination of standard and exam_type
            num_students=Count('standard__studentprofile')  # Count the number of students in the standard
        )

    context = {
        'time_tables': time_tables
    }
    return render(request, 'exam_time_table_list.html', context=context)

def exam_time_table_create(request):
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session.')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch.')
        return redirect('some_error_page')

    if request.method == 'POST':
        standard_id = request.POST.get('standard')
        venue = request.POST.get('venue')  # Get venue input
        note = request.POST.get('note')  # Get note input
        exam_type_id = request.POST.get('exam_type')
        
        subjects = Subjects.objects.filter(standard_id=standard_id, session_id = session)

        print(subjects)
    
        for subject in subjects:
            date = request.POST.get(f'date_{subject.id}')
            start_time = request.POST.get(f'start_time_{subject.id}')
            end_time = request.POST.get(f'end_time_{subject.id}')
            exam_type_data = ExamType.objects.filter(id=exam_type_id).first()
            

            ExamTimeTable.objects.create(
                institute=institute,
                branch=active_branch,
                session=active_session,
                standard_id=standard_id,
                subject=subject,
                exam_type = exam_type_data,
                date=date,
                start_time=start_time,
                end_time=end_time,
                venue=venue,  # Add venue here
                note=note  # Add note here
            )

        return redirect('examination:exam_time_table_list')

    else:
        form = ExamTimeTableForm(user=request.user)

    context = {
        'form': form,
    }
    return render(request, 'exam_time_table_create.html', context=context)


def exam_time_table_delete(request, standard, exam_type):
    # Filter the timetable by standard and exam_type
    timetable = ExamTimeTable.objects.filter(standard_id=standard, exam_type=exam_type)

    if timetable.exists():
        timetable.delete()
        messages.success(request, "Timetable deleted successfully.")
    else:
        messages.error(request, "Timetable not found.")

    return redirect('examination:exam_time_table_list')

from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string

def view_timetable_ajax(request):
    standard_id = request.GET.get('standard_id')
    exam_type = request.GET.get('exam_type')
    institute = request.user.institute_id.first()
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    time_table = ExamTimeTable.objects.filter(
        institute=institute,
        branch=active_branch,
        session=active_session,
        standard_id=standard_id,
        exam_type=exam_type
    )

    # Render the timetable HTML
    timetable_html = render_to_string('timetable_popup_content.html', {
        'time_table': time_table
    })

    return JsonResponse({'timetable_html': timetable_html})

def get_exam_types(request):
    standard_id = request.GET.get('standard_id')
    session_id = request.session.get('session_id')
    branch_id = request.session.get('branch_id')
    
    if standard_id:
        exam_types = ExamType.objects.filter(standard_id=standard_id, session_id=session_id, branch_id=branch_id)
        exam_types_data = [{'id': exam_type.id, 'name': exam_type.name} for exam_type in exam_types]
        return JsonResponse({'exam_types': exam_types_data})
    
    return JsonResponse({'exam_types': []})

def examination_marks_list(request):
    institute = request.user.institute_id.first()  # Assuming the user is related to the institute
    branch = request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session = request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    # Check if active session or branch is available
    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session.')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch.')
        return redirect('some_error_page')

    # Get search query from request
    student_name = request.GET.get('student_name', '')

    # Filter marks based on the student name (if provided)
    marks = ExaminationMarks.objects.filter(
        institute=institute,
        branch=active_branch,
        session=active_session
    )
    
    if student_name:
        marks = marks.filter(student__first_name__icontains=student_name)

    context = {
        'marks': marks,
        'student_name': student_name
    }
    return render(request, 'examination_marks_list.html', context=context)

def create_examination_marks(request):
    # Get active institute, session, and branch for the logged-in user
    institute = request.user.institute_id.first()  # Assuming the user is related to the institute
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    # Check if active session or branch is available
    if not active_session:
        messages.warning(request, 'No active session found. Please activate a session.')
        return redirect('some_error_page')

    if not active_branch:
        messages.warning(request, 'No active branch found. Please activate a branch.')
        return redirect('some_error_page')

    # Initialize form
    form = ExaminationMarksForm(user=request.user, session= request.session)

    # If the request is POST (form submission)
    if request.method == 'POST':
        form = ExaminationMarksForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            standard = form.cleaned_data['standard']
            section = form.cleaned_data['section']
            exam_type = form.cleaned_data['exam_type']
            subject = form.cleaned_data['subject']
            
            # Get all students related to the selected section
            students = StudentProfile.objects.filter(section=section)

            # Loop through each student and save their marks
            for student in students:
                # Get the max marks and obtained marks from the POST request
                max_marks = request.POST.get(f'max_marks_{student.id}')
                obtained_marks = request.POST.get(f'obtained_marks_{student.id}')

                # Ensure max_marks and obtained_marks are not empty and are integers
                if max_marks and obtained_marks:
                    try:
                        max_marks = int(max_marks)
                        obtained_marks = int(obtained_marks)

                        # Save the marks into the ExaminationMarks model
                        # Use `update_or_create` to prevent duplicate entries
                        ExaminationMarks.objects.update_or_create(
                            institute=institute,
                            branch=active_branch,
                            session=active_session,
                            student=student,
                            standard=standard,
                            section=section,
                            exam_type=exam_type,
                            subject=subject,
                            defaults={
                                'max_marks': max_marks,
                                'obtained_marks': obtained_marks,
                            }
                        )
                    except ValueError:
                        messages.warning(request, f"Invalid marks input for student {student.first_name}. Please enter valid numbers.")
                        return redirect('examination:create_examination_marks')  # Redirect to the same form in case of an error

            # Redirect to a success page after processing
            messages.success(request, 'Marks have been successfully saved!')

            return redirect('examination:examination_marks_list')  # Update this with the appropriate success URL

        else:
            # If form is invalid, return the form with errors
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'examination_marks_form.html', {'form': form})

    # Render the form for GET requests
    return render(request, 'examination_marks_form.html', {'form': form})

def load_students(request):
    section_id = request.GET.get('section_id')
    if section_id:
        # Fetch students from the selected section
        students = StudentProfile.objects.filter(section_id=section_id)
        
        # Render the students as HTML rows
        students_html = render_to_string('partial_student_rows.html', {'students': students})
        
        return JsonResponse({'students_html': students_html})
    return JsonResponse({'students_html': ''})

def get_sections_subjects(request):
    standard_id = request.GET.get('standard_id')
    sections = Section.objects.filter(standard_id=standard_id)
    subjects = Subjects.objects.filter(standard_id=standard_id)
    exam_types = ExamType.objects.filter(standard_id=standard_id)

    sections_html = '<option value="">Select Section</option>'
    subjects_html = '<option value="">Select Subject</option>'
    exam_type_html = '<option value="">Select Exam Type</option>'

    for section in sections:
        sections_html += f'<option value="{section.id}">{section.name}</option>'

    for subject in subjects:
        subjects_html += f'<option value="{subject.id}">{subject.name}</option>'

    for exam_type in exam_types:
        exam_type_html += f'<option value="{exam_type.id}">{exam_type.name}</option>'

    return JsonResponse({
        'sections_html': sections_html,
        'subjects_html': subjects_html,
        'exam_type_html': exam_type_html
    })


def examination_marks_update(request, pk):
    institute = request.user.institute_id.first()  # Assuming the user is related to the institute
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    # Retrieve the specific examination marks record
    mark = get_object_or_404(ExaminationMarks, id=pk, institute=institute, session=active_session, branch=active_branch)

    # If the request is POST, process the form data
    if request.method == 'POST':
        max_marks = request.POST.get('max_marks')
        obtained_marks = request.POST.get('obtained_marks')

        # Ensure max_marks and obtained_marks are provided
        if max_marks and obtained_marks:
            try:
                max_marks = int(max_marks)
                obtained_marks = int(obtained_marks)

                # Check if obtained marks are greater than max marks
                if obtained_marks > max_marks:
                    messages.error(request, "Obtained marks cannot be greater than maximum marks.")
                    return render(request, 'update_examination_marks.html', {'mark': mark})

                # Update and save the examination mark
                mark.max_marks = max_marks
                mark.obtained_marks = obtained_marks
                mark.save()
                messages.success(request, 'Examination marks updated successfully!')
                return redirect('examination:examination_marks_list')  # Redirect to the marks list

            except ValueError:
                messages.error(request, 'Please enter valid numbers for the marks.')

    # Render the form with the current mark values
    context = {
        'mark': mark
    }
    return render(request, 'update_examination_marks.html', context)


def examination_marks_delete(request, pk):
    
    institute = request.user.institute_id.first()  # Assuming the user is related to the institute
    branch= request.session.get('branch_id')
    active_branch = InstituteBranch.objects.get(pk=branch)
    session= request.session.get('session_id')
    active_session = AcademicSession.objects.get(pk=session)

    # Retrieve the specific examination marks record
    mark = get_object_or_404(ExaminationMarks, id=pk, institute=institute, session=active_session, branch=active_branch)

    # Delete the record and redirect
    if request.method == 'POST':
        mark.delete()
        messages.success(request, 'Examination marks deleted successfully!')
        return redirect('examination:examination_marks_list')

    # Render confirmation page
    return render(request, 'delete_examination_marks.html', {'mark': mark})


def student_exam_timetable_view(request, student_id, institute_id, branch_id, session_id):
    student = get_object_or_404(StudentProfile, id=student_id)

    # Fetch the exam timetable for this student based on institute, branch, session, and standard
    exam_timetables = ExamTimeTable.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard=student.standard
    )

    # Group timetables by exam_type for display
    grouped_data = {}
    exam_types = []
    for timetable in exam_timetables:
        exam_type = timetable.exam_type.name
        if exam_type not in grouped_data:
            grouped_data[exam_type] = []
            exam_types.append(exam_type)
        grouped_data[exam_type].append(timetable)
    
    serialized_data = {}
    for exam_type, timetables in grouped_data.items():
        serialized_data[exam_type] = [
            {
                'subject': t.subject.name,
                'date': t.date.strftime('%Y-%m-%d'),
                'start_time': t.start_time.strftime('%H:%M'),
                'end_time': t.end_time.strftime('%H:%M'),
                'venue': t.venue,
                'note': t.note
            } for t in timetables
        ]

    context = {
        'student': student,
        'exam_types': exam_types,
        'grouped_data': json.dumps(serialized_data, cls=DjangoJSONEncoder),
    }
    
    return render(request, 'student_exam_timetable.html', context)


def student_exam_result(request, student_id, institute_id, branch_id, session_id, exam_type_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    
    standard = student.standard
    examination_marks = ExaminationMarks.objects.filter(
        institute_id=institute_id,
        branch_id=branch_id,
        session_id=session_id,
        standard=standard,
        exam_type_id=exam_type_id
    )
    exam_type = ExamType.objects.get(id=exam_type_id)
    
    if standard.result_type == 'percentage':
        # Percentage calculation logic (already provided)
        marks_sum = {}
        for mark in examination_marks:
            curr_student_id = mark.student.id
            if curr_student_id not in marks_sum:
                marks_sum[curr_student_id] = {
                    'student': mark.student,
                    'total_obtained_marks': 0,
                    'total_max_marks': 0
                }
            marks_sum[curr_student_id]['total_obtained_marks'] += int(mark.obtained_marks)
            marks_sum[curr_student_id]['total_max_marks'] += int(mark.max_marks)

        sorted_students = sorted(marks_sum.values(), key=lambda x: x['total_obtained_marks'], reverse=True)

        rank = next((index + 1 for index, entry in enumerate(sorted_students) if entry['student'].id == student_id), None)

        total_obtained_marks = marks_sum.get(student_id, {}).get('total_obtained_marks')
        total_max_marks = marks_sum.get(student_id, {}).get('total_max_marks')

        marks_details = ExaminationMarks.objects.filter(
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id,
            standard=standard,
            student_id=student_id
        )
        percentage = (total_obtained_marks / total_max_marks) * 100

        context = {
            'exam_type': exam_type.name,
            'marks_details': marks_details,
            'student_name': f"{student.first_name} {student.last_name}",
            'total_obtained_marks': total_obtained_marks,
            'total_max_marks': total_max_marks,
            'percentage': percentage,
            'rank': rank,
        }
        return render(request, 'exam_result.html', context=context)

    elif standard.result_type == 'grade':
        # Grade calculation logic (already provided)
        marks = ExaminationMarks.objects.filter(
            student_id=student_id,
            exam_type_id=exam_type_id,
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id
        )

        gradings = GradingSystem.objects.filter(
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id
        )

        normalized_max_marks = 100
        grade_data = {}
        total_marks = 0
        total_maximum_marks = 0

        for mark in marks:
            obtained_marks = int(mark.obtained_marks)
            max_marks = mark.max_marks

            if max_marks != 100:
                normalized_obtained_marks = (obtained_marks / max_marks) * normalized_max_marks
            else:
                normalized_obtained_marks = obtained_marks

            assigned_grade = None
            total_marks += obtained_marks
            total_maximum_marks += mark.max_marks

            for grading in gradings:
                if grading.marks_from <= normalized_obtained_marks <= grading.marks_to:
                    assigned_grade = grading.grade
                    break

            if mark.subject.name not in grade_data:
                grade_data[mark.subject.name] = assigned_grade

        normalized_obtained_marks_for_overall_grade = (total_marks / total_maximum_marks) * normalized_max_marks
        overall_grade = None
        for grading in gradings:
            if grading.marks_from <= normalized_obtained_marks_for_overall_grade <= grading.marks_to:
                overall_grade = grading.grade
                break

        context = {
            'exam_type': exam_type.name,
            'student_name': f"{student.first_name} {student.last_name}",
            'grade_data': grade_data,
            'overall_grade': overall_grade
        }
        return render(request, 'exam_result_grade.html', context=context)

    elif standard.result_type == 'cgpa':
        # CGPA grading logic
        marks = ExaminationMarks.objects.filter(
            student_id=student_id,
            exam_type_id=exam_type_id,
            institute_id=institute_id,
            branch_id=branch_id,
            session_id=session_id
        )

        total_obtained_marks = 0
        total_max_marks = 0

        for mark in marks:
            total_obtained_marks += int(mark.obtained_marks)
            total_max_marks += mark.max_marks

        # Calculate CGPA (normalized to a 10-point scale)
        cgpa = (total_obtained_marks / total_max_marks) * 10

        # Manually define CGPA ranges and corresponding grades
        if cgpa >= 9.0:
            overall_grade = 'A+'
        elif 8.0 <= cgpa < 9.0:
            overall_grade = 'A'
        elif 7.0 <= cgpa < 8.0:
            overall_grade = 'B+'
        elif 6.0 <= cgpa < 7.0:
            overall_grade = 'B'
        elif 5.0 <= cgpa < 6.0:
            overall_grade = 'C+'
        elif 4.0 <= cgpa < 5.0:
            overall_grade = 'C'
        else:
            overall_grade = 'F'  # Fail grade if CGPA is below 4.0

        # Prepare the response
        context = {
            'exam_type': exam_type.name,
            'student_name': f"{student.first_name} {student.last_name}",
            'total_obtained_marks': total_obtained_marks,
            'total_max_marks': total_max_marks,
            'cgpa': cgpa,
            'overall_grade': overall_grade
        }
        return render(request, 'exam_result_cgpa.html', context=context)



