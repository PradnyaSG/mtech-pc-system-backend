from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.get_student_project_info,name='students')
]