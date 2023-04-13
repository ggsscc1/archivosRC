import os
import pandas as pd
import shutil
from generaCarpetaMunicipios import generaCarpetaNumericaMunicipio


#lista carpetas de los municipios desde la ruta inicial
actos = os.listdir(r'T:\ZONA ALTIPLANO 2022 SLP\2022')
rutaActos = r'T:\ZONA ALTIPLANO 2022 SLP\2022'
#lista que guarda nombre de archivos
cadena = []
#lista que guarda estatus y se exporta a excel
status = []
#lista que guarda ubicacion y se exporta a excel
ubicacion = []
#variable auxiliar para generar carpeta donde se guardan archivos con cadena erronea


#Moverse a carpeta def dentro de municipio y listar actas def
for municipio in actos:
        rutaActos = r'T:\ZONA ALTIPLANO 2022 SLP\2022'
        path = os.path.join(rutaActos, municipio)
        os.chdir(path)
        oficialias = os.listdir(path)
        pathAux = path
        for oficialia in oficialias:
            pathOfi = pathAux 
            pathOfi = os.path.join(pathAux, oficialia)
            actos = os.listdir(pathOfi)
            for acto in actos:
                pathActo = pathOfi
                contador = 0
                path = os.path.join(pathActo, acto)
                
                os.chdir(path)
                actas = os.listdir(path)
                #quitar extension pdf a actas y genera status
                for archivo in actas:
                    #i = 0
                    contador = contador + 1
                    archivo = archivo.replace('.pdf','')
                    cadena.append(archivo)
                    direccion = 'A:/ZONA ALTIPLANO 2022 SLP/2022/'+ municipio + '/' + oficialia + '/' + acto    
                    ubicacion.append(direccion)
        
df = pd.DataFrame(ubicacion, columns = ['Cadena'])
df.to_excel('D:/excel/ubicacion.xlsx')
print(contador)
df = pd.DataFrame(cadena, columns = ['Cadena'])
df.to_excel('D:/excel/cadena.xlsx')
        
print('Listo')
        