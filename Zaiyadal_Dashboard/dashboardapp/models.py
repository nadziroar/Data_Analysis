from django.db import models

# Create your models here.
#This is class for Parent
class ParentClass (models.Model):
    name = models.CharField(max_length= 200)
    createddate = models.DateTimeField(auto_now_add=True)
    createdby = models.CharField (max_length= 200 , default= 'Admin')
    updatedate = models.DateTimeField (auto_now_add= True)
    updateby =models.CharField (max_length= 200, default= 'Admin')