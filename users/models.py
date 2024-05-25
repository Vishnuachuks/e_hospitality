from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Patient related models
class Patient(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField()
    email = models.EmailField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    parents_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_number = models.CharField(max_length=15)
    weight = models.FloatField()
    height = models.FloatField()
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    departments = models.CharField(max_length=200)
    resources = models.TextField()

    def __str__(self):
        return self.name

# class AppointmentManagement(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     date_time = models.DateTimeField(default=timezone.now)
#     duration = models.PositiveIntegerField(help_text="Duration in minutes")

#     def __str__(self):
#         return f'{self.patient}  {self.doctor}  {self.date_time}'

class PatientAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason_for_visit = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '', self.doctor

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    billing_date = models.DateField()
    amount = models.FloatField()
    is_paid = models.BooleanField(default=False)
    insurance_info = models.TextField()

class HealthResource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    RESOURCE_TYPE_CHOICES = [
        ('Article', 'Article'),
        ('Video', 'Video'),
        ('Infographic', 'Infographic'),
    ]
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    instructions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f'Prescription for {self.patient} by Dr. {self.doctor.last_name}'

class AppointmentSchedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='schedule')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    details = models.TextField()

    def __str__(self):
        return f'{self.doctor} with {self.patient} on {self.date}'
