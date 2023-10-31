from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('marquee/',marquee_view),
    path('newabout/<newsid>',newsDetails),
    path('filter/',filter_view),
    path('pagi/',paginator_view),
    path('form/',form_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)