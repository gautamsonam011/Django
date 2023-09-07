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
from django.shortcuts import render
from django.http import HttpResponse


def cal(request):
    a = int(request.GET.get('n1',0))
    b = int(request.GET.get('n2',0))
    # c = request.GET.get('n3','NA')
    c = a+b
    # print("a=",a,"b=",b,"c=",c)
    d1 = {'a':a,'b':b,'c':c}
    resp = render(request,"calculator.html", context=d1)
    return resp
    
# path(urlMapping,functionName)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cal/',cal),
    
]
