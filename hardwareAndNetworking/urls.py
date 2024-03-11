from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hardwares, name="hardwares"),
    path('ipsubnet/', include("hardwareAndNetworking.ipsubnet.urls"))
]
