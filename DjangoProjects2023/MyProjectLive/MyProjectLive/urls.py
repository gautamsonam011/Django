"""MyProjectLive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('about/',about_us),
    
    # Creating a Dynamic URL in django
    path('course/<int:courseid>',course_details),   
    path('course-name/<str:course>',course_name),
    path('slug/<slug:course>',course_slug),
    # Teplates
    path('index/',index_view),
    # passing data from a view to a template URL
    path('template/',template_view,name="index"),
    # for loop
    path('code/',ForLoop_views,name="code"),
    path('stat/',static_view,name="home"),
    path('ind/',view_index2),
    path("userform/",userForm),
    path('cal/',view_calculator),
    path('even/',evenOdd),
    path('marksheet/',views_marksheet),
    # path('sms/',include('SMS.urls')),
    path('news/',include('News.urls'))
    ]   
