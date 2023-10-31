from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForms
from django.core.mail import send_mail,EmailMultiAlternatives


def home(request):
    return HttpResponse("Welcome To Home Page!!")
def about_us(request):
    return HttpResponse("Welcome To Here!!")

# Creating a Dynamic URL in django
# int 
def course_details(request,courseid):
    return HttpResponse(courseid)
#str
def course_name(request,course):
    return HttpResponse(course)
#slug
def course_slug(request,course):
    return HttpResponse(course)

# Templates index page

def index_view(request):
    return render(request,"index.html")

# passing data from a django view to a template

def template_view(request):
    data = {
        'title':'This is a details!',
        'name':'This is a index page'
    }
    resp = render(request,'index.html',data)
    return resp

# for loop
def ForLoop_views(request):
    data = {
        'list':['Python','PHP','JAVA','HTML','CSS'],
        'number':[23,14,16,9,64],
        'student_details':[
            {'name':'Pradeep','phone':9895785},
            {'name':'Testing','phone':3865874}]
    }
    resp = render(request,'code.html',data)
    return resp
# static 
def static_view(request):
    resp = render(request,"home.html")
    return resp

def view_index2(request):
    resp = render(request,"index2.html")
    return resp 
# GET----------------------> 
# def userForm(request):
#     final = 0
#     try:
#         # n1 = int(request.GET['num1'])
#         # n2 = int(request.GET['num2'])
#         n1 = int(request.GET.get('num1'))
#         n2 = int(request.GET.get('num2'))
#         print(n1+n2)
#         final = n1+n2
#         d1 = {'op':final}
#     except:
#         pass
#     resp = render(request,"form.html",context=d1)
#     return resp 

# POST:---------------->

# def userForm(request):
#     final = 0
#     data = {}
#     try:
#         if request.method == "POST":
#             n1 = int(request.POST.get('num1'))
#             n2 = int(request.POST.get('num2'))
#             # print(n1+n2)
#             final = n1+n2
#             data={
#                 'n1':n1,
#                 'n2':n2,
#                 'op':final
#             }
#             # url = "/code/?op={}".format(final)
#             # return HttpResponseRedirect('/code/')
#             # return HttpResponseRedirect(url)
#             # return redirect(url)
#     except:
#         pass
#     resp = render(request,"form.html",data)
#     return resp 

# Form 
def userForm(request):
    final = 0
    fn = userForms()
    data = {'form':fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            # print(n1+n2)
            final = n1+n2
            data={
                'form':fn,
                # 'n1':n1,
                # 'n2':n2,
                'op':final
            }
           
    except:
        pass
    resp = render(request,"form.html",data)
    return resp 

def view_calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr == "/":
                c = n1/n2
            else:
                return "Select Valid Operator"
    except:
        c = "Invalid Opr----"
    resp = render(request,"calculator.html",{'c':c})
    return resp

# Check Even odd number 

def evenOdd(request):
    c = ''
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request, "evenOdd.html",{'error':True})
        n = eval(request.POST.get('num1'))
        if n%2 == 0:
            c = "Even Number{}".format(n)
        else:
            c = "Odd Number{}".format(n)
            
    resp = render(request,"evenOdd.html",{'c':c})
    return resp

def views_marksheet(request):
    
    if request.method == "POST":
        s1 = eval(request.POST.get("subject1"))
        s2 = eval(request.POST.get("subject2"))
        s3 = eval(request.POST.get("subject3"))
        s4 = eval(request.POST.get("subject4"))
        s5 = eval(request.POST.get("subject5"))
        t = (s1+s2+s3+s4+s5)
        p = (t*100)/500
        # p = round((t*100)/500,0)
        
        if p >= 60:
            d = "First Div"
        elif p >= 48:
            d = "Second Div"
        elif p >= 35:
            d = "Third Div"
        else:
            d = "Failed"
        data = {
            'total':t,
            'per':p,
            'div':d
        }
        return render(request,"marksheet.html",data)
    
    resp = render(request,"marksheet.html")
    return resp

def sendEmail(request):
#     send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )

    subject = "Testing mail"
    form_email = "mailgfh011@gmail.com"
    msg = '<p>Welcome to you<b>You</b></p>'
    to = 'hjk67@gmail.com'
    msg = EmailMultiAlternatives(subject,msg,form_email,[to])
    msg = content_subtype = 'html'
    msg.send()
    
