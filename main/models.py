from django.db import models 
from user.models import Ware
class Client(models.Model): 
    full_name = models.CharField(max_length=30) 
    shop_name = models.CharField(max_length=30) 
    telephone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=30) 
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE) 

    def __str__(self):
        return self.full_name
class Product(models.Model):  
    name = models.CharField(max_length=30) 
    brand = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    in_warehouse = models.PositiveIntegerField()   
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name
class Stats(models.Model): 
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)  
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) 
    date = models.DateField()   
    product_amount = models.PositiveIntegerField()
    total = models.PositiveIntegerField(default=0)
    payed = models.PositiveIntegerField(default=0)
    debt = models.PositiveIntegerField(default=0, null=True) 
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE) 

    
    