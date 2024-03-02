from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contributors/', views.contributors, name="contributors"),
    path('softwares/', views.softwares, name="softwares"),
    path('hardwares/', include("hardwareAndNetworking.urls")),
    path('roadmaps/', views.roadmaps, name="roadmaps")
]