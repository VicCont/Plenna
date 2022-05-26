from django.db import connection


def get_insights(id_pac):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from obtener_insights(%s)''',[id_pac])
        retorno=cursor.fetchall()
    return retorno

def get_pacientes_doc(id_doc):
    retorno=[]
    with connection.cursor() as cursor:
        cursor.execute('''select * from obtener_pacientes_doc(%s)''',[id_doc])
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