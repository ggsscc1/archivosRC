import os



#listaMunicipios = 'AHUALULCO','ALAQUINES','AQUISMON','ARMADILLO DE LOS INFANTE','CARDENAS','CATORCE','CEDRAL','CERRITOS','CERRO DE SAN PEDRO','CIUDAD DEL MAIZ','CIUDAD FERNANDEZ','TANCANHUITZ','CIUDAD VALLES','COXCATLAN','CHARCAS','EBANO','GUADALCAZAR','HUEHUETLAN','LAGUNILLAS','MATEHUALA','MEXQUITIC DE CARMONA','MOCTEZUMA','RAYON','RIOVERDE','SALINAS','SAN ANTONIO','SAN CIRO DE ACOSTA','SAN LUIS POTOSI','SAN MARTIN CHALCHICUAUTLA','SAN NICOLAS TOLENTINO','SANTA CATARINA','SANTA MARIA DEL RIO','SANTO DOMINGO','SAN VICENTE TANCUAYALAB','SOLEDAD DE GRACIANO SANCHEZ','TAMASOPO','TAMAZUNCHALE','TAMPACAN','TAMPAMOLON CORONA','TAMUIN','TANLAJAS','TANQUIAN DE ESCOBEDO','TIERRA NUEVA','VANEGAS','VENADO','VILLA DE ARRIAGA','VILLA DE GUADALUPE','VILLA DE LA PAZ','VILLA DE RAMOS','VILLA DE REYES','VILLA HIDALGO','VILLA JUAREZ','AXTLA DE TERRAZAS','XILITLA','ZARAGOZA','VILLA DE ARISTA','MATLAPA','EL NARANJO'
listaMunicipios = 'ahualulco','alaquines','aquismon','armadillo de los infante','cardenas','catorce','cedral','cerritos','cerro de san pedro','ciudad del maiz','ciudad fernandez','tancanhuitz','ciudad valles','coxcatlan','charcas','ebano','guadalcazar','huehuetlan','lagunillas','matehuala','mexquitic de carmona','moctezuma','rayon','rioverde','salinas','san antonio','san ciro de acosta','san luis potosi','san martin chalchicuautla','san nicolas tolentino','santa catarina','santa maria del rio','santo domingo','san vicente tancuayalab','soledad de graciano sanchez','tamasopo','tamazunchale','tampacan','tampamolon corona','tamuin','tanlajas','tanquian de escobedo','tierra nueva','vanegas','venado','villa de arriaga','villa de guadalupe','villa de la paz','villa de ramos','villa de reyes','villa hidalgo','villa juarez','axtla de terrazas','xilitla','zaragoza','villa de arista','matlapa','el naranjo'




#leer carpetas de municipios
municipio = os.listdir('D:/municipios')

#print(municipio)
#print(listaMunicipios)
#print(len(municipio))

def manejaRutaOrigen(): 

    #asigna un numero al municipio para crear la carpeta corresponiente
    contador = 0
    for elemento in municipio:
        
        valorMunicipio = 0
        #print(valorMunicipio)
        for word in listaMunicipios:
            valorMunicipio += 1

            if elemento in word:
                contador = contador + 1
                #print(contador, elemento)

                #print("\n")
                if valorMunicipio < 10:
                    os.mkdir('D:/MigracionDefunciones/2017/DEFUNCION/'+'00'+str(valorMunicipio))
                    print('00'+str(valorMunicipio))
                if valorMunicipio >= 10:
                    os.mkdir('D:/MigracionDefunciones/2017/DEFUNCION/'+'0'+str(valorMunicipio))
                    print('0'+str(valorMunicipio))
                break
    print('a', contador)
        
        
#Funcion auxiliar para generar cadena, ubicacion y status en excel PARTE DE programaCopearRutaFinal          
def generaCarpetaNumericaMunicipio(municipio):
    valorMunicipio = 0

    for word in listaMunicipios:
            valorMunicipio += 1

            if municipio in word:
                #print(municipio)
                #print("\n")
                if valorMunicipio < 10:
                    #os.mkdir('D:/MigracionDefunciones/2017/DEFUNCION/'+'00'+str(valorMunicipio))
                    #print('00'+str(valorMunicipio))
                    return '00'+str(valorMunicipio)
                if valorMunicipio >= 10:
                    #os.mkdir('D:/MigracionDefunciones/2017/DEFUNCION/'+'0'+str(valorMunicipio))
                    #print('0'+str(valorMunicipio))
                    return '0'+str(valorMunicipio)

#manejaRutaOrigen()
#generaCarpetaNumericaMunicipio("valles")