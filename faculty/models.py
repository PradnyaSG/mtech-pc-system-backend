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


