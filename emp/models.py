from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    empid=models.CharField(max_length=100)
    departments=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    working=models.BooleanField(default=True)


    
