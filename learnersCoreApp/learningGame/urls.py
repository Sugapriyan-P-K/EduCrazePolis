from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:number>/', views.start, name="start"),
]
