from django.shortcuts import render
from News.models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.

def marquee_view(request):
    newsData = News.objects.all().order_by("-news_title")
    
    data = {
        # 'servicesData':servicesData,
        'newsData':newsData
    }
    resp = render(request,"News/marquee.html",data)
    return resp
 
def newsDetails(request,newsid):
    newsdetails = News.objects.get(id=newsid)
    data = {
        'newsdetails':newsdetails
    }
    resp = render(request,"News/newsDetails.html",data)
    return resp

def filter_view(request):
    s = News.objects.all()
    if request.method == "GET":
        st = request.GET.get('news_title')
        if st != None:
            
            # _icontains
            
            s = News.objects.filter(news_title_icontains=st)
            
    data = {
        's':s,
        'st':st
    }
    resp = render(request,"News/newsDetails.html",data)
    return resp

def paginator_view(request):
    d = News.objects.all()
    paginator = Paginator(d,2)
    page_number = request.GET.get('page')
    page_final = paginator.get_page(page_number)
    
    data = {
        'page':page_final
    }
    resp = render(request,"News/paginator.html",data)
    return resp

def form_view(request):
    n=''
    if request.method == "POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone_no = request.POST.get('pno')
        message = request.POST.get('msg')
        
        en = Enquiry(name=name,email=email,phone_number=phone_no,desc=message)
        en.save()
        n = "Data Send Successfully!"
    
    data = {
        'n':n
    }
        
    resp = render(request,"News/formData.html",data)
    return resp