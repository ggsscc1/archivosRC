import os
import pandas as pd

contenido = os.listdir(r'C:\Users\Informatica\Desktop\actas defuncion\28\DEFUNCION')
#print(len(contenido[1]))
cadena = []
for file in contenido:
   
    file = file.replace('.TIF','')
    cadena.append(file)
#print(type(contenido[1]))
#print(len(contenido[1]))
#print(cadena)



archivo = 'Relacion_1992.xlsx'

if archivo:
    df = pd.read_excel(archivo, sheet_name= 'Hoja1')
    columna = df.iloc[:,0:1]
    print(type(df))
    print(columna.values)

else:
    print('No se pudo abrir')

#lista = columna.values.tolist()
#print(lista)
indice = cadena.index('22402800041992000110')
#indice = columna.values.index('22402800041992000110')

print(indice)
