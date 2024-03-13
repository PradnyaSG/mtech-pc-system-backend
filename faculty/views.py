from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
#from .forms import ExcelUploadForm
from .models import *

def addfaculty(request):
     #Creating a faculty object
     facobj=faculty(name="ABC",dept="CSE", isguide=1,ischair=2 , iscommem=3,isprojcoo=1,email = "aboc@gmail.com",domain="CV")
     facobj.save()
     return render(request,'home.html',{'facobj':facobj})

     
def evaluations(request):
    mydata = faculty.objects.get(id=1)
    eval=mystudents(rollNoId="M23002CS",guide=mydata)
    eval.save()
    return render(request,'home.html',{'eval':eval})
    

    
