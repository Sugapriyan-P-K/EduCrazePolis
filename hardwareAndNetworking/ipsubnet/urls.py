from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:number>/', views.index, name="start")
]
