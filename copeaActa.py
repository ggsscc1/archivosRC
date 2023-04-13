#Programa para copear acta por acta desde una carpeta que contiene todas las actas y guardarlas en una variable para pegar en excel a mano
import os
import pandas as pd
import shutil


#variable para recorrer todas las actas
listaActas = os.listdir(r'C:\Users\Informatica\Desktop\entregaFinal\1957\san luis\ahora si ultimas')
cadena = []

for acta in listaActas:
    actaAux = acta
    acta = acta.replace('.pdf','')
    cadena.append(acta)

df = pd.DataFrame(cadena, columns = ['cadena'])
df.to_excel('D:/excel/ultima.xlsx')