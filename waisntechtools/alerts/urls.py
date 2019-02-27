from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'alerts'
urlpatterns = [
    path('', lambda request: render(request, 'alerts/index.html'), name='index'),
    path('debug', views.DebugView.as_view(), name='debug')
]
