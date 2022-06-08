from django.db import connection
from django.conf import settings

def get_permisos(id_doc,id_pac):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from get_permisos(%s,%s)''',[id_doc,id_pac])
        retorno=cursor.fetchall()
    return retorno

def actualiza_cuestionario(request,id_esp,id_pac):
    ids_ab=[]
    ids_cerr=[]
    resp_ab=[]
    resp_cerr=[]        
    pregs=get_preguntas_esp(id_esp)
    tipos=settings.TIPOS
    for preg in pregs:
        respondido=request.POST.getlist(str(preg[0]))
        for i in respondido:
            if tipos[preg[1]]<=4:
                resp_ab.append(i)
                ids_ab.append(preg[0])    
            else:
                if i=="otro":
                    resp_ab.append(request.POST[f'otro{preg[0]}'])
                    ids_ab.append(preg[0])
                resp_cerr.append(int(i))
                ids_cerr.append(int(preg[0]))    
    with connection.cursor() as cursor:
        cursor.execute('''select actualiza_resp_abierta(%s,%s,%s,%s)''',[id_pac,ids_ab,resp_ab,id_esp])
        cursor.execute('''select inserta_resp_cerrada(%s,%s,%s)''',[id_pac,ids_cerr,resp_cerr])
        cursor.fetchall()

def get_preguntas_esp (id_esp):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from get_preguntas_esp(%s)''',[id_esp])
        retorno=cursor.fetchall()
    return retorno    

def get_permisos_faltantes(id_doc,id_pac):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from get_permisos_faltantes(%s,%s)''',[id_doc,id_pac])
        retorno=cursor.fetchall()
    return retorno

def get_permisos_doc(id_doc):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from get_permisos_doc(%s)''',[id_doc])
        retorno=cursor.fetchall()
    return retorno

def get_insights(id_pac):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from obtener_insights(%s)''',[id_pac])
        retorno=cursor.fetchall()
    return retorno

def obtener_datos(id):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from obtener_datos(%s)''',[id])
        retorno=cursor.fetchall()
    return retorno 

def get_docs():
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from get_docs()''')
        retorno=cursor.fetchall()
    return retorno

def remueve_permisos(id_doc,id_pac,lista):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select remueve_permisos(%s,%s,%s::int[])''',[id_doc,id_pac,list(lista)])
        retorno=cursor.fetchall()
    return retorno     

def insert_permisos(id_doc,id_pac,lista):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select insert_permisos(%s,%s,%s::int[])''',[id_doc,id_pac,list(lista)])
        retorno=cursor.fetchall()
    return retorno   

def get_pacientes_doc(id_doc):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from obtener_pacientes_doc(%s)''',[id_doc])
        retorno=cursor.fetchall()
    return retorno 

def get_pacientes():
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select id_pac, nombre,clave_pac from paciente p''')
        retorno=cursor.fetchall()
    return retorno 

def login_doc(usu,passw):
    id=None
    with connection.cursor() as cursor:
        cursor.execute('''select login(%s,%s)''', [usu,passw])
        id = cursor.fetchone()
        id=id[0]
        try:
            id=int(id)
        except:
            id=None
    return id

def login_adm(usu,passw):
    id=None
    with connection.cursor() as cursor:
        cursor.execute('''select login_admin(%s,%s)''', [usu,passw])
        try:
            id=cursor.fetchone()[0]
            print(id)
        except:
            id=None
    return id

def insert_insight(doc, pac, texto):
    resp=None
    with connection.cursor() as cursor:
        cursor.execute('''select insertar_insight(%s,%s,%s)''', [doc,pac,texto])
        try:
            resp=bool(cursor.fetchone()[0])
            print(id)
        except:
            resp=None
    return resp   

def is_authorized(doc,pac):
    resp=None
    with connection.cursor() as cursor:
        cursor.execute('''select is_authorized(%s,%s)''', [doc,pac])
        try:
            resp=bool(cursor.fetchone()[0])
            print(id)
        except:
            resp=None
    return resp