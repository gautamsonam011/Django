from django.urls import path
from .views import *
#Base URL =>> http://127.0.0.1:8000/cms/

urlpatterns = [
    path('customer/',view_cms),
]
