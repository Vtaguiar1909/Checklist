from django.urls import path
from . import models
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("add_item/",views.add_item,name="add_item"),
    path("update_item/<int:pk>",views.update_item,name="update_item"),
    path("delete_item/<int:pk>",views.delete_item,name="delete_item"),
    ## name equals path
]
