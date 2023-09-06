"""CreateURL URL Configuration

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
from django.urls import path
from django.http import HttpResponse

def sum(request,a,b):
    res = HttpResponse("<h1>Hello Welcome To Sum</h1>"+str(a+b))
    return res

def sub(request):
    res = HttpResponse("<h1>Hello I am Calling Sub</h1>")
    return res

def Hey(hfdj):
    resp = HttpResponse("<h1>Hello! How are You?</h1>")
    return resp
# path(urlMapping,functionName)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/<int:a>/<int:b>/',sum), #http://127.0.0.1:8000/sum/
    path('sub/',sub),
    path('hey/',Hey),
]
