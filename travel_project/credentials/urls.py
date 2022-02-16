from django.urls import path
from . import views

urlpatterns=[
     path("",views.register,name="reg"),
     path("login",views.login,name="login"),
     path("logout", views.login, name="logout")

     # path("operation/",views.operation,name="operation")
]