from django.urls import path

from alerts import views

app_name = 'alerts'
urlpatterns = [
    path('', views.index, name='index'),
    path('debug', views.debug, name='debug'),
]
