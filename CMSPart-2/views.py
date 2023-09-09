from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Employee():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
def getNEmployee(n):
    list_emp = []
    for i in range(1,n+1):
        emp = Employee()
        emp.name = "Pankaj"+str(i)
        emp.age = 19+i
        emp.address = "New Ashok Nagar"+str(i)
        list_emp.append(emp)
    return list_emp

def view_dtl(request):
    employees = getNEmployee(10)
    d1 = {'employees':employees}
    resp = render(request, "CMS/dtl.html", context=d1)
    return resp