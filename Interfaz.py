from tkinter import Tk, Text, Button, END, re  #Interfaz APP

class Interfaz:
    def __init__(self, ventana, label):
        #Inicializar la ventana con un título
        self.ventana=ventana
        self.ventana.title('RENOMBRADOR DE ARCHIVOS - GMR')
        self.label(pantalla1, Text="Renombrador de Archivos")
        #Agregar una caja de texto para que sea la pantalla de la calculadora
        self.pantalla1=Text(ventana, state="disabled", width=34, height=1, font=("Helvetica",15))
        self.pantalla2=Text(ventana, state="disabled", width=34, height=1, background="orchid", foreground="white", font=("Helvetica",15))
        
        #Ubicar la pantalla en la ventana
        self.pantalla1.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.pantalla2.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        #Inicializar la operación mostrada en pantalla como string vacío
        self.operacion=""

    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica",15), command=lambda:self.click(valor,escribir))

    #Controla el evento disparado al hacer click en un botón
    def click(self, texto, escribir):
        #Si el parámetro 'escribir' es True, entonces el parámetro texto debe mostrarse en pantalla. Si es False, no.
        if not escribir:
            #Sólo calcular si hay una operación a ser evaluada y si el usuario presionó '='
            if texto=="=" and self.operacion!="":
                #Reemplazar el valor unicode de la división por el operador división de Python '/'
                self.operacion=re.sub(u"\u00F7", "/", self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #Si se presionó el botón de borrado, limpiar la pantalla
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)
        return
   
    #Borra el contenido de la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")
        return
   
    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")
        return

ventana_principal=Tk()
calculadora=Interfaz(ventana_principal)
ventana_principal.mainloop()