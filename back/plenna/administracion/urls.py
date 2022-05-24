# films/urls.py
from sys import path_hooks
from django.urls import path
from . import views

app_name = 'administracion'
urlpatterns = [
    path('', views.index, name='main'),
    path('doctor/pacientes',views.pacientes_doc, name='vista_pacientes'),
    path('doctor/pacientes/<int:id_pac>',views.consulta_cuestionario,name='consulta_custionarios'),
    path('doctor/insights',views.insights, name='vista_insights'),
    path('doctor/insights/crear/<int:id_pac>',views.insights, name='crear_insight'),
    path('doctor/insights/<int:id_pac>',views.consulta_insight, name='consulta_insight'),
    path('administrar',views.administrar,name='vista_Dgral'),
    path('doctor',views.doctor,name='doctor'),
    path('login', views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('loginA', views.login_doc_gral,name='loginA')
    
]