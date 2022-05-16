import csv
from collections import defaultdict
import copy
preguntas_seccion=defaultdict(list)
datos={}
columnas=[]
faltantes=0
seccion_actual=""
with open('ITAM + Plenna.csv',encoding="latin1", mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if (line_count>=36):
            print("ccc")
        if (line_count==0):
            for y in row:
                if not str(y):
                    columnas.append(f"extra{faltantes}")
                    faltantes+=1
                else:
                    columnas.append(str(y))
        else:
            if (not row[1]):
                if (line_count!=1):
                    datos[seccion_actual]=copy.deepcopy(preguntas_seccion)
                    preguntas_seccion.clear()
                seccion_actual=row[0]
            else:
                for x in range(len(columnas)):
                    preguntas_seccion[str(columnas[x])].append(row[x])
        line_count += 1
datos[seccion_actual]=preguntas_seccion
print (f"categorias {[x for x in datos.keys()]}")
imprimible=""
for x in datos.keys():
    i=0
    for y in range(len(datos[x][columnas[0]])):
        retorno="\n"+str(x)
        i=0
        while (i<len(columnas)):
            if (not str(datos[x][str(columnas[i])][y]) and i!=2):
                if (i<4):
                    imprimible+=retorno+"|"
                break
            if(i>2):
                imprimible+=retorno+"|"+str(datos[x][str(columnas[i])][y])
            else:
                retorno+="|"+str(datos[x][str(columnas[i])][y])
            i+=1
print(imprimible)
file1 = open("insertable.csv", "w")  # write mode
file1.write(imprimible)
file1.close()

