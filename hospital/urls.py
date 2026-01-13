from django.urls import path
from hospital import views


urlpatterns = [
    path("",views.index,name="index"),
    path("create-user/",views.create_user,name="create-user"),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
]