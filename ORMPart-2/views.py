from django.shortcuts import render
from django.http import HttpResponse
from CMS.models import Customer
# Create your views here.

def view_cms(request):
    if request.method == 'GET':
        resp = render(request, 'CMS/cms.html')
        return resp
    elif request.method == 'POST':
        if 'btnadd' in request.POST:
            cus = Customer()
            cus.name = request.POST.get('txtname','NA')
            cus.age = request.POST.get('txtage','NA')
            cus.mobileno = request.POST.get('txtno','NA')
            cus.address = request.POST.get('txtaddress','NA')
            cus.save()
            resp = HttpResponse("<h1>Customer Add Successfully in Table With ID:"+str(cus.id)+"!</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            cid = int(request.POST.get("txtid",0))
            cus = Customer.objects.get(id = cid)
            d1 = {'cus':cus}
            resp = render(request,"CMS/cms.html",context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            cus = Customer()
            cus.id = int(request.POST.get('txtid',0))
            if Customer.objects.get(id = cus.id):
                cus.name = request.POST.get('txtname','NA')
                cus.age = request.POST.get('txtage','NA')
                cus.mobileno = request.POST.get('txtno','NA')
                cus.address = request.POST.get('txtaddress','NA')
                cus.save()
                resp = HttpResponse("<h1>Customer Update Successfully in Table With ID:"+str(cus.id)+"!</h1>")
                return resp
        elif 'btndelete' in request.POST:
            cus_id = int(request.POST.get('txtid',0))
            Customer.objects.filter(id = cus_id).delete()
            resp = HttpResponse("<h1>Customer Delete Successfully in Table With ID:"+str(cus_id)+"!</h1>")
            return resp 
        elif 'btnshow' in request.POST:
            all_cus = Customer.objects.all()
            d1 = {'customers':all_cus}
            resp = render(request,"CMS/cms.html", context=d1)
            return resp       