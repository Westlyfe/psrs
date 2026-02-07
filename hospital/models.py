from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.TextChoices):
    ADMIN = 'ADMIN','Admin'
    PATIENT = 'PATIENT','Patient'
    DOCTOR = 'DOCTOR','Doctor'

class InquiryStatus(models.TextChoices):
    OPEN = 'OPEN','Open'
    CLOSED ='CLOSED','Closed'

class AppointmentStatus(models.TextChoices):
    COMPELETED = 'COMPLETED','Completed'
    CONFIRMED = 'CONFIRMED','Confirmed'
    PENDING = 'PENDING','Pending'
    CANCELLED = 'CANCELLED','Cancelled'

class Users(AbstractUser):
    name = models.CharField(max_length = 20)
    role = models.CharField(max_length = 10,choices = Role.choices,default=Role.PATIENT)
    
    def __str__(self):
        return f"User {self.username} has role ({self.role})"

class Inquries(models.Model):
    patient_name = models.CharField(max_length=50)
    location = models.CharField(max_length = 50)
    inquiries_details = models.TextField(max_length = 1000)
    date = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    status = models.CharField(max_length = 20,choices = InquiryStatus.choices,default = InquiryStatus.OPEN)

    def __str__(self):
        return f"Inquerie for patient {self.patient_name} has ({self.status})"

class Doctor(models.Model):
    name = models.CharField(max_length = 50)
    user_id = models.ForeignKey(Users,on_delete = models.CASCADE)
    speicilization = models.CharField(max_length = 30,blank=False)
    availability = models.JSONField(default=dict, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Docter {self.name} has specialized in {self.speicilization}"


class Appointment(models.Model):
    patient_id = models.ForeignKey(Users,on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices = AppointmentStatus.choices,default = AppointmentStatus.PENDING)
    reason = models.CharField(max_length = 400,null=False)
    date = models.DateTimeField()

    def __str__(self):
        return f"Patient {self.patient_id.username} has apointment with doctor {self.doctor_id.user_id.username}"

class Schedule(models.Model):
    doctor_id = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    time_slot = models.CharField(max_length = 30)
    availability = models.BooleanField(default = True)

    # Remember doctor table provided has no relation with users table so thats the tricky sice user has role Doctor we have to make sure that Doctor can login to the system as Admin and Patient so i introduced the relationship
    # 1. Create the api (/api/v1/inquiries) so that you can post inqueties.
            # sample payload your given and the output
            # Then display the inqury created above on ui

    # 2. Create the Api for the following
        # 1. GET available doctors (/api/v1/doctor/availability)
        # 2. POST create an apointment if the doctor is available (/api/v1/appintment)
        # 3. GET all apointment(ilikuwa na inner join ambayo nimesahau but i was bit tricky had uwe unajua how relation work and how to manipulate it)
        # 4. CANCEL apointment 
        # 5. SHOW doctors schedules (/api/v1/schedules/{doctor_id})

    # 3. Authentication
        # Ensure proper api authentcation

    # 4. Create an Admin Pannel to manage the above staffs means apointment doctors and schedule
        # paper ndo iliisha kama ivo
        # 
    # Note: Hii practical tutafanya kwa hii repo in django framework, so far tumeanza na question number 3 which is Done and we will keep posted  
        
