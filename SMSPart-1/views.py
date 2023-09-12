from django.shortcuts import render
from django.http import HttpResponse
from SMS.models import *

# Create your views here.

# one to many relationship 

def view_paymentDetails(request):
    if request.method == 'GET':
        resp = render(request,'SMS/index.html')
        return resp
    elif request.method == 'POST':
        sid = int(request.POST.get('txtid',0))
        stu = Student.objects.get(id=sid)
        allp = stu.paymentdetails_set.all()
        d1 = {'payments':allp,'stu':stu}
        resp = render(request,'SMS/index.html', context=d1)
        return resp