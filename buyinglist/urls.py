from django.urls import path,include
from . import models
from . import views
urlpatterns = [
    path("",views.home,name="home")
]
