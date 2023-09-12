from django.urls import path
from .views import *
#Base URL =>> http://127.0.0.1:8000/sms/

urlpatterns = [
    path('course/',get_course_wise_student_details)

]
