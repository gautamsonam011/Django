from django.contrib import admin
from News.models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title','news_desc')
    
admin.site.register(News,NewsAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number','desc','create_date')
admin.site.register(Enquiry,EnquiryAdmin)