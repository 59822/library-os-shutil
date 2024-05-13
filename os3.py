import os

def cambiar_nombre(ruta):
    contador = 1 
    nombre = os.listdir(ruta)
    
    for i in nombre:
        nombre_nuevo = str(contador) + "_" + i
        ruta_vieja = os.path.join(ruta, i)
        ruta_neuva = os.path.join(ruta, nombre_nuevo)
        os.rename(ruta_vieja, ruta_neuva)
        contador += 1
    return "Se ha cambiado el nombre de los archivos"
directorio_raiz = "D:\Downloads\helloo"    
nuevo = cambiar_nombre(directorio_raiz)
print(nuevo)