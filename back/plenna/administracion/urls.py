# films/urls.py
from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('', views.index, name='main'),
    path('/doctor/insights', views.insights, name ='insights')
]