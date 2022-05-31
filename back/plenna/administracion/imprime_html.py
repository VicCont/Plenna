import csv
import string
from django.urls import reverse
from sympy import re
datos=[]

def generar_form (id_pac,id_esp,nombre):
    return f'''<form action="{reverse('administracion:responder_cuestionario',kwargs={'id_esp':id_esp,'id_pac':id_pac,'nom_pac':nombre})}" method="post">'''

def formatear(datos,permisos,id_pac,nombre):
    tipos={'number':1, 'text':2, 'date':3,'radio':4,'select':5,'check':6,'check/text':7}
    retorno=""
    i=0
    apertura_seccion='<div class="column-grid home-hero">'
    pendientes=""
    cierre_seccion='</div>'
    id_esp_previo=0
    retorno+=apertura_seccion
    while (i<len(datos)):
        if ( id_esp_previo!=datos[i][1]):
            retorno+=pendientes
            pendientes=""
            if (id_esp_previo!=0):
                retorno+=cierre_seccion
            retorno+=apertura_seccion
            id_esp_previo=datos[i][1]
            if (id_esp_previo in permisos):
                retorno+=generar_form(id_pac,id_esp_previo,nombre)
                pendientes+='<br><input id="Submit1" type="submit" value="Actualizar" /><input id="Reset1" type="reset" value="reset" /></form>'
        if (tipos[str(datos[i][5])]<=3):
            retorno+=imprime_input_simple(datos[i])
            i+=1
        elif (tipos[str(datos[i][5])]==4):
            retorno+=imprime_input_radio(datos[i])
            i+=1
        elif (tipos[str(datos[i][5])]==5):
            aux=imprime_input_select(datos,i)
            i=aux[0]
            retorno+=aux[1]
        else:
            aux=imprime_input_checkbox(datos,i)
            i=aux[0]
            retorno+=str(aux[1])
    retorno+=cierre_seccion
    return retorno 




def imprime_input_radio(datos):
    return f'<fieldset><legend>{datos[3]}</legend><label><input type="radio" name="{datos[0]}" value="False"> no</label><label>    <input type="radio" name="{datos[0]}" value="True"> si</label></fieldset> <br>  '


def imprime_input_select(datos,i):
    retorno=f'<label for="{datos[i][0]}">{datos[i][3]}</label>'    
    retorno+=f'<select name="{datos[i][0]}">'
    id_preg=datos[i][0]
    while(id_preg==datos[i][0]):
        respuesta=datos[i][4]
        index = respuesta.find(",", 0, len(respuesta))
        retorno+=f'<option value="{respuesta[0:index]}" >{respuesta[index+1:len(respuesta)]}</option>'

        i+=1
    retorno+="</select><br>"
    return i,retorno

def imprime_input_checkbox(datos,i):
    retorno=f"     <fieldset><legend>{datos[i][3]}</legend>"    
    id_preg=datos[i][0]
    while(id_preg==datos[i][0]):
        respuesta=datos[i][4]
        index = respuesta.find(",", 0, len(respuesta))
        retorno+=f'<input type="checkbox"  value="{respuesta[0:index]}" > {respuesta[index+1:len(respuesta)]}'
        i+=1
    retorno+="</fieldset><br>"
    return i,retorno

def imprime_input_simple(datos):
    return f'<label for="{datos[0]}">{datos[3]}</label><input type="{datos[5]}" id="fname" name="{datos[0]}" value="{datos[4]}"><br>'