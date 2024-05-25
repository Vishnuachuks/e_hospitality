from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-page/', views.admin_dashboard, name='admin_page'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete_patient/<int:patient_id>/', views.delete_patient_management, name='delete_patient_management'),
    path('delete_facility/<int:facility_id>/', views.delete_facility_management, name='delete_facility_management'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('update_patient/<int:patient_id>/',edit_patient, name='update_patient'),
    path('update_facility/<int:facility_id>/',edit_facility, name='update_facility'),
    path('update_appointment/<int:appointment_id>/',edit_appointment, name='update_appointment'),
    path('update_user/<int:user_id>/', edit_user, name='update_user'),




    # Patient
    path('patient-register/', views.register, name='patient_register'),
    path('patient-logout/', views.patient_logout, name='patient_logout'),
    path('patient-page/', views.patientpage_view, name='patient_page'),
    path('patient-form/', views.patient_form_view, name='patient_form'),
    path('patients/update/', views.patient_update, name='patient_update'),
    path('patients/delete/', views.patient_delete, name='patient_delete'),
    path('delete_patient/<int:pk>/',views.patient_delete, name='delete_patient'),
    path('patient-create/', views.patient_create, name='patient_create'),
    path('patient/<int:patient_id>/', views.patient_detail_view, name='patient_detail'),
    path('edit-patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('appointment-form/', views.patient_appointment_create, name='appointment_form'),
    path('appointment-view/', views.patient_appointment_view, name='appointment_view'),
    path('medical-history/', views.medical_history_form_view, name='medical_history'),
    path('bills-payments/', views.billing_form_view, name='bills_payments'),
    path('health-resource/', views.health_resource_form_view, name='health_resource'),
    path('appointment/update/<int:pk>/', views.patient_appointment_update, name='appointment_update'),
    path('appointment/delete/<int:pk>/', views.patient_appointment_delete, name='appointment_delete'),
    path('medical-history/update/<int:pk>/', views.medical_history_update, name='medical_history_update'),
    path('medical-history/delete/<int:pk>/', views.medical_history_delete, name='medical_history_delete'),

    # Doctors
    path('doctor-page/', views.doctorpage_view, name='doctor_page'),
    path('doctor-register/', views.doctor_register, name='doctor_register'),
    path('doctor-login/', views.doctor_login, name='doctor_login'),
    path('logout/', doctor_logout, name='doctor_logout'),
    path('doctor-form/', views.doctor_form_view, name='doctor_form'),
    path('prescriptions/new/', views.create_prescription, name='create_prescription'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('patient-management/', views.patient_management, name='patient_management'),
    path('doctor-appointment-view/', views.doctor_appointment_view, name='doctor_appointments_view'),
    path('e-prescribing/', views.e_prescribing_view, name='e_prescribing'),
    path('submit-prescription/', views.submit_prescription, name='submit_prescription'),

]
