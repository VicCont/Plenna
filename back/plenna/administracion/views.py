from urllib import response
from django.shortcuts import redirect, render
from sympy import re
from administracion.bd_raw import login_adm,login_doc,get_insights,get_pacientes_doc
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
        id=login_doc(usu,passw)
        if (id is not None and id>0):
            response=redirect('/doctor')
            response.set_cookie('id_doc', id)
            response.set_cookie('is_admin', False)
            return response
        request.method='GET'
        return redirect('/login')
    else:
        try:
            id=request.COOKIES.get('id_doc')
            if(id is None):
                return render(request,'login.html')
            return redirect('/doctor')
        except:
            return redirect('/login')

def doctor(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/login')
        return render(request,'vista_doc.html',{'admin':request.COOKIES.get('is_admin')})
        
    except Exception as e:
        pass
        ##return redirect('/login')

def login_doc_gral(request):
    if request.method == 'POST':
        usu=request.POST['usu']
        passw=request.POST['pass']
        id=login_adm(usu,passw)
        if (id is not None and id>0):
            response= render(request,'vista_doc.html')
            response.set_cookie('id_doc', id)
            response.set_cookie('is_admin',True)
            return response
    else:
        try:
            id=request.COOKIES.get('id_doc')
            if(id is None):
                return render(request,'login.html')
            return redirect('/doctor')
        except:
                return render(request,'login.html')

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

def prueba(request):
    pass

def pacientes_doc(request):
    pass

def logout(request):
    response=redirect("/")
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response

def insights(request):
    id=request.COOKIES.get('id_doc')
    if(id is None):
        return redirect('/login')
    datos={'pacientes':get_pacientes_doc(id)}
    return render(request, 'insights.html',datos)

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

