from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, mentor_list
from users.forms import LoginForm
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