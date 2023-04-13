import os
x = range(1, 58)

dobleCero = '00'
for n in x:
  #print(n)
  if n < 10:
      os.mkdir('C:/Users/Informatica/Desktop/proyectoDefun/DEFUNCIONES/2015/Nueva carpeta/'+'00'+str(n))
      print('00'+str(n))
  if n >= 10:
      os.mkdir('C:/Users/Informatica/Desktop/proyectoDefun/DEFUNCIONES/2015/Nueva carpeta/'+'0'+str(n))
      print('0'+str(n))
