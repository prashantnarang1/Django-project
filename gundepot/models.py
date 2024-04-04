from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Gun(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=200)


class Product(models.Model):

    CAT=((1,'Assault Rifles'),(2,'Designated Marksman Rifles'),(3,'Sniper Rifles'),(4,'Shotguns'),(5,'Light Machine Guns'),(6,'Submachine Guns'),(7,'Pistols'),(8,'Crossbows'),(9,'Melee Weapons'),(10,'Throwables'))

    name=models.CharField(max_length=40,)
    price=models.FloatField()
    pdetails=models.CharField(max_length=400,verbose_name="product details")
    category=models.IntegerField(choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name="available")
    piamge=models.ImageField(upload_to="image")

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)


class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)
    
    
