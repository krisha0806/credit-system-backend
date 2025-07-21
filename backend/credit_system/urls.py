"""credit_system URL Configuration

The `urlpatterns` list routes URLs to views.
For more information, see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', lambda request: HttpResponse("Welcome to the Credit System Homepage!")),
]



