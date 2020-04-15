import os
import json

print('Escriba la ruta de la carpeta que desea cambiar los nombres')
print()
#p          rint('Ejemplo')
#print()
#print('/Users/Cristal/Desktop/github')
ruta = input()
#print()

print('Ingrese el tipo de extension de archivo que desea cambiar: ')
nombre_variable = input()

print('Ingrese el new nombre de archivo que desea: ')
nuevo_nombre = input()

files = os.listdir(ruta)

base_de_datos = []  

for index, file in enumerate (files):

  # Separamos la extencion por si queremos cambiar archivos de alguna extension en especifico
  ext = file.split(".")
  ext = ext[len(ext) - 1]

  if ext == nombre_variable: # Este if es solo si queremos cambiar archivos con extension especifica

    # Esta es la ruta antigua del archivo
    old = ruta + '/' + file 

    # Esta es la ruta nueva del archivo y podes cambiar el str(index) por cualquier nombre pero acordate que deben ser unicos 
    new = ruta + '/' + str(nuevo_nombre) + '_' + str(index+1) + '.' + ext

    # Aqui cambiamos los nombres
    os.rename(old, new)

    lista_archivos = {}
    viejo = file
    nuevo = str(nuevo_nombre) + '_' + str(index+1) + '.' + ext
    lista_archivos['original'] = viejo
    lista_archivos['nuevo'] = nuevo
    base_de_datos.append(lista_archivos)  
    

  print(base_de_datos)
  print('Archivos renombrados con exito!')


with open('base_de_datos.json', 'w') as archivo:
  json.dump(base_de_datos, archivo)
  print("Archivo exportado")

files = os.listdir(ruta)