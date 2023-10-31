# from django.shortcuts import render
# from SMS.models import Service
# # Create your views here.

# def service_view(request):
#     # sData = Service.objects.all()
#     # sData = Service.objects.all().order_by('-service_title') #or('-id')
#     sData = Service.objects.all().order_by('-service_title')[:3]
#     # for a in sData:
#     #     print(a.service_icon)
#     resp = render(request,"Service.html")
#     return resp