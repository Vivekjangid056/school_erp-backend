from django.urls import path
from .views import *

app_name = 'examination'

urlpatterns = [
    path('exam-time-table-list', exam_time_table_list, name='exam_time_table_list'),
    path('timetable/view/', view_timetable_ajax, name='view_timetable_ajax'),
    path('exam-time-table-create', exam_time_table_create, name='exam_time_table_create'),
    path('timetable/delete/<int:standard>/<str:exam_type>/', exam_time_table_delete, name='exam_time_table_delete'),
    path('exam-type-list', exam_type_list, name='exam_type_list'),
    path('exam-type-create', exam_type_create, name='exam_type_create'),
    path('exam-update/<int:pk>', exam_type_update, name='exam_type_update'),
    path('exam-type-delete/<int:pk>', exam_type_delete, name='exam_type_delete'),
    path('get-exam-types/', get_exam_types, name='get_exam_types'),
    path('examination-marks-create', create_examination_marks, name = 'examination_marks_create'),
    path('examination-marks-list', examination_marks_list, name = 'examination_marks_list'),
    path('load-students', load_students, name = 'load_students'),
    path('get-section_subjects', get_sections_subjects, name = 'get_sections_subjects'),
    path('marks_update/<int:pk>', examination_marks_update, name='examination_marks_update'),
    path('marks-delete/<int:pk>', examination_marks_delete, name='examination_marks_delete'),

    # paths for web links related to the examination
    path('student-exam-timetable/<int:student_id>/<int:institute_id>/<int:branch_id>/<int:session_id>/', 
         student_exam_timetable_view, 
         name='student_exam_timetable'),
    path('student-exam-result/<int:student_id>/<int:institute_id>/<int:branch_id>/<int:session_id>/<int:exam_type_id>/', 
         student_exam_result, 
         name='student_exam_result'),
]
