from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    salary = models.IntegerField()
    post = models.CharField(max_length=50)
    def __str__(self):
        return self.name  #return type class of model is object and case sensitive