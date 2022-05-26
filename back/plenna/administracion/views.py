from urllib import response
from xmlrpc.client import boolean
from django.shortcuts import redirect, render
from sympy import re
from administracion.bd_raw import *
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


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
        resp=request.COOKIES.get('is_admin')            
        return render(request,'vista_doc.html',{'is_admin':bool(resp)})
        
    except Exception as e:
        return redirect('/login')

def login_doc_gral(request):
    if request.method == 'POST':
        usu=request.POST['usu']
        passw=request.POST['pass']
        id=login_adm(usu,passw)
        if (id is not None and id>0):
            response=redirect('/administrar')
            response.set_cookie('id_doc', id)
            response.set_cookie('is_admin',True)
            return response
        else:
            messages.add_message(request, messages.INFO, 'Inicio de sesión invalido')
            return render(request,'login.html',{'is_admin':True})
    else:
        try:
            id=request.COOKIES.get('id_doc')
            if(id is None):
                return render(request,'login.html',{'is_admin':True})
            admin=request.COOKIES.get('is_admin')
            if (admin is None or not admin):
                return render(request,'login.html',{'is_admin':True})
            return render(request,'vista_doc.html',{'is_admin':bool(admin)})
        except:
                return render(request,'login.html',{'is_admin':True})


def administrar(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=request.COOKIES.get('is_admin')
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'vista_doc.html',{'is_admin':bool(admin)})
    except Exception as e:
        return redirect('/login')    

def prueba(request):
    pass

def pacientes_doc(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/login')
        datos={'pacientes':get_pacientes_doc(id),'is_admin':bool(request.COOKIES.get('is_admin')),'tipo':0}
        return render(request, 'pacientes_doctor.html',datos)
    except Exception as e:
        return redirect('/login')    

def logout(request):
    response=redirect("/")
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response

def insights(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/login')
        datos={'pacientes':get_pacientes_doc(id),'is_admin':bool(request.COOKIES.get('is_admin')),'tipo':1}
        return render(request, 'pacientes_doctor.html',datos)
    except Exception as e:
        return redirect('/login')    

def consulta_insight(request,id_pac,nombre):
    id=request.COOKIES.get('id_doc')
    if(id is None):
        return redirect('/login')
    datos=get_insights(id_pac)
    contexto={'id_pac':id_pac,'datos':datos,'is_admin':bool(request.COOKIES.get('is_admin')),'nombre':nombre}
    return render(request,'consulta_insight.html',contexto)

def crea_insight(request, id_pac,nombre):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/login')
        elif (not is_authorized(id,id_pac)):
            return redirect('/doctor/insights')
        if (request.method=='POST'):
            insight=request.POST['insight']
            resp=insert_insight(id,id_pac,insight)
            if resp:
                messages.add_message(request, messages.INFO, 'Insight insertado con exito')
                return redirect('administracion:consulta_insight',id_pac=id_pac,nombre=nombre)
            else:
                return render(request,'creacion_insight.html',{'nombre':nombre,'id_pac':id_pac,'is_admin':bool(request.COOKIES.get('is_adming'))})
        else:
            return render(request,'creacion_insight.html',{'nombre':nombre,'id_pac':id_pac,'is_admin':bool(request.COOKIES.get('is_adming'))})
    except Exception as e:
        return redirect('/login')   

def consulta_cuestionario(request):
    pass

def actualiza_cuestionario(request):
    pass

def dar_permiso(request):
    pass

def quitar_permiso(request):
    pass

