from django.urls import path
from . import views

urlpatterns=[
     path("home/",views.view,name="home"),
    # path("operation/",views.operation,name="operation")
]