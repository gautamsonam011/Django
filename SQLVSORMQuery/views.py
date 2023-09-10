from django.shortcuts import render
from django.http import HttpResponse
from CMS.models import *
# Create your views here.

def views_ems(request):
    if request.method == 'GET':
        resp = render(request,"CMS/ems.html")
        return resp
    elif request.method == 'POST':
        if 'btnadd' in request.POST:
            emp = Employee()
            emp.name = request.POST.get('txtname','NA')
            emp.age = request.POST.get('txtage','NA')
            emp.address = request.POST.get('txtaddress','NA')
            emp.salary = request.POST.get('txtsalary','NA')
            emp.post = request.POST.get('txtpst','NA')
            emp.save()
            resp = HttpResponse("<h1>Employee Add Successfully in Table With ID:"+str(emp.id)+"!</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            cid = int(request.POST.get("txtid",0))
            emp = Employee.objects.get(id = cid)
            d1 = {'emp':emp}
            resp = render(request,"CMS/ems.html",context=d1)
            return resp
        elif 'btnupdate' in request.POST:
            emp = Employee()
            emp.id = int(request.POST.get('txtid',0))
            if Employee.objects.get(id = emp.id):
                emp.name = request.POST.get('txtname','NA')
                emp.age = request.POST.get('txtage','NA')
                emp.address = request.POST.get('txtaddress','NA')
                emp.salary = request.POST.get('txtsalary','NA')
                emp.post = request.POST.get('txtpst','NA')
                emp.save()
                resp = HttpResponse("<h1>Employee Update Successfully in Table With ID:"+str(emp.id)+"!</h1>")
                return resp
        elif 'btndelete' in request.POST:
            emp_id = int(request.POST.get('txtid',0))
            Employee.objects.filter(id = emp_id).delete()
            resp = HttpResponse("<h1>Employee Delete Successfully in Table With ID:"+str(emp_id)+"!</h1>")
            return resp 
        elif 'btnshow' in request.POST:
            all_emp = Employee.objects.all()
            d1 = {'employees':all_emp}
            resp = render(request,"CMS/ems.html", context=d1)
            return resp    