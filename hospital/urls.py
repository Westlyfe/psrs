from django.urls import path
from hospital.views import create_user,login,create_inquiries,create_doctor,doctor_availability

urlpatterns = [
    path('create-user/',create_user,name = 'create-user'),
    path('auth/login/',login,name = 'login'),
    path('inquiries/',create_inquiries,name = 'create_inquiries'),
    path('doctor/',create_doctor,name = 'create-doctor'),
    path('doctor/availability',doctor_availability,name = 'doctor-availability'),
]