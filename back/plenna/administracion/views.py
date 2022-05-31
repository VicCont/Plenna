from urllib import response
from xmlrpc.client import boolean
from django.shortcuts import redirect, render
from sympy import re, true
from administracion.bd_raw import *
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from administracion.imprime_html import formatear

def bool_from_String(cadena):
    if cadena=='True':
        return True
    else:
        return False

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
        resp=bool_from_String(request.COOKIES.get('is_admin'))         
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
            admin=bool_from_String(request.COOKIES.get('is_admin'))
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
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'vista_dra_gral.html',{'is_admin':bool(admin)})
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
        datos={'pacientes':get_pacientes_doc(id),'is_admin':bool_from_String(request.COOKIES.get('is_admin')),'tipo':0}
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
        datos={'pacientes':get_pacientes_doc(id),'is_admin':bool_from_String(request.COOKIES.get('is_admin')),'tipo':1}
        return render(request, 'pacientes_doctor.html',datos)
    except Exception as e:
        return redirect('/login')    

def consulta_insight(request,id_pac,nombre):
    id=request.COOKIES.get('id_doc')
    if(id is None):
        return redirect('/login')
    datos=get_insights(id_pac)
    contexto={'id_pac':id_pac,'datos':datos,'is_admin':bool_from_String(request.COOKIES.get('is_admin')),'nombre':nombre}
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

def consulta_cuestionario(request,id_pac,nom_pac):
    id=request.COOKIES.get('id_doc')
    if(id is None):
        return redirect('/login')
    if (not is_authorized(id,id_pac)):
        return redirect("administracion:vista_pacientes")
    pregs=obtener_datos(id_pac)
    perms=get_permisos(id,id_pac)
    perms=[x[0] for x in perms]
    imprimible=formatear(pregs,perms,id_pac,nom_pac)
    contexto={'id_pac':id_pac,'cuestionario':imprimible,'is_admin':bool_from_String(request.COOKIES.get('is_admin')),'nombre':nom_pac}
    return render(request,'cuestionario.html',contexto)

def responder_cuestionario(request,id_pac,nom_pac,id_esp):
    pass

def listado_docs_con(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'pacientes_doctor.html',{'is_admin':bool(admin),'pacientes':get_docs(),'tipo':4,'action':0})
    except Exception as e:
        return redirect('/login')      

def listado_docs_rem(request):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'pacientes_doctor.html',{'is_admin':bool(admin),'pacientes':get_docs(),'tipo':4,'action':1})
    except Exception as e:
        return redirect('/login')    

def listado_pac_rem(request,id_doc,nom_doc):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        contexto={'is_admin':bool(admin),'nom_doc':nom_doc,'id_doc':id_doc,'pacientes':get_pacientes_doc(id_doc),'tipo':int(2),'action':1}
        return render(request,'pacientes_doctor.html',contexto)
    except Exception as e:
        return redirect('/login')    

def listado_pac_con(request,id_doc,nom_doc):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        return render(request,'pacientes_doctor.html',{'is_admin':bool(admin),'nom_doc':nom_doc,'id_doc':id_doc,'pacientes':get_pacientes(),'tipo':3,'action':1})
    except Exception as e:
        return redirect('/login')    

def dar_permiso(request,id_doc,nom_doc,id_pac,nom_pac):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            return redirect('/loginA')
        if request.method=='GET':
            return render(request,'permisos.html',{'is_admin':bool(admin),'action':0,'permisos':get_permisos_faltantes(id_doc,id_pac),'nom_doc':nom_doc,'id_doc':id_doc,'nom_pac':nom_pac,'id_pac':id_pac})
        else:
            seleccionados=request.POST.getlist('permiso')
            insert_permisos(id_doc,id_pac,seleccionados)
            messages.add_message(request, messages.INFO, 'Se han agregado con exito los permisos selccionados')
            return redirect('administracion:conceder_permiso',id_doc=id_doc,nom_pac=nom_pac,nom_doc=nom_doc,id_pac=id_pac)
    except Exception as e:
        return redirect('/login')    


def quitar_permiso(request,id_doc,nom_doc,id_pac,nom_pac):
    try:
        id=request.COOKIES.get('id_doc')
        if(id is None):
            request.method='GET'
            return redirect('/loginA')
        admin=bool_from_String(request.COOKIES.get('is_admin'))
        if (admin is None or not admin):
            request.method='GET'
            return redirect('/loginA')
        if request.method=='GET':
            return render(request,'permisos.html',{'is_admin':bool(admin),'action':1,'permisos':get_permisos(id_doc,id_pac),'nom_doc':nom_doc,'id_doc':id_doc,'nom_pac':nom_pac,'id_pac':id_pac})
        else:
            seleccionados=request.POST.getlist('permiso')
            remueve_permisos(id_doc,id_pac,seleccionados)
            messages.add_message(request, messages.INFO, 'Se han quitado con exito los permisos selccionados')
            return redirect('administracion:remover_permiso',id_doc=id_doc,nom_pac=nom_pac,nom_doc=nom_doc,id_pac=id_pac)

    except Exception as e:
        return redirect('/login')    
