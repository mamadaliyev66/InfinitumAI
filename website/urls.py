
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('company/', views.company, name='company'),
    path('solutions/', views.solutions, name='solutions'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('efds/', views.efds, name='efds'),
    path('pd/', views.plant_disease, name='plant_disease'),
    path('attendance/', views.attendance, name='atendance'),
    path('jrs/', views.jrs, name='jrs')

]
