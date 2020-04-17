import os
import json
from tkinter import * #esta libreria es para usar la interfaz grafica 
from tkinter import messagebox #importar los cuadros de mensajes
principal = Tk() 
menu = Menu(principal)
#Funcicon del cuadro de texto
def info_adicional():
    messagebox.showinfo(title="Acerca de...", message='Aplicación creada por: ''\n'
    'Jorge Ricardo Rivas Monzon 1990-19-24988' '\n'
    'Jose Manuel Figueroa Figueroa 1990-19-15243''\n'
    'Gustavo Adolfo Domingo Fajardo 1990-19-16436 ')
#Función para la obtencion de datos
def sen_data(): #En ests parte se guardan los datos ingresados en la Interfaz
    ruta_data =  ruta.get()
    nombre_extension_data = nombre_extension.get() 
    nuevo_nombre_data = nuevo_nombre.get()
    files = os.listdir(ruta_data)
    base_de_datos = []  # Directorio para almacenar datos
    for index, file in enumerate(files): # Para recorrer los archivos dentro del directorio selecionado
        ext = file.split(".")   # Separamos la extencion para hacer selección de archivos por la extensión solicitada
        ext = ext[len(ext) - 1] 

        if ext == nombre_extension_data: #comparamos los archivos que tienen la extension solicitada
            old = ruta_data + '/' + file
            new = ruta_data + '/' + str(nuevo_nombre_data) + '_' + str(index+1) + '.' + ext # Nueva ruta del archivo, cambiando el str(index) por cualquier nombre
            os.rename(old, new) # Aqui cambiamos los nombres
            lista_archivos = {} # Lista para guardar nombres
            viejo = file
            nuevo = str(nuevo_nombre_data) + '_' + str(index+1) + '.' + ext # Variable para exportar datos a Json
            lista_archivos['original'] = viejo #listado 1
            lista_archivos['nuevo'] = nuevo  #listado 2
            base_de_datos.append(lista_archivos)  # Agregar datos a listado
    print('\n','Archivos renombrados con exito!')

    with open('base_de_datos.json', 'w') as archivo: # Para exportar datos a un Json
        json.dump(base_de_datos, archivo)
        print('Archivo JSON con registros de cambio, exportado con exito!','\n')


#Menu tipo cascada con opciones
principal.config(menu=menu)
principal.title('Renombrador archivos - RJG') 
principal.resizable(False,False)
#Creación de Menús, pestañas y separadores
filemenu = Menu(menu) 
menu.add_cascade(label='Archivo', menu=filemenu) 
filemenu.add_separator() 
filemenu.add_command(label='Salir', command=principal.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Ayuda', menu=helpmenu) 
helpmenu.add_command(label='About', command = info_adicional) 
Label(principal, text='Ingrese la ruta que contiene los archivos a renombrar: ').grid(row=0)
Label(principal, text='Ingrese el tipo de extensión de archivos que desea cambiar: ').grid(row=2)
Label(principal, text='Ingrese el nuevo nombre que desea darle a sus archivos: ').grid(row=4)
#Variables para guardado de datos
ruta = StringVar()
nombre_extension = StringVar()
nuevo_nombre = StringVar()
#Envío de datos desde los Entry
ruta_entry = Entry(textvariable = ruta , width = "60")
nombre_extension_entry = Entry(textvariable = nombre_extension, width = "60")
nuevo_nombre_entry = Entry(textvariable = nuevo_nombre , width = "60")

ruta= Entry(principal) # para el ingreso de datos 
nombre_extension = Entry(principal)# para el ingreso de datos 
nuevo_nombre = Entry(principal)# para el ingreso de datos 
aplicar = Entry(principal)# para el ingreso de datos 
ruta.grid(row=1, column=0, padx=1, pady=10)
nombre_extension.grid(row=3, column=0, padx=1, pady=10)
nuevo_nombre.grid(row=5, column=0, padx=1, pady=10)

submit_btn = Button(principal, text ='aplicar', command = sen_data ).grid(row=7, column=0, padx=1, pady=10) #cracion de el boton aplicar que manda todo a una base de datos 
mainloop()  


                        