# WEB SCRAPPING 
## OS

Utilización de os nos permite interactuar con el sistema operativo

Funciones
### os.path.join()
Crea rutas de de archivos
### os.path.isfile /os.path.isdir
### os.listdir()
Lista el contenido actual de un directorio
### os.getcwd() 
Para obtener el directorio del trabajo actual
### os.mkdir(path) 
Utiliza un directorio que ya tiene una ubicacion previa por lo tanto es necesario especificar el directorio path.

Para crear un directorio utilizaremnos 
### os.mkdir(“nuevo_directorio”)
Si intentamos crear un directorio dentro de otro directorio que no existe obtendremos un error
### os.mkdir("directorio_padre/nuevo_directorio")
### os.makedirs(path, exist_ok=False) 
Puede crear una ruta con multiples directorios, creando los necesarios. 
os.makedirs(path, exist_ok=False).
Si el booleano es igual exist_ok=True; entonces no hara nada puesto que el directorio existe
Si el booleano es igual exist_ok=False; entonces generara un error si el directorio existe


# Uso de mkdirs
```python
import os

# Especifica la ruta completa que deseas crear
ruta_completa = "/directorio_padre/nuevo_directorio"

# Utiliza os.makedirs() para crear la estructura de directorios completa
os.makedirs(ruta_completa)

# La función creará tanto "directorio_padre" como "nuevo_directorio"
# incluso si "directorio_padre" no existía previamente

print("Estructura de directorios creada con éxito.")
```
### os.remove(path)
Remueve un archivo en la ubicacion especificada por path
Si el archivo no existe habra un error
Para borrar un archivo llamado “archivo.txt” usamos os.remove(“archivo.txt”)

### os.rmdir(path)
Elimina un directorio vacio de la ubicación especificada por path
Si el directorio no esta vacio habrá un error

### os.system(command)
Ejecuta comandos directos del sistema, como “dir”, “cd”. Aquí habria la salida de 0 o cualquier otro valor numerico.
En caso de retornar un valor = 0, se ejecuto correctamente
En caso de retornar un valor != 0, se ejecuto mal

``` python
import os

# Ejecutar un comando para mostrar el contenido de un directorio
codigo_salida = os.system("ls")

# Verificar el código de salida
if codigo_salida == 0:
    print("El comando se ejecutó correctamente.")
else:
    print("Ocurrió un error durante la ejecución del comando.")
```

### os.walk(path)
Permite recorrer un directorio, subdirectorio. Permite iterar en la estructura de directorios y archivos de manera recursiva

```python
import os

# Ruta del directorio raíz que quieres explorar
directorio_raiz = "/ruta/a/tu/directorio"

# Iterar sobre el árbol de directorios utilizando os.walk()
for directorio_actual, subdirectorios, archivos in os.walk(directorio_raiz):
    print("Directorio actual:", directorio_actual)
    print("Subdirectorios:", subdirectorios)
    print("Archivos:", archivos)
```


# Uso
```python

import os

# Obtener el directorio de trabajo actual
current_dir = os.getcwd()
print("Directorio de trabajo actual:", current_dir)

# Crear un nuevo directorio
new_dir = os.path.join(current_dir, "nuevo_directorio")
os.mkdir(new_dir)
print("Nuevo directorio creado:", new_dir)

# Listar el contenido del directorio actual
print("Contenido del directorio actual:")
for item in os.listdir(current_dir):
    print(item)

# Crear un archivo dentro del nuevo directorio
new_file_path = os.path.join(new_dir, "archivo.txt")
with open(new_file_path, "w") as f:
    f.write("¡Hola desde el archivo!\n")
print("Nuevo archivo creado:", new_file_path)

# Eliminar el archivo creado
os.remove(new_file_path)
print("Archivo eliminado:", new_file_path)

# Eliminar el directorio creado
os.rmdir(new_dir)
print("Directorio eliminado:", new_dir)

```
### os.path.getsize()
Permite encontrar el tamaño de los archivos

## USO DE TIME 
```python 
import os.path
import time

# Ruta del archivo que deseas analizar
archivo = "/ruta/a/tu/archivo.txt"

# Obtener la fecha de modificación del archivo en forma de marca de tiempo
fecha_modificacion_timestamp = os.path.getmtime(archivo)

# Convertir la marca de tiempo a una fecha legible
fecha_modificacion = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(fecha_modificacion_timestamp))

# Imprimir la fecha de modificación
print("Fecha de modificación del archivo:", fecha_modificacion)


```

# EJERCICIOS 

## 1. Contar archivos en una ruta 

```python
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
```

## 2. Leer archivos con cierta extensión

```python 
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
```

## 3. Cambiar el nombre de cierta ruta
```python
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

```

### 4. Listar archivos en un directorio y contar cuántos son archivos CSV:

```python
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
```
### 5. Calcular el tamaño promedio de archivos en un directorio:
Uso de os.path.getsize() para encontrar el tamaño
```python 
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
```
### 6. Encontrar el archivo más reciente en un directorio:
Utilizamos getmtime para encontrar el tiempo

```python
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

```
### 7. Crear un informe de resumen de archivos en un directorio:
Utilizamos la libreria time, y en ella utilizamos time.strftime ppara darle formato a la fecha y time.localtime para convertir la fecha en tiempo local

```python
import os
import time

def informe(ruta):
    rute = os.listdir(ruta)
    
    for directorio, subdirectorio, archivo in os.walk(ruta):
        for i in archivo:
            nombre = i
            tamaño = os.path.getsize(os.path.join(directorio, i))
            fecha = os.path.getmtime(os.path.join(directorio, i))
            fecha_Editada =  time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(fecha))
            print(f"Nombre del archivo: {nombre}, Tamaño: {tamaño} bytes, Fecha de modificación: {fecha_Editada}")
            
ruta = "D:\Downloads\helloo"
objeto = informe(ruta)
print(objeto)
            # 
```