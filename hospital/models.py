from django.db import models
from django.contrib.auth.models import AbstractUser,User


# Create your models here.

class Roles(models.TextChoices):
    DOCTER = 'DOCTER','Docters',
    ADMIN = 'ADMIN','Admins',
    PATIENTS = 'PATIENTS','Patients'

class User(AbstractUser):
    role = models.CharField(max_length=20,choices=Roles.choices,default=Roles.PATIENTS)
    
    


class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    specialization = models.CharField(max_length=50,default='Eye specialist')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr {self.user.first_name} - {self.user.last_name}"
    
class Apointment(models.Model):
    STATUS_CHOICE = (
        ('pending','pending'),
        ('cancelled','cancelled'),
        ('Approved','Approved')
    )
    patient = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'patient'})
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='pending')

    def __str__(self):
        return f"{self.patient.first_name} with Dr {self.doctor.user.last_name} on {self.date}"