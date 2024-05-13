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

