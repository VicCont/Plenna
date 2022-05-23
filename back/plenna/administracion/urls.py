# films/urls.py
from sys import path_hooks
from django.urls import path
from . import views

app_name = 'administracion'
urlpatterns = [
    path('', views.index, name='main'),
    path('doctor/pacientes',views.pacientes_doc),
    path('doctor/pacientes/<int:num>',views.consulta_cuestionario),
    path('doctor/insights',views.insights),
    path('doctor',views.doctor,name='doctor'),
    path('login', views.login,name='login'),
    path('loginA', views.login_doc_gral,name='loginA')
    
]