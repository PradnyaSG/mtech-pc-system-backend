from django.db import models
<<<<<<< HEAD

# Create your models here.
class faculty(models.Model):
=======
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,default=None)
>>>>>>> f3eace6288e8b4decc6f602f7862aff16a8445a1
    name = models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    #counters for each role
    isguide = models.IntegerField(default=0)#guide
    ischair = models.IntegerField(default=0)#chair person
    iscommem = models.IntegerField(default=0)#committee member
    isprojcoo=models.IntegerField(default=0)#project coordinator
<<<<<<< HEAD
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

    

=======
    email = models.CharField(max_length=30,unique=True)
    domain=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

@receiver(post_save, sender=Faculty)
def my_handler(sender,created,instance, **kwargs):
    if created:
        user = User.objects.filter(email=instance.email)
        if not user:
            user1 = User.objects.create(username=instance.email,email=instance.email)
            user1.set_password(instance.email)
            user1.save()
            new_user = User.objects.get(email=instance.email)
            instance.user = new_user
            instance.save(update_fields=['user'])
>>>>>>> f3eace6288e8b4decc6f602f7862aff16a8445a1
