from django.db import models

# Create your models here.
#This is class for Parent
class ParentClass (models.Model):
    first_name = models.CharField(max_length= 200)
    gender = [
        ('M' , 'Male') , 
        ('F' , 'Female'),
        ]
    status = [
        ('S' , 'Single') , 
        ('M' , 'Married'),
        ('W' , 'Widow'),
        ]
    createddate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField (max_length= 200 , default= 'Admin')
    updatedate = models.DateTimeField (auto_now_add= True)
    updateby =models.CharField (max_length= 200, default= 'Admin')