from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    RollNoId = models.CharField(max_length=9,unique=True)
    Semester = models.IntegerField()
    program = models.CharField(default="M.tech")
    
   # guide = models.ForeignKey(Faculty,on)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


