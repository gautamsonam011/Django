from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_cms(request):
    resp = HttpResponse("<h1>Welcome To CMS</h1>")
    return resp
def view_index(request):
    resp = render(request, "CMS/index.html")
    return resp
def view_about(request):
    resp = render(request, "CMS/about.html")
    return resp
# Loop 
def Number(n):
    nl = []
    for i in range(1,n+1):
        nl.append(i)
    return nl
def Num(n1):
    n_list = []
    for i in range(n1,0,-1):
        n_list.append(i)
    return n_list

def view_dtl(request):
    res = Number(10)
    result = Num(20)
    d1 = {'x':500, 'a':400,'b':800,'c':200,'res':res,'result':result}
    resp = render(request, "CMS/dtl.html", context=d1)
    return resp