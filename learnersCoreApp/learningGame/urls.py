from django.urls import path
from . import views

# app_name="start"
urlpatterns = [
    path('page/<int:number>/', views.start, name="start"),
]