from django.db import models
from django.contrib.auth.models import User 

class Ware(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=30)
    telephone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=30) 
    
