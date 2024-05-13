#Crear un informe de resumen de archivos en un directorio nombre del archivo, su tamaño y la fecha de modificación. 

import os
import time

def informe(ruta):
    rute = os.listdir(ruta)
    
    for directorio, subdirectorio, archivo in os.walk(ruta):
        for i in archivo:
            nombre = i
            tamaño = os.path.getsize(os.path.join(directorio, i))
            fecha = os.path.getmtime(os.path.join(directorio, i))
            fecha_Editada =  time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(fecha)) #usamos strftime para darle formato a la fecha y time.localtime para convertir la fecha en tiempo local
            print(f"Nombre del archivo: {nombre}, Tamaño: {tamaño} bytes, Fecha de modificación: {fecha_Editada}")
            
ruta = "D:\Downloads\helloo"
objeto = informe(ruta)
print(objeto)
            

