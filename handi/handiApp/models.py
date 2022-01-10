from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    userType = models.IntegerField(default=0) #0 = student, 1 = mentor, 2 = manager, 3 = admin
    hearingLevel = models.IntegerField(default=0) #0 = hearing, 1 = hard of hearing, 2 = deaf
    profilePic = models.ImageField(upload_to ='uploads/', default='media/handiApp/blankProfilePic.png')
    signType = models.IntegerField(default=0) #1 = ASL
    #friends or something like that


    def __str__(self):
        return self.user.username

class MentorRequest(models.Model):
    requestor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    requestDate = models.DateField(null=True)
