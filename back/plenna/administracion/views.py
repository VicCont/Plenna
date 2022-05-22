from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def login(request):
    pass

def login_doc_gral(request):
    pass

def insights(request):
    pass

def consulta_insight(request):
    pass

def crea_insight(request):
    pass

def consulta_cuestionario(request):
    pass

def actualiza_cuestionario(request):
    pass

def dar_permiso(request):
    pass

def quitar_permiso(request):
    pass

