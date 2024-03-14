from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
#from .forms import ExcelUploadForm
from .models import Student

#def login(request):
#    return

def students(request):

    return HttpResponse("Hello World!!!")

# views.py
from django.http import JsonResponse
from .models import Student

def get_student_project_info(request):
    # Retrieve the student instance based on the user (assuming user authentication is already handled)
    student = Student.objects.get(email=request.user.email)

    # Check if isGuideSelected is True
    if student.isGuideSelected:
        # If project_name is not empty, send project details
        if student.project_name:
            project_details = {
                'project_name': student.project_name,
                'semester': student.semester,
                'program': student.program,
                # Add more project details if needed
            }
            return JsonResponse(project_details)
        else:
            # If project_name is empty, send response to show a form in the frontend
            return JsonResponse({'message': 'Please fill in the project name'}, status=400)
    else:
        # If isGuideSelected is False, send a response to prompt the frontend to select a guide
        return JsonResponse({'message': 'Please select a guide'}, status=400)
