
from django.db import models 
from user.models import Ware

class Client(models.Model): 
    full_name = models.CharField(max_length=30) 
    shop_name = models.CharField(max_length=30) 
    telephone_number = models.IntegerField()
    location = models.CharField(max_length=30) 
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)


class Product(models.Model):  
    name = models.CharField(max_length=30) 
    brand = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    in_warehouse = models.CharField(max_length=30)   
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)


class Stats(models.Model): 
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)  
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)  
    total = models.PositiveIntegerField(default=0)
    payed = models.PositiveIntegerField(default=0)
    debt = models.PositiveIntegerField(default=0) 
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)
    


    def debt_count(self): 
        self.sdebt = self.total - self.payed