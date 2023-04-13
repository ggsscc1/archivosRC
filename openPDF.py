import os
import sys
direccion = (r"D:\MigracionDefunciones\2002\028\011/")
actas = os.listdir(r"D:\MigracionDefunciones\2002\028\011")
for acta in actas:
    os.system(direccion + acta)
    