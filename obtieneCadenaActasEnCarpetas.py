import os
import pandas as pd
import shutil
from generaCarpetaMunicipios import generaCarpetaNumericaMunicipio


#lista carpetas de los municipios desde la ruta inicial
listaCarpetasMunicipio = os.listdir(r'D:\MigracionDefunciones\2017\DEFUNCION')
rutaCarpetasMunicipio = r'D:\MigracionDefunciones\2017\DEFUNCION'
#lista que guarda nombre de archivos
cadena = []
#lista que guarda estatus y se exporta a excel
status = []
#lista que guarda ubicacion y se exporta a excel
ubicacion = []
#ruta a carpeta destino
carpetaDestino = 'D:/MigracionDefunciones/2017/DEFUNCION/'
#variable auxiliar para generar carpeta donde se guardan archivos con cadena erronea
renombrar = '/renombrar'
contador = 0
#recorre carpetas de municipios
for carpetaMunicipio in listaCarpetasMunicipio:
    #ruta de cada municipio contenido en listaCarpetasMunicipio
    path = os.path.join(rutaCarpetasMunicipio, carpetaMunicipio)
    os.chdir(path)
    #print(path)
    #lista contenido dentro de cada carpeta de cada municipio
    contenidoCarpetaMunicipio = os.listdir(path)
    #print(contenidoCarpetaMunicipio[0])
    n = 0
    #Moverse a carpeta def dentro de municipio y listar actas def
    for n in contenidoCarpetaMunicipio:
        path = os.path.join(carpetaDestino, carpetaMunicipio)
        path = os.path.join(path, n)
        os.chdir(path)
        actas = os.listdir(path)
        #quitar extension pdf a actas y genera status
        for archivo in actas:
            #i = 0
            contador = contador + 1
            archivo = archivo.replace('.pdf','')
            cadena.append(archivo)
            #lista_excel = [cadena]
            #print(lista_excel)
df = pd.DataFrame(cadena, columns = ['Cadena'])
df.to_excel('D:/excel/ubicacion.xlsx')
print(contador)
#df = pd.DataFrame(status, columns = ['Cadena'])
#df.to_excel('D:/excel/status.xlsx')
#df = pd.DataFrame(cadena, columns = ['Cadena'])
#df.to_excel('D:/excel/cadena.xlsx')
        
print('Listo')
        