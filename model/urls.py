from django.contrib import admin
from django.urls import path,include
from model.views import *

urlpatterns = [
    path("",view=welcome)
]
