import os
import pandas as pd
import shutil
from generaCarpetaMunicipios import generaCarpetaNumericaMunicipio


#lista carpetas de los municipios desde la ruta inicial
listaCarpetasMunicipio = os.listdir(r'D:\municipios')
rutaCarpetasMunicipio = r'D:\municipios'
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
#recorre carpetas de municipios
for carpetaMunicipio in listaCarpetasMunicipio:
    #ruta de cada municipio contenido en listaCarpetasMunicipio
    path = os.path.join(rutaCarpetasMunicipio, carpetaMunicipio)
    os.chdir(path)
    #print(path)
    numMun = generaCarpetaNumericaMunicipio(carpetaMunicipio)
    #print(type(numMun))

    #lista contenido dentro de cada carpeta de cada municipio
    contenidoCarpetaMunicipio = os.listdir(path)
    #print(contenidoCarpetaMunicipio[0])

    #Moverse a carpeta def dentro de municipio y listar actas def
    path = os.path.join(path, contenidoCarpetaMunicipio[0])
    os.chdir(path)
    actas = os.listdir(path)
    #quitar extension pdf a actas y genera status
    for archivo in actas:
        #i = 0
        #agrega auxiliar y guarda nombre de acta sin extension pdf junto con status
        actaAux = archivo
        archivo = archivo.replace('.pdf','')
        cadena.append(archivo)
        status.append(1)
        #Manejando archivos respecto oficialia y copeandolos en carpeta destino
        if len(archivo) == 20:
            ofi = archivo[6:10]
            carpetaOfi = ofi[1:]
            carpetaMun = os.path.join(carpetaDestino, numMun)
            direccion = os.path.join(carpetaMun, carpetaOfi)
            #print(carpetaMun)
            #direccion = 'D:/MigracionDefunciones/2017/DEFUNCION/'+ numMun + '/' + carpetaOfi

            #copear actas a carpeta correspondiente y crear carpetas si no existen
            if os.path.isdir(carpetaMun):
                if os.path.isdir(direccion):
                    #print("Hola ruta completa")
                    shutil.copy(actaAux, direccion)
                else:
                    #print("Hola ruta falta direccion")
                    os.mkdir(direccion)
                    shutil.copy(actaAux, direccion)
            else : 
                #print("Hola ruta falta todo")
                os.mkdir(carpetaMun)
                os.mkdir(direccion)
                shutil.copy(actaAux, direccion)
            
            direccion = 'A:/MigracionDefunciones/2017/DEFUNCION/'+ numMun + '/' + carpetaOfi   
            ubicacion.append(direccion)
        else:
            #os.chdir(direccion)
            ##checar direccion donde se colocan las renombradas----------------------------------------------
            #------------------------------------------------
            direccion = os.path.join(carpetaMun, renombrar)
            if os.path.isdir(direccion):
                shutil.copy(actaAux, direccion)
            else: 
                os.mkdir(direccion)
                shutil.copy(actaAux, direccion)
            direccion = 'A:/MigracionDefunciones/2017/DEFUNCION/'+ numMun + '/' + renombrar   
            ubicacion.append(direccion)
            #status.append(1)
        #lista_excel = [cadena]
        #print(lista_excel)
df = pd.DataFrame(ubicacion, columns = ['Cadena'])
df.to_excel('D:/excel/ubicacion.xlsx')
df = pd.DataFrame(status, columns = ['Cadena'])
df.to_excel('D:/excel/status.xlsx')
df = pd.DataFrame(cadena, columns = ['Cadena'])
df.to_excel('D:/excel/cadena.xlsx')
        
print('Listo')
        