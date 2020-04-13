import os
print('Escriba la ruta de la carpeta que desea cambiar los nombres')
print()
print('Ejemplo')
print()
print('/Users/Cristal/Desktop/github')
ruta = input()
print()



files = os.listdir(ruta)

for index, file in enumerate(files):

  # Separamos la extencion por si queremos cambiar archivos de alguna extension en especifico
  ext = file.split(".")
  ext = ext[len(ext) - 1]

  if ext == "jpg": # Este if es solo si queremos cambiar archivos con extension especifica

    # Esta es la ruta antigua del archivo
    viejo = ruta + '/' + file

    # Esta es la ruta nueva del archivo y podes cambiar el str(index) por cualquier nombre pero acordate que deben ser unicos 
    nuevo = ruta + '/ejemplo_' + str(index+1) + '.' + ext

    # Aqui cambiamos los nombres
    os.rename(viejo, nuevo)
files = os.listdir(ruta)



