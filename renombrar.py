import os

print('Escriba la ruta de la carpeta que desea cambiar los nombres')
print()
ruta = input()

print('Ingrese el tipo de extension de archivo que desea cambiar: ')
nombre_variable = input()

print('Ingrese el nuevo nombre de archivo que desea: ')
nuevo_nombre = input()

files = os.listdir(ruta)

for index, file in enumerate (files):
    ext = file.split(".")
    ext = ext[len(ext) - 1]

    if ext == nombre_variable:
        viejo = ruta + '/' + file
        nuevo = ruta + '/' + str(nuevo_nombre) + '_' + str(index+1) + '.' + ext

        os.rename(viejo, nuevo)
files = os.listdir(ruta)        