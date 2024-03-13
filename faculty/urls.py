from django.urls import path
from . import views

urlpatterns = [
    path('showfac/',views.addfaculty,name='addfaculty'),

]