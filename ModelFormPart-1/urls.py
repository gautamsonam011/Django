from django.urls import path
from .views import *
#Base URL =>> http://127.0.0.1:8000/sms/

urlpatterns = [
    path('stufrm/',view_student),
    path('paydetails/',view_paymentdetails),

]
