from django.db import models

# Create your models here.

class Customer(models.Model):
    # cid = models.IntegerField() No need to take id field because id automatically created by Django 
    name = models.CharField(max_length= 15)
    age = models.IntegerField()
    mobileno = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name