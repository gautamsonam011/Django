from django.db import models

# Create your models here.


# null->Related with Database 
# blank->Related with Django Validation.
# null=False->(You can not leave this field)
# By default it's value is null=False and blank=False

class Student(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False) 
    age = models.IntegerField()
    mobileno = models.CharField(max_length=15)
    dob = models.DateField(null=True,blank=True)
    pic = models.ImageField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PaymentDetails(models.Model):
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=200,choices=[('cash','cash'),('Dabit Card','Dabit Card'),('PhonePe','PhonePe'),('PayTM','PayTM'),('UPI','UPI')])
    payment_date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    
    
    
    