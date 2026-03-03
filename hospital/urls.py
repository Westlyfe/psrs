from django.urls import path
from hospital.views import create_user,login,create_inquiries,create_doctor,doctor_availability,create_appointment,get_doctor_schedule,create_schedule,cancel_appointment

urlpatterns = [
    path('create-user/',create_user,name = 'create-user'),
    path('auth/login/',login,name = 'login'),
    path('inquiries/',create_inquiries,name = 'create_inquiries'),
    path('doctor/',create_doctor,name = 'create-doctor'),
    path('doctor/availability',doctor_availability,name = 'doctor-availability'),
    path('appointment',create_appointment,name = 'create-appointment'),
    path('appointment/cancel/<int:id>/',cancel_appointment, name='cancell_appointment'),
    path('schedule/create/',create_schedule, name='create_schedule'),
    path('schedule/<int:id>/',get_doctor_schedule, name='get_doctor_schedule'),
]