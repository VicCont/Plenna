from django.contrib import admin

# Register your models here.
from administracion.models import *

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(Pregunta)
admin.site.register(OpcPreg)
