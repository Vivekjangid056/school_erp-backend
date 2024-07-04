from django.urls import path
from .views import *

app_name = 'teacher'


urlpatterns = [
    # category master
    path('category-master-list/',category_master_list, name='category_master_list'),
    path('category-master-create/', AddMasterCategory.as_view(), name='create_category_master'),
    path('category-master-update<int:pk>',updateMasterCategory.as_view(),name="update_category_master"),
    path('category-master-delete<int:pk>',deleteMasterCategory.as_view(),name="delete_category_master"),
    
    # designation master
    path('designation-master-list/',designation_master_list,name='designation_master_list'),
    path('designation-master-create/',CreateDesignationMaster.as_view(),name='add_designation_master'),
    path('designation-master-update<int:pk>',UpdateDesignationMaster.as_view(),name='designation_master_update'),
    path('designation-master-delete<int:pk>',DeleteDesignationMaster.as_view(),name='designation_master_delete'),
    
    # department master
    path('department-master-list/',department_master_list,name='department_master_list'),
    path('department-master-create/', CreateDepartmentMaster.as_view(),name='add_department_master'),
    path('department-master-update<int:pk>',updateDepartmentMaster.as_view(),name='update_department_master'),
    path('department-master-delete<int:pk>',deleteDepartmentMaster.as_view(),name='delete_department_master'),
    
    # attendance type
    path('attendance-type-list/',attendance_type,name='attendance_type_list'),
    path('attendance-type-create/',CreateAttendanceType.as_view(), name='attendance_type_create'),
    path('attendance-type-update<int:pk>',EditAttendanceType.as_view(), name='attendance_type_update'),
    path('attendance-type-delete<int:pk>',DeleteAttendanceType.as_view(), name='attendance_type_delete'),
    
    #holiday list urls
    path('holiday-list/',holiday_list,name='holiday_list'),
    path('holiday-list-create/',CreateHolidayList.as_view(), name='holiday_list_create'),
    path('holiday-list-update<int:pk>',UpdateHolidayList.as_view(),name='holiday_list_update'),
    path('holiday-list-delete<int:pk>',DeleteHolidayList.as_view(),name='holiday_list_delete'),
     
]
