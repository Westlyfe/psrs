from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.TextChoices):
    ADMIN = 'ADMIN','Admin'
    PATIENT = 'PATIENT','Patient'
    DOCTOR = 'DOCTOR','Doctor'

class Users(AbstractUser):
    name = models.CharField(max_length = 20)
    role = models.CharField(max_length = 10,choices = Role.choices,default=Role.PATIENT)
    
    def __str__(self):
        return f"User {self.username} has role ({self.role})"