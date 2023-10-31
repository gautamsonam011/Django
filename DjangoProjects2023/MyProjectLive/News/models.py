from django.db import models
from autoslug import AutoSlugField
# # Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_desc = models.TextField(max_length=500)
    # news_desc = HTMLField(max_length=500)
    news_image = models.FileField(upload_to = 'newimg/',max_length=250,null=True,default=None)
    news_slug = AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    phone_number = models.BigIntegerField()
    desc = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    
