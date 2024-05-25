from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# User
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

# Patient
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = PatientAppointment
        fields = ['doctor', 'patient', 'appointment_date', 'reason_for_visit', 'notes']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'reason_for_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = '__all__'
        widgets = {
            'diagnosis': forms.Textarea(attrs={'class': 'form-control'}),
            'medications': forms.Textarea(attrs={'class': 'form-control'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control'}),
            'treatment_history': forms.Textarea(attrs={'class': 'form-control'}),
        }

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
        widgets = {
            'billing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'insurance_info': forms.Textarea(attrs={'class': 'form-control'}),
        }

class HealthResourceForm(forms.ModelForm):
    class Meta:
        model = HealthResource
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'resource_type': forms.Select(attrs={'class': 'form-control'}),
        }

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'departments': forms.TextInput(attrs={'class': 'form-control'}),
            'resources': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = PatientAppointment
        fields = ['doctor', 'patient', 'appointment_date', 'reason_for_visit', 'notes']


class FacilityUpdateForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'departments', 'resources']


class UserUpateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# class UserUpdateForm(forms.ModelForm):
#     username = forms.CharField
#     password

#     class Meta:
#         model = User
#         fields = ['username', 'password']


class AppointmentManagementForm(forms.ModelForm):
    class Meta:
        model = PatientAppointment
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'medication': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
