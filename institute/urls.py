from django.urls import path
from .views import *

app_name = 'institute'  # Namespace for this app

urlpatterns = [
    # path('institute-create/', InstituteRegisterView.as_view(), name='add_institute'),
    # path('institute-list/', InstituteList.as_view(), name='institute_list'),
    # path('institute-update<int:pk>', InstituteUpdateView.as_view(), name="institute_update"),
    # path('institute-delete<int:pk>', InstituteDeleteView.as_view(), name="institute_delete"),

#                              #List Of Masters urls starts

    # List of masters add forms
    path('add-signature', AddSignature.as_view(), name="add_signature"),
    path('add-caste', AddCaste.as_view(), name="add_caste"),
    path('add-category', AddCategory.as_view(), name="add_category"),
    path('add-house', AddHouse.as_view(), name="add_house"),
    path('add-medium', AddMedium.as_view(), name="add_medium"),
    path('add-religion', AddReligion.as_view(), name="add_religion"),
    path('add-standard', AddStandard.as_view(), name="add_standard"),
    path('add-reference', AddReference.as_view(), name="add_reference"),
    path('add-nationality', AddNationality.as_view(), name="add_nationality"),
    path('add-mother-tongue', AddMotherTongue.as_view(), name="add_mother_tongue"),
    path('add-family-relation', AddFamilyRelation.as_view(), name="add_family_relation"),
    path('add-enquiry-type', AddEnquiryType.as_view(), name="add_enquiry_type"),
    path('add-payment-mode', AddPaymentMode.as_view(), name="add_payment_mode"),
    path('add-class-groups', AddClassGroups.as_view(), name="add_class_groups"),
    path('add-standard', AddStandard.as_view(), name="add_standard"),
    path('add-subject', AddSubject.as_view(), name="add_subject"),
    path('add-document', AddDocuments.as_view(), name="add_document"),
    path('add-fee-head', AddFeeHeads.as_view(), name="add_fee_head"),
    path('add-fee-installments', AddFeeInstallments.as_view(), name="add_fee_installments"),
    path('add-leaving-reason', AddLeavingReason.as_view(), name="add_leaving_reason"),
    path('add-sainik-school', AddNameOfSainikSchool.as_view(), name="add_sainik_school"),
    path('add-name-of-bank', AddNameOfBank.as_view(), name="add_name_of_bank"),
    path('add-student-type', AddStudentType.as_view(), name="add_student_type"),
    path('add-child-status', AddChildStatus.as_view(), name="add_child_status"),

    #list of masters listview urls
    path('list-of-signature', ListofSignatures.as_view(), name="list_of_signatures"),
    path('list-of-caste', ListofCaste.as_view(), name="list_of_caste"),
    path('list-of-category', ListofCategory.as_view(), name="list_of_category"),
    path('list-of-house', ListofHouse.as_view(), name="list_of_house"),
    path('list-of-medium', ListofMedium.as_view(), name="list_of_medium"),
    path('list-of-religion', ListofReligion.as_view(), name="list_of_religion"),
    path('list-of-reference', ListofReference.as_view(), name="list_of_reference"),
    path('list-of-nationality', ListofNationality.as_view(), name="list_of_nationality"),
    path('list-of-mother-tongue', ListofMotherToungue.as_view(), name="list_of_mother_tongue"),
    path('list-of-family-relation', ListofFamilyRelation.as_view(), name="list_of_family_relation"),
    path('list-of-enquiry-type', ListofEnquiryType.as_view(), name="list_of_enquiry_type"),
    path('list-of-payment-mode', ListofPaymentMode.as_view(), name="list_of_payment_mode"),
    path('list-of-class-groups', ListofClassGroups.as_view(), name="list_of_class_groups"),
    path('list-of-standard', ListofStandard.as_view(), name="list_of_standard"),
    path('list-of-subjects', ListofSubjects.as_view(), name="list_of_subjects"),
    path('list-of-documents', ListofDocuments.as_view(), name="list_of_documents"),
    path('list-of-fee-heads', ListofFeeHeads.as_view(), name="list_of_fee_heads"),
    path('list-of-fee-installments', ListofFeeInstallments.as_view(), name="list_of_fee_installments"),
    path('list-of-leaving-reason', ListofLeavingReasonTC.as_view(), name="list_of_leaving_reason"),
    path('list-of-sainik-school', ListofNameOfSainikSchool.as_view(), name="list_of_sainik_school"),
    path('list-of-name-of-banks', ListofNameOfTheBank.as_view(), name="list_of_name_of_bank"),
    path('list-of-student-types', ListofStudentType.as_view(), name="list_of_student_type"),
    path('list-of-child-status', ListofChildStatus.as_view(), name="list_of_child_status"),

    # deleting the entries
    path('delete-signature/<int:pk>/', SignatureDeleteView.as_view(), name='signature_delete'),
    path('delete-caste/<int:pk>/', CasteDeleteView.as_view(), name='caste_delete'),
    path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('delete-house/<int:pk>/', HouseDeleteView.as_view(), name='house_delete'),
    path('delete-medium/<int:pk>/', MediumDeleteView.as_view(), name='medium_delete'),
    path('delete-religion/<int:pk>/', RelligionDeleteView.as_view(), name='religion_delete'),
    path('delete-reference/<int:pk>/', ReferenceDeleteView.as_view(), name='reference_delete'),
    path('delete-nationality/<int:pk>/', NationalityDeleteView.as_view(), name='nationality_delete'),
    path('delete-mother-tongue/<int:pk>/', MotherTongueDeleteView.as_view(), name='mother_tongue_delete'),
    path('delete-family-relation/<int:pk>/', FamilyRelationDeleteView.as_view(), name='family_relation_delete'),
    path('delete-enquiry-type/<int:pk>/', EnquiryTypeDeleteView.as_view(), name='enquiry_type_delete'),
    path('delete-payment-mode/<int:pk>/', PaymentModeDeleteView.as_view(), name='payment_mode_delete'),
    path('delete-class-group/<int:pk>/', ClassGroupsDeleteView.as_view(), name='class_groups_delete'),
    path('delete-standard/<int:pk>/', StandardDeleteView.as_view(), name='standard_delete'),
    path('delete-subject/<int:pk>/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('delete-document/<int:pk>/', DocumentDeleteView.as_view(), name='document_delete'),
    path('delete-fee-head/<int:pk>/', FeeHeadDeleteView.as_view(), name='fee_head_delete'),
    path('delete-fee-installment/<int:pk>/', FeeInstallmentDeleteView.as_view(), name='fee_installment_delete'),
    path('delete-leaving-reason/<int:pk>/', LeavingReasonDeleteView.as_view(), name='leaving_reason_delete'),
    path('deletesainik-school/<int:pk>/', SainikSchoolDeleteView.as_view(), name='sainik_school_delete'),
    path('delete-name-of-bank/<int:pk>/', NameOfBankDeleteView.as_view(), name='name_of_bank_delete'),
    path('delete-student-type/<int:pk>/', StudentTypeDeleteView.as_view(), name='student_type_delete'),
    path('delete-child-status/<int:pk>/', ChildStatusDeleteView.as_view(), name='child_status_delete'),

    # Updating the entries
    path('update-signature/<int:pk>', UpdateSignature.as_view(), name="update_signature"),
    path('update-caste/<int:pk>', UpdateCaste.as_view(), name="update_caste"),
    path('update-category/<int:pk>', UpdateCategory.as_view(), name="update_category"),
    path('update-house/<int:pk>', UpdateHouse.as_view(), name="update_house"),
    path('update-medium/<int:pk>', UpdateMedium.as_view(), name="update_medium"),
    path('update-religion/<int:pk>', UpdateReligion.as_view(), name="update_religion"),
    path('update-reference/<int:pk>', UpdateReference.as_view(), name="update_reference"),
    path('update-nationality/<int:pk>', UpdateNationality.as_view(), name="update_nationality"),
    path('update-mother-tongue/<int:pk>', UpdateMotherTongue.as_view(), name="update_mother_tongue"),
    path('update-family-relation/<int:pk>', UpdateFamilyRelation.as_view(), name="update_family_relation"),
    path('updateenquiry-type/<int:pk>', UpdateEnquiryType.as_view(), name="update_enquiry_type"),
    path('update-payment-mode/<int:pk>', UpdatePaymentMode.as_view(), name="update_payment_mode"),
    path('update-class-group/<int:pk>', UpdateClassGroups.as_view(), name="update_class_group"),
    path('update-standard/<int:pk>', UpdateStandard.as_view(), name="update_standard"),
    path('update-subject/<int:pk>', UpdateSubjects.as_view(), name="update_subject"),
    path('update-document/<int:pk>', UpdateDocument.as_view(), name="update_document"),
    path('update-fee-head/<int:pk>', UpdateFeeHeads.as_view(), name="update_fee_head"),
    path('update-fee-installment/<int:pk>', UpdateFeeInstallment.as_view(), name="update_fee_installment"),
    path('update-leaving-reason/<int:pk>', UpdateLeavingReason.as_view(), name="update_leaving_reason"),
    path('update-sainik-school/<int:pk>', UpdateSainikSchool.as_view(), name="update_sainik_school"),
    path('update-name-of-bank/<int:pk>', UpdateNameOfBank.as_view(), name="update_name_of_bank"),
    path('update-student-type/<int:pk>', UpdateStudentType.as_view(), name="update_student_type"),
    path('update-child-status/<int:pk>', UpdateChildStatus.as_view(), name="update_child_status"),
    
    
    # urls for employees {for create user in sysytem setting}
    path('employee-list/', EmployeeList.as_view(), name='list_of_employees'),
    path('add-employee/', create_employee, name='add_employee'),
    # path('employee-update<int:pk>', UpdateEmployee.as_view(), name="employee_update"),
    # path('employee-delete<int:pk>', EmployeeDeleteView.as_view(), name="employee_delete"),

    path('add-role', role_create, name = 'add_role'),
    path('roles-list/', role_list, name='list_of_roles'),
    path('update-role/<int:pk>', role_update, name='update_role'),
    path('delete-role/<int:pk>', RoleDeleteView.as_view(), name='role_delete'),
    path('get_menu_data/', get_menu_data, name='get_menu_data'),
    # path('roles/<int:pk>/permissions/create/', permission_create, name='permission_create'),
    
    # urls for subject for class groups
    path('sub-for-class-groups-list/', listSubForClassGroup.as_view(), name='list_of_sub_for_class_groups'),
    path('add-sub-for-class-groups/', AddSubForClassGroup.as_view(), name='add_of_sub_for_class_groups'),
    path('update-sub-for-class-groups/<int:pk>', UpdateSubForClassGroup.as_view(), name='update_of_sub_for_class_groups'),
    path('delete-sub-for-class-groups/<int:pk>', DeleteSubForClassGroup.as_view(), name='delete_of_sub_for_class_groups'),
    
    # url for section
    path('section-list/', listOfSection.as_view(), name='list_of_section'),
    path('add-section/', AddSection.as_view(), name='add_section'),
    path('update-section/<int:pk>', UpdateSection.as_view(), name='update_section'),
    path('delete-section/<int:pk>', DeleteSection.as_view(), name='delete_section'),
]