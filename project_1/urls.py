from django.urls import path
from project_1 import views

urlpatterns = [
    path('', views.project_1, name='project_1'),
]