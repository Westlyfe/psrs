from django.urls import path
from hospital.views import create_user,login

urlpatterns = [
    path('create-user/',create_user,name = 'create-user'),
    path('auth/login/',login,name = 'login')

]