from tkinter import *
principal = Tk() 
menu = Menu(principal)

#Menu tipo cascada con opciones
principal.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Archivooo', menu=filemenu) 
filemenu.add_command(label='Nuevooo') 
filemenu.add_command(label='Abrir') 
filemenu.add_separator() 
filemenu.add_command(label='Salir', command=principal.quit) 
menu_ayuda = Menu(menu) 
menu.add_cascade(label='Ayuda', menu=menu_ayuda) 
menu_ayuda.add_command(label='About') 

Label(principal, text='Ingrese la ruta que contiene los archivos a renombrar: ').grid(row=0)
Label(principal, text='Ingrese el tipo de extensión de archivos que desea cambiar: ').grid(row=2)
Label(principal, text='Ingrese el nuevo nombre que desea darle a sus archivos: ').grid(row=4)
e1 = Entry(principal)
e2 = Entry(principal)
e3 = Entry(principal)
e1.grid(row=1, column=0, padx=1, pady=10)
e2.grid(row=3, column=0, padx=1, pady=10)
e3.grid(row=5, column=0, padx=1, pady=10)
mainloop() 

print('Seleccione el tipo de cliente:','\n')
print('1. Cliente Estandar')
print('2. Miembro','\n')

