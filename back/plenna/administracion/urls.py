# films/urls.py
from sys import path_hooks
from django.urls import path
from . import views

app_name = 'administracion'
urlpatterns = [
    path('', views.index, name='main'),
    path('doctor/pacientes',views.pacientes_doc, name='vista_pacientes'),
    path('doctor/pacientes/<int:num>',views.consulta_cuestionario,name='consulta_insight'),
    path('doctor/insights',views.insights, name='vista_insights'),
    path('doctor/insights/<int:num>',views.consulta_insight),
    path('administrar',views.doctor,name='vista_Dgral'),
    path('doctor',views.doctor,name='doctor'),
    path('login', views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('loginA', views.login_doc_gral,name='loginA')
    
]