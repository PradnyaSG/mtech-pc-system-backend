from django.db import models

# Create your models here.
class faculty(models.Model):
    name = models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    #counters for each role
    isguide = models.IntegerField(default=0)#guide
    ischair = models.IntegerField(default=0)#chair person
    iscommem = models.IntegerField(default=0)#committee member
    isprojcoo=models.IntegerField(default=0)#project coordinator
    email = models.CharField(max_length=9,unique=True)
    domain=models.CharField(max_length=255)

class mystudents(models.Model):
    rollNoId = models.CharField(max_length=9,unique=True)
    projectname=models.CharField(default="",max_length=50)
    eval1=models.IntegerField(default=-1)
    eval2=models.IntegerField(default=-1)
    eval3=models.IntegerField(default=-1)
    eval1comment=models.CharField(default="",max_length=100)
    eval2comment=models.CharField(default="",max_length=100)
    eval3comment=models.CharField(default="",max_length=100)
    report1=models.URLField(max_length = 200,null=True) 
    report2=models.URLField(max_length = 200,null=True) 
    report3=models.URLField(max_length = 200,null=True) 
    report1comment=models.CharField(default="",max_length=100)
    report2comment=models.CharField(default="",max_length=100)
    report3comment=models.CharField(default="",max_length=100)
    report1acceptancestatus=models.BooleanField(default=False)
    report2acceptancestatus=models.BooleanField(default=False)
    report3acceptancestatus=models.BooleanField(default=False)
    guide= models.ForeignKey(faculty, on_delete=models.CASCADE)

    

