# films/urls.py
from sys import path_hooks
from django.urls import path
from . import views

app_name = 'administracion'
urlpatterns = [
    path('', views.index, name='main'),
    path('doctor/pacientes',views.pacientes_doc, name='vista_pacientes'),
    path('doctor/pacientes/<int:id_pac>/<str:nom_pac>',views.consulta_cuestionario,name='consulta_custionarios'),
    path('doctor/pacientes/<int:id_pac>/<str:nom_pac>/<int:id_esp>',views.responder_cuestionario,name='responder_cuestionario'),
    path('doctor/insights',views.insights, name='vista_insights'),
    path('doctor/insights/crear/<int:id_pac>/<str:nombre>',views.crea_insight, name='crear_insight'),
    path('doctor/insights/<int:id_pac>/<str:nombre>',views.consulta_insight, name='consulta_insight'),
    path('administrar/permisos/conceder',views.listado_docs_con,name='listado_docs_perms_con'),
    path('administrar/permisos/remover',views.listado_docs_rem,name='listado_docs_perms_rem'),
    path('administrar/permisos/remover/doctor/<int:id_doc>/<str:nom_doc>',views.listado_pac_rem,name='listado_pacs_perms_rem'),
    path('administrar/permisos/conceder/doctor/<int:id_doc>/<str:nom_doc>',views.listado_pac_con,name='listado_pacs_perms_con'),
    path('administrar/permisos/remover/doctor/<int:id_doc>/<str:nom_doc>/paciente/<int:id_pac>/<str:nom_pac>',views.quitar_permiso,name='remover_permiso'),
    path('administrar/permisos/conceder/doctor/<int:id_doc>/<str:nom_doc>/paciente/<int:id_pac>/<str:nom_pac>',views.dar_permiso,name='conceder_permiso'),
    path('administrar',views.administrar,name='vista_Dgral'),
    path('doctor',views.doctor,name='doctor'),
    path('login', views.login,name='login'),
    path('logout',views.logout,name="logout"),
    path('loginA', views.login_doc_gral,name='loginA'),
    path('doctor/visualizaciones',views.visualizaciones,name='visualizaciones')
    
    
]