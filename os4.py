## Listar archivos en un directorio y contar cuántos son archivos CSV:

import os

def listar_archivos(ruta):
    ruta = os.listdir(ruta)
    contador = 0
    
    for i in ruta:
        if i.endswith(".CSV"):
            contador +=1
    return contador

directorio = "D:\Downloads\helloo"
listado = listar_archivos(directorio)
print("El total de archivos CSV son:", listado)        
        