from tkinter import * #esta libreria es para usar la interfaz grafica 

principal = Tk() 
menu = Menu(principal)

def sen_data(): #En ests parte se guardan los datos ingresados en la Interfaz
    ruta_data =  ruta.get()
    nombre_extension_data = nombre_extension.get() 
    nuevo_nombre_data = nuevo_nombre.get()
    print (ruta_data, '\t',nombre_extension_data, '\t', nuevo_nombre_data) #Imprimir en pantalla los datos ingresados en la interfaz 

#Menu tipo cascada con opciones
principal.config(menu=menu)
principal.title('RENOMBRAR ARCHIVOS') 
principal.resizable(False,False)
filemenu = Menu(menu) 
menu.add_cascade(label='Archivo', menu=filemenu) 
filemenu.add_command(label='Nuevo') 
filemenu.add_command(label='Abrir') 
filemenu.add_separator() 
filemenu.add_command(label='Salir', command=principal.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

Label(principal, text='Ingrese la ruta que contiene los archivos a renombrar: ').grid(row=0)
Label(principal, text='Ingrese el tipo de extensión de archivos que desea cambiar: ').grid(row=2)
Label(principal, text='Ingrese el nuevo nombre que desea darle a sus archivos: ').grid(row=4)

ruta = StringVar()
nombre_extension = StringVar()
nuevo_nombre = StringVar()

ruta_entry = Entry(textvariable = ruta , width = "60")
nombre_extension_entry = Entry(textvariable = nombre_extension, width = "60")
nuevo_nombre_entry = Entry(textvariable = nuevo_nombre , width = "60")

ruta= Entry(principal) # para el ingreso de datos 
nombre_extension  = Entry(principal)# para el ingreso de datos 
nuevo_nombre = Entry(principal)# para el ingreso de datos 
aplicar = Entry(principal)# para el ingreso de datos 
ruta.grid(row=1, column=0, padx=1, pady=10)
nombre_extension.grid(row=3, column=0, padx=1, pady=10)
nuevo_nombre.grid(row=5, column=0, padx=1, pady=10)
submit_btn = Button(principal, text ='aplicar', command = sen_data ).grid(row=7, column=0, padx=1, pady=10) #cracion de el boton aplicar que manda todo a una base de datos 
mainloop()