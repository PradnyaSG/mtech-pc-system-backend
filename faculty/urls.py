from django.urls import path
from . import views

urlpatterns = [
    path('showfac/',views.addfaculty,name='addfaculty'),
<<<<<<< HEAD
         path('evaluations/',views.evaluations,name='evaluations'),
=======
>>>>>>> f3eace6288e8b4decc6f602f7862aff16a8445a1

]