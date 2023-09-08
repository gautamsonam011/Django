# GET -- Completed -->> url-rewriting.
# ------------------------------------------------------
# POST
# -------------
# Forbidden (403)
# CSRF verification failed. Request aborted.
# --------------------------------------------------------
# >> To solve this error we use CSRF token.
# >> csrf stands for Cross site request forgery.
# >> while making post request it provide security to our data.
# >> it ensure that no other user can post your data from different sites.

# 	{% csrf_token %}
# ---------------------------------------------------------------------
# Bootstrap :- html,css,js
# -------------------------------------------------------------
# How to post request from different buttons:-
# -----------------------------------------------------------



# 1!=2 -> true
# 1!=1 -> false




from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def get_Numeric_Number(request):
    list_button = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','t0']
    for i in list_button:
        return i[3]
    return '-1'           
def btn_cal(request):
    if request.method == "GET":
        resp = render(request,"calculator.html")
        return resp
    elif request.method == "POST":
        msg = request.POST.get('res',0)
        check_no = get_Numeric_Number(request)
        if (check_no != -1):
            msg =msg+check_no
            d1 = {'msg':msg}
            resp = render(request,'calbtn.html',context=d1)
            return resp
        
     
# path(urlMapping,functionName)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calbtn/',btn_cal),
    
]