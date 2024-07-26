from django.urls import path
from .views import *


app_name = 'fees_module'  # This sets the application namespace


urlpatterns = [
    
    
    # <________________URL FOR FEE STRUCTURE____________________>
    path('add-fee-strucutre', FeeStructureCreateView.as_view(), name="add_fee_structure" ),
    # list
    path('list-fee-strucutre', FeeStructureListView.as_view(), name="list_fee_structure" ),
    # update
    path('update-fee-strucutre/<int:pk>', FeeStructureUpdateView.as_view(), name="update_fee_structure" ),
    path('delete-fee-strucutre/<int:pk>', FeeStructureDeleteView.as_view(), name="delete_fee_structure" ),
    
    # <________________URL FOR PAYMENT SCHEDULE____________________>
    path('add-payment-schedule', PaymentScheduleView.as_view(), name="add_payment_schedule" ),
    # list
    path('list-payment-schedule', PaymentScheduleListView.as_view(), name="list_payment_schedule" ),
    # update
    path('update-payment-schedule/<int:pk>', PaymentScheduleUpdateView.as_view(), name="update_payment_schedule" ),
    path('delete-payment-schedule/<int:pk>', PaymentScheduleDeleteView.as_view(), name="delete_payment_schedule" ),    
    
    path('student-fee-payments/', student_fee_payment_list, name='student_fee_payment_list'),
    path('student-fee-payments-create/',create_student_fee_payment, name='create_student_fee_payment'),
    path('student-fee-payments-update/<int:pk>',update_student_fee_payment, name='update_student_fee_payment'),
    path('student-fee-payments-delete/<int:pk>',delete_student_fee_payment, name='delete_student_fee_payment'),
    
    path('api/student_fee_payment/<int:id>/',StudentFeePaymentDetailView.as_view(), name='student_fee_payment_detail'),
]