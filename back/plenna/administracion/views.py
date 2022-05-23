from urllib import response
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def login_doc_bd(usu,passw):
    return (usu=='hola' and passw=='bimbo')

def login(request):
    if request.method == 'POST':
        usu=request.POST['usu']
        passw=request.POST['pass']
        id=login_doc_bd(usu,passw)
        if (id is not None and id>0):
            response= render(request,'vista_doc.html')
            response.set_cookie('id_doc', id)
            return response
    else:
        return render(request,"login.html")

def doctor(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            return redirect('/login')
        return render(request,'vista_doc.html')
        
    except:
        return redirect('/login')

def login_doc_gral(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            return redirect('/loginA')
        admin=request.COOKIES.get("is_adim")
        if (admin):
            return render(request,'vista_doc.html')
        return redirect('/loginA')
    except:
        return redirect('/loginA')
def pacientes_doc(request):
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

