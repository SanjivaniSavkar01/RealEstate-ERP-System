from django.db import models

class REUser(models.Model):   #this is table
      fullname=models.CharField(max_length=100)
      mobileno=models.CharField(max_length=10)
      username=models.CharField(max_length=100)
      password=models.CharField(max_length=100)

def __str__ (self):
      return self.fullname

# Create your models here.
