from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView, mentor_list
from users.forms import LoginForm
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    # path('home/', views.home, name="home"), # home page
    path('about/', views.about, name="about"), # about page
    path('community/', views.contributors, name="community"), # community page
    path('users/', include("users.urls")), # user management
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'), # login view with authentication

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # logout view

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'), # password reset through email needs credential

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'), # reset confirmation view

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'), # reset complete after email verification
    path('mentors-seek/', mentor_list, name='mentors-seek'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'), # changing password by entering old password
#     path('mentors/', MentorView.as_view(), name="mentors"), # mentors view currently dont display anything until it's on development
    re_path(r'^oauth/', include('social_django.urls', namespace='social')), # oauth from google and github needs clientID and client secret key to authenticate needs to get hosted if it has to take url from development
]