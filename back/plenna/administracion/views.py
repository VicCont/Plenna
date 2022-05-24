from urllib import response
from django.shortcuts import redirect, render
from sympy import re
from administracion.bd_raw import login_adm,login_doc,get_insights,get_pacientes_doc
# Create your views here.
from django.http import HttpResponse


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
        return render(request,'vista_doc.html',{'is_admin':resp})
        
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
        try:
            id=request.COOKIES.get('id_doc')
            if(id is None):
                return render(request,'login.html',{'is_admin':True})
            admin=request.COOKIES.get('is_admin')
            if (admin is None or not admin):
                return render(request,'login.html',{'is_admin':True})
            return render(request,'vista_doc.html',{'is_admin':admin})
        except:
                return render(request,'login.html',{'is_admin':True})

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

def administrar(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=request.COOKIES.get('is_admin')
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'vista_doc.html',{'is_admin':admin})
    except Exception as e:
        return redirect('/login')    

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

def consulta_insight(request,id_pac):
    id=request.COOKIES.get('id_doc')
    if(id is None):
        return redirect('/login')
    datos=get_insights(id_pac)
    contexto={'id_pac':id_pac,'datos':datos}
    return render(request,'consulta_insight.html',contexto)

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

