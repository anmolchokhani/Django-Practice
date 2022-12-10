from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('homeapp1/', views.homepage),

]