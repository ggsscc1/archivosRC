import os
import pandas as pd
import shutil

contenido = os.listdir(r'C:\Users\Informatica\Desktop\defuncion disco red\2017\san luis potosi\DEFUNCION')
direccionInicial = 'C:/Users/Informatica/Desktop/defuncion disco red/2017/san luis potosi/DEFUNCION'

#print(len(contenido[1]))
cadena = []
acta = []
for file in contenido:
   
    file = file.replace('.pdf','')
    cadena.append(file)
    acta.append(file)
#print(type(contenido[1]))
#print(len(contenido[1]))
#print(cadena)

#cadenaExample = "22402800022017000110"
#ofi = cadenaExample[6:10]
#print(ofi)
#print(len(cadenaExample))
#status = []
ubicacion = []
for file in acta:
    if len(file) == 20:
        ofi = file[6:10]
        carpetaOfi = ofi[1:]
        direccion = 'C:/Users/Informatica/Desktop/MigracionDefunciones/2017/DEFUNCION/028/'+ carpetaOfi
        tipo = type(direccion)
        shutil.copy(direccionInicial, direccion)
        #os.chdir(direccion)
        direccion = 'T:/MigracionDefunciones/2017/DEFUNCION/028/'+ carpetaOfi
        ubicacion.append(direccion)
        #status.append(1)
    else:
        direccion = 'C:/Users/Informatica/Desktop/MigracionDefunciones/2017/DEFUNCION/028/renombrar'
        #os.chdir(direccion)
        shutil.copy(direccionInicial, direccion)
        ubicacion.append(direccion)
        #status.append(1) 
            
        
""" for file in cadena:
    status.append(1) """
    
#lista_excel = [cadena]
#print(lista_excel)
df = pd.DataFrame(direccion, columns = ['Cadena'])
#df.dtypes()

df.to_excel('C:/Users/Informatica/Desktop/excel a combinar/ubicacion.xlsx')
print('Listo')
#C:\Users\Informatica\Desktop\MigracionDefunciones\2017\DEFUNCION\028
#T:\MigracionDefunciones\2017\DEFUNCION\028