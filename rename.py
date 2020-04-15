import os
import json

print('\n','Escriba la ruta de la carpeta que desea cambiar los nombres. Ejemplo: ')
print('/Users/Cristal/Desktop/github','\n')
ruta = input()
print('\n','Ingrese el tipo de extension de archivo que desea cambiar: ')
nombre_extension = input()
print('\n','Ingrese el nombre que desea darle a los arhivos: ')
nuevo_nombre = input()
files = os.listdir(ruta)
base_de_datos = []  # Directorio para almacenar datos

for index, file in enumerate(files): # Para recorrer los archivos dentro del directorio selecionado
  ext = file.split(".")   # Separamos la extencion para hacer selección de archivos por la extensión solicitada
  
  ext = ext[len(ext) - 1]   

  if ext == nombre_extension: #comparamos los archivos que tienen la extension solicitada
    old = ruta + '/' + file
    new = ruta + '/' + str(nuevo_nombre) + '_' + str(index+1) + '.' + ext # Nueva ruta del archivo, cambiando el str(index) por cualquier nombre
    os.rename(old, new) # Aqui cambiamos los nombres
    lista_archivos = {} # Lista para guardar nombres
    viejo = file
    nuevo = str(nuevo_nombre) + '_' + str(index+1) + '.' + ext # Variable para exportar datos a Json
    lista_archivos['original'] = viejo #listado 1
    lista_archivos['nuevo'] = nuevo  #listado 2
    base_de_datos.append(lista_archivos)  # Agregar datos a listado
print('\n','Archivos renombrados con exito!')

with open('base_de_datos.json', 'w') as archivo: # Para exportar datos a un Json
  json.dump(base_de_datos, archivo)
  print('Archivo JSON con registros de cambio, exportado con exito!','\n')