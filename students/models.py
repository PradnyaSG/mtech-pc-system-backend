from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    rollNoId = models.CharField(max_length=9,unique=True)
    email = models.CharField(max_length=9,unique=True)

    semester = models.IntegerField()
    program = models.CharField(default="M.tech",max_length=50)
    # = model.boolField()
    isGuideSelected=models.BooleanField(default=False)
    
 #  Guide = models.ForeignKey(Faculty,onS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# class Reports(models.Model):
#     Student =  
