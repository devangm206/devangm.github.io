from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils import timezone
# Create your models here.


class studentgriev(models.Model):
    name = models.CharField(max_length=30,default='',null=False)
    contactnum = models.IntegerField(default='',null=False)
    email = models.EmailField(max_length=50,default='',null=False)
    grievance = models.TextField(default='',null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(null=True)

    def __str__(self):
        return self.name + " "

class contactus(models.Model):
    ctname = models.CharField(max_length=30,default='',null=False)
    ctemail = models.EmailField(max_length=20,default='',null=False)
    ctsubject = models.CharField(max_length=30,default='',null=False)
    ctmessage = models.TextField(default='',null=False)


