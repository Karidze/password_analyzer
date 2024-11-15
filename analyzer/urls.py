from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: render(request, 'analyzer/password.html'), name='password'),
]
