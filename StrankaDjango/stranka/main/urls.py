
from django.urls import path, include
from django.contrib import admin
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('bmw', views.bmw, name='bmw'),
    path('tesla', views.tesla, name='tesla'),
    path('mercedes', views.mercedes, name='mercedes'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)