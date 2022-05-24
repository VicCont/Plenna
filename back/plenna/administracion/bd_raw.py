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
            print("entrada")
            id=cursor.fetchone()[0]
            print(id)
        except:
            id=None
    return id