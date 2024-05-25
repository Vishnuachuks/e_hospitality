from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import * 
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View





# USER
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save the form data to 'user' object without committing to database yet
            user.set_password(form.cleaned_data['password'])  # Set the user's password
            user.save()  # Save the user object to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage')  # Redirect to your homepage or any other success page
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

# Homepages
def homepage_view(request):
    return render(request, 'homepage.html')

# Patient
def patientpage_view(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient/patient_page.html', context)

def patient_logout(request):
    logout(request)
    return redirect('patient-page')

def patient_create(request):
    patient=Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-page')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_create.html', {'form': form, 'patient' : patient})

def patient_form_view(request):
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-page')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient-page')
    return render(request, 'patient/patient_delete.html', {'patient': patient})

def patient_detail_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    medical_history = MedicalHistory.objects.filter(patient=patient)
    context = {
        'patient': patient,
        'medical_history': medical_history
    }
    return render(request, 'patient/patient_details.html', context)

def patient_appointment_create(request):
    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_form')
    else:
        form = PatientAppointmentForm()
    return render(request, 'patient/patient_appointment_form.html', {'form': form})


def patient_appointment_update(request, pk):
    appointment = get_object_or_404(PatientAppointment, pk=pk)
    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_view')
    else:
        form = PatientAppointmentForm(instance=appointment)
    return render(request, 'patient/appointment_update.html', {'form': form})


def patient_appointment_delete(request, pk):
    appointment = get_object_or_404(PatientAppointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_view')
    return render(request, 'patient/appointment_delete.html', {'appointment': appointment})


def patient_management_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_page')
    return render(request, 'patient/appointment_delete.html', {'patient': patient})


def patient_appointment_view(request):
    appointments = PatientAppointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'patient/appointment_view.html', context)

def medical_history_form_view(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MedicalHistoryForm()
    medical_histories = MedicalHistory.objects.all()
    context = {
        'form': form,
        'medical_histories': medical_histories,
    }
    return render(request, 'patient/medical_history.html', context)

def medical_history_update(request, pk):
    history = get_object_or_404(MedicalHistory, pk=pk)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('medical_history')  # Redirect to the list view after updating
    else:
        form = MedicalHistoryForm(instance=history)
    return render(request, 'patient/medical_history_update.html', {'form': form})

def medical_history_delete(request, pk):
    history = get_object_or_404(MedicalHistory, pk=pk)
    if request.method == 'POST':
        history.delete()
        return redirect('medical_history_list')  # Redirect to the list view after deleting
    return render(request, 'patient/medical_history_delete.html', {'history': history})

def billing_form_view(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BillingForm()
    return render(request, 'patient/billing_payments.html', {'form': form})

def health_resource_form_view(request):
    if request.method == 'POST':
        form = HealthResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = HealthResourceForm()
    return render(request, 'patient/health_resource.html', {'form': form})

# Doctor
def doctorpage_view(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor/doctor_page.html', context)

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_page')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_register.html', {'form': form})


def doctor_login(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('homepage')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_login.html', {'form': form})

def doctor_logout(request):
    logout(request)
    return redirect('admin_page')



def doctor_appointment_view(request):
    appointments = PatientAppointment.objects.filter(doctor=request.user)
    context = {'appointments': appointments}
    return render(request, 'doctor/appointment_list.html', context)

def doctor_form_view(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_form')
    else:
        form = DoctorForm()
    return render(request, 'doctor/doctor_form.html', {'form': form})

def e_prescribing_view(request):
    form = PrescriptionForm()
    patients = Patient.objects.all()
    context = {'form': form, 'patients': patients}
    return render(request, 'doctor/e-prescribing.html', context)

def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_form')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor/prescription_form.html', {'form': form})

def prescription_list(request):
    prescriptions = Prescription.objects.filter(doctor=request.user)
    context = {'prescriptions': prescriptions}
    return render(request, 'doctor/prescription_list.html', context)

def submit_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Prescription submitted successfully')
    else:
        form = PrescriptionForm()
    return render(request, 'doctor/prescription_form.html', {'form': form})

def patient_management(request):
    patients = Patient.objects.all()
    records = MedicalHistory.objects.all()
    appointments = PatientAppointment.objects.all()
    history = MedicalHistory.objects.all()
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            form = MedicalHistoryForm(instance=history)
    context = {
        
        'patients': patients,
        'records': records,
        'appointments': appointments,

    }
    return render(request,'doctor/patient_management.html', context)



def history_update(request, history_id):
    medical_history = get_object_or_404(MedicalHistory, id=history_id)
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST, instance=medical_history)
        if form.is_valid():
            form.save()
            return redirect('patient_management')  # Redirect to the list view after updating
    else:
        form = MedicalHistoryForm(instance=medical_history)
    return render(request, 'doctor/medical_history_update.html', {'form': form})

# Admin
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'admin/patient_update.html', {'form': form })



def delete_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        # Perform additional checks for permissions if needed
        user.delete()
        messages.success(request, f'User {user.username} has been deleted.')
        return redirect('admin_page')  # Redirect to appropriate page after deletion
    else:
        # Handle GET request to show confirmation form (if needed)
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'admin/user_delete.html', {'user': user})
    




def delete_facility_management(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    if request.method == 'POST':
        facility.delete()
        messages.success(request, f'facility {facility.name} {facility.location} has been deleted.')
        return redirect('patient_page')  # Replace with your patient list URL name
    return render(request, 'admin/patient_delete.html', {'facility': facility})

    
def delete_patient_management(request, patient_id):
    patients = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        patients.delete()
        messages.success(request, f'Patient {patients.first_name} {patients.last_name} has been deleted.')
        return redirect('patient_page')  # Replace with your patient list URL name
    return render(request, 'admin/patient_delete.html', {'patients': patients})



def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(PatientAppointment, pk=appointment_id)
    
    if request.method == 'POST':
        # Handle delete logic
        appointment.delete()
        # Redirect or return a response
        
    context = {
        'appointment': appointment,
    }
    return render(request, 'admin/appointment_delete.html', context)



def admin_dashboard(request):
    users = User.objects.all()
    patients = Patient.objects.all()
    facilities = Facility.objects.all()
    appointments = PatientAppointment.objects.all()
    context = {
        'users': users,
        'patients': patients,
        'facilities': facilities,
        'appointments': appointments,
    }
    return render(request, 'admin/admin_page.html', context)



def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(PatientAppointment, id=appointment_id)
    if request.method == 'POST':
        form = PatientAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = PatientAppointmentForm(instance=appointment)
    return render(request, 'admin/appointment_update.html', {'form': form })



def edit_facility(request, facility_id):
    facility = get_object_or_404(Facility, id=facility_id)
    if request.method == 'POST':
        form = FacilityUpdateForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = FacilityUpdateForm(instance=facility)
    return render(request, 'admin/facility_update.html', {'form': form })

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_page')
    else:
        form = UserUpateForm(instance=user)
    return render(request, 'admin/user_update.html', {'form': form })