
from django.contrib import admin
from django.urls import path,include
import website
import jrs

urlpatterns = [
    path('',include("website.urls")),
    path('jrs-try/',include("jrs.urls"))
]
