import os
import pandas as pd
import shutil



#lista carpetas de los municipios desde la ruta inicial
rutaActa = r'C:\Users\Informatica\Desktop\entregaFinal\1957\san luis\ahora si ultimas/'
actas = os.listdir(rutaActa)

for acta in actas:
    #ruta de cada municipio contenido en listaCarpetasMunicipio
    auxActa = acta
    #acta = acta +'.pdf'
    #cambiar a bis 1
    #acta =  '224011' + acta[6:]
    #acta = acta + '1.pdf'
    #acta = acta.replace('22402800301998','22402800111998')
    acta = acta[:-4] + '0'
    if(len(acta) == 2):
        acta = '0000' + acta 
    if(len(acta) == 3):
        acta = '000' + acta 
    if(len(acta) == 4):
        acta = '00' + acta
    if(len(acta) == 5):
        acta = '0' + acta
    acta = '22402800011957' + acta + '.TIF'
    #print(acta)  
    rutaInicial = rutaActa + auxActa
    rutaFinal = rutaActa + acta
    os.rename(rutaInicial, rutaFinal)
print('Listo')
