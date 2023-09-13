from django.shortcuts import render
from django.http import HttpResponse
from SMS.models import *
from SMS.forms import *
# Create your views here.

def view_student(request):
    if request.method == 'GET':
        frm_unbound = StudentForm()
        d1 = {'forms': frm_unbound}
        resp = render(request, 'SMS/stufrm.html', context= d1)
        return resp
    elif request.method == 'POST':
        frm_bound = StudentForm(request.Post)
        if frm_bound.is_valid():    # server side validation
            frm_bound.save()
            return HttpResponse("<h1>Student Added Successfully!!</h1>")
        else:
            d1 = {'forms':frm_bound}
            resp = render(request,'SMS/stufrm.html',context=d1)
            return resp
        
def view_paymentdetails(request):
    if request.method == 'GET':
        frm_unbound = PaymentDetailsForm()
        d1 = {'payment':frm_unbound}
        resp = render(request,'SMS/paymentfrm.html',context=d1)
        return resp
    elif request.method == 'POST':
        frm_bound = PaymentDetailsForm(request.Post)
        if frm_bound.is_valid():    # server side validation
            frm_bound.save()
            return HttpResponse("<h1>Payment Added Successfully!!</h1>")
        else:
            d1 = {'payment':frm_bound}
            resp = render(request,'SMS/paymentfrm.html',context=d1)
            return resp
        
        
