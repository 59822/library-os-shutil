### Encontrar el archivo más reciente en un directorio:

import os 

def archivo_reciente(ruta):
    linea = os.listdir(ruta)
    reciente = None
    fecha = 0
    
    for directorio, subdirectorio, archivo in os.walk(ruta):
        for i in archivo:
            ner_rute = os.path.join(directorio, i)
            fechamodificada = os.path.getmtime(ner_rute)
            if fechamodificada > fecha:
                fecha = fechamodificada
                reciente = i
    return reciente

ruta = "D:\Downloads\helloo"
objeto = archivo_reciente(ruta)
print("El archivo más reciente es:", objeto)
