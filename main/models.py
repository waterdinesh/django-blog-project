from dataclasses import fields
from django.db import models
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
       return self.name
    # return f"{self.name} ({self.addblog_set.count()} blog(s))"

class Addblog(models.Model):
    name=models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='addimg/',null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# class Latestpost(models.Model):
#     name=models.CharField(max_length=20)
#     image=models.ImageField(upload_to='addimg/',null=True, blank=True)
#     date=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name


# Create your models here.
