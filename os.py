import os 

def contar_archivos(ruta):
    archivos = 0
    dicto = 0
    
    contenido = os.listdir(ruta)    
    for i in contenido:
        if os.path.isfile(ruta + "/" + i):
            archivos += 1
            print("Se ha encontrado un archivo")
        elif os.path.isdir(ruta + "/" + i):
            dicto += 1
            print("Se ha encontrado un directorio")
    return f"El total  de archivos son {archivos}, y directorios son {dicto}"      
        

rutix = "D:\Downloads\helloo"
objeto = contar_archivos(rutix)
print(objeto)
