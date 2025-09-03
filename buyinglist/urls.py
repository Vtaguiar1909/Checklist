from django.urls import path
from . import models
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.login_user,name="login")
]
