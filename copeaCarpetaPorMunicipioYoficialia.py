#Programa para copear acta por acta desde una carpeta que contiene todas las actas y distribuirlas en cada carpeta segun oficialia y municipio
import os
import pandas as pd
import shutil


#variable para recorrer todas las actas
listaActas = os.listdir(r'C:\Users\Informatica\Desktop\1998 AGUS\28\DEFUNCION\Nueva carpeta')
rutaActas = r'C:\Users\Informatica\Desktop\1998 AGUS\28\DEFUNCION\Nueva carpeta'
#variable que indica la carpeta destino
carpetaDestino = r'D:\MigracionDefunciones\1998\DEFUNCION'
#variable que almacena las cadenas
cadena = []
status = []
ubicacion = []
os.chdir(rutaActas)

for acta in listaActas:
    actaAux = acta
    acta = acta.replace('.pdf','')
    cadena.append(acta)
    status.append(1)
    #Manejando archivos respecto municipio y oficialia y copeandolos en carpeta destino
    if len(acta) == 20:
        mun = acta[3:6]
        ofi = acta[6:10]
        carpetaOfi = ofi[1:]
        direccion = os.path.join(carpetaDestino, mun)

        if os.path.isdir(direccion):
            direccion = os.path.join(direccion, carpetaOfi)
            if os.path.isdir(direccion):
                shutil.copy(actaAux, direccion)
                
            else:
                os.mkdir(direccion)
                shutil.copy(actaAux, direccion)
               

        else:
            os.mkdir(direccion)
            direccion = os.path.join(direccion, carpetaOfi)
            if os.path.isdir(direccion):
                shutil.copy(actaAux, direccion)
                

            else:
                os.mkdir(direccion)
                shutil.copy(actaAux, direccion)
        direccion = 'A:/MigracionDefunciones/1998/DEFUNCION/'+ mun + '/' + carpetaOfi   
        ubicacion.append(direccion)        

    else:
        renombrar = "renombrar"
        direccion = os.path.join(carpetaDestino, renombrar)
        shutil.copy(actaAux, direccion)
        direccion = 'A:/MigracionDefunciones/1998/DEFUNCION/'+ renombrar   
        ubicacion.append(direccion)

df = pd.DataFrame(ubicacion, columns = ['Cadena'])
df.to_excel('D:/excel/ubicacion.xlsx')
df = pd.DataFrame(status, columns = ['Cadena'])
df.to_excel('D:/excel/status.xlsx')
df = pd.DataFrame(cadena, columns = ['Cadena'])
df.to_excel('D:/excel/cadena.xlsx')
        
print('Listo')        

                



