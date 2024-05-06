from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path #, include

import anasayfa.views
import ogrenci.views
import ogretmen.views

# from . import views

urlpatterns = [
path('admin/', admin.site.urls),
# path('', include('anasayfa.urls')),
path('home/', anasayfa.views.xxxen, name='homeen'),
path('anasayfa/', anasayfa.views.xxx, name='home'),
path('', anasayfa.views.xxx, name='home'),
path('ogrenci', ogrenci.views.ogrencianaf, name='ogrencianaf'),
path('students', ogrenci.views.ogrencianaf, name='ogrencianaf'),
path('ogretmen', ogretmen.views.ogretmenanaf, name='ogretmenanaf'),