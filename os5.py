# Calcular el tamaño promedio de archivos en un directorio:

import os

def promedio_archivos(ruta):
    tamaño = 0
    numero_archivos = 0
    
    for directorio, subdirectorio, archivo in os.walk(ruta):
        for i in archivo:
            tamaño+= os.path.getsize(os.path.join(directorio, i))
            numero_archivos += 1
    
    return f"El tamaño promedio de los archivos es: {tamaño/numero_archivos} bytes"

directorio_raiz = "D:\Downloads\helloo"
objeto = promedio_archivos(directorio_raiz)
print(objeto) 

  
