from django.contrib import admin
from SMS.models import *
# Register your models here.
# admin.site.register(Student)
# admin.site.register(PaymentDetails) 
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','mobileno']
    
@admin.register(PaymentDetails)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['amount','payment_mode']
        