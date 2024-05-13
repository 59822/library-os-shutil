import os 
import pdb

def archivos_con_extension(ruta, extension):
    archivos_extension = []
    
    for directorio, subdirectorio, archivo in os.walk(ruta):
        for i in archivo:
            if i.endswith(extension):
                archivos_extension.append(i)
    return archivos_extension

directorio_raiz = "D:\Downloads\helloo"
exte = ".txt"
objeto = archivos_con_extension(directorio_raiz, exte)
print("Los archivos encontrados son:",  objeto)