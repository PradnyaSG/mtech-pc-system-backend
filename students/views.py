from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
#from .forms import ExcelUploadForm
from .models import Student
#import pandas as pd
def students(request):
    
    return HttpResponse("Hello World!!!")

