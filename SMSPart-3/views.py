from django.shortcuts import render
from django.http import HttpResponse
from SMS.models import *

# one to one relationship 

def get_course_wise_student_details(request):
    c=Course.objects.all()
    d1={'courses':c}
    if request.method=='GET':
        c=Course.objects.get(id=1)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp
    elif request.method=='POST':
        course_id=int(request.POST.get('courses',0))
        c=Course.objects.get(id=course_id)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp
