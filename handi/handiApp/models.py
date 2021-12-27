from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100, default="")
    lastName = models.CharField(max_length=100, default="")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    userType = models.IntegerField(default=1) #1 = student, 2 = mentor, 3 = manager, 4 = admin
    hearingLevel = models.IntegerField(default=1) #1 = hearing, 2 = hard of hearing, 3 = deaf
    profilePic = models.ImageField(upload_to ='uploads/', null=True)
    signType = models.IntegerField(default=1) #1 = ASL
    #friends or something like that


    def __str__(self):
        return self.user.username
