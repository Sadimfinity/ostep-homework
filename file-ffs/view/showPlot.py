from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, Frame, filedialog
import sys
import fileRepresentation as ventana_fileRepresentation

class Interfaz:
    def __init__(self, data, path):
        self.window = Tk()
        self.n = self.n = int(data[-1].decode("utf-8"))
        self.data = data
        self.path = path
        # Inicializar la ventana con un título
        self.window.title('File Fast System')
        self.createAndPositionLabels()
        self.createAndPositionButtons()
        self.window.mainloop()

    def createAndPositionLabels(self):
        titles = ['Tipo', 'Nombre', 'Span']
        for i, val in enumerate(titles):
            value = Label(self.window, text = val, font=('mincho', 11))
            value.grid(row=0, column=i, pady=4, padx=4)

        for i in range (10, 10+self.n):
            values = []
            dataSplit = self.data[i].split()
            typo = dataSplit[0].decode("utf-8")
            if(typo == 'file:'): typo = 'Archivo' 
            elif (typo == 'dir:'): typo = 'Directorio' 
            else: typo = 'Promedio'
            if(typo != 'Promedio'):
                name = dataSplit[1].decode("utf-8")
                span = dataSplit[3].decode("utf-8")
            else:
                name = dataSplit[1].decode("utf-8")
                name = 'Archivo' if name == 'filespan:' else 'Directorio' 
                span = dataSplit[2].decode("utf-8")
            values = [typo, name,span]
            for j, val in enumerate(values):
                value = Label(self.window, text = val, font=('mincho', 11))
                value.grid(row=i-8, column=j, pady=4, padx=4)

    def createAndPositionButtons(self):
        buttonReturn = Button(self.window, text='Regresar', command=self.regresar,
                         width=25, height=1, font=('mincho', 11))
        buttonExit = Button(self.window, text='Salir',command=self.salir,
                         width=25, height=1, font=('mincho', 11))

        buttonReturn.grid(column=1, row=self.n+2,  pady=10, padx=4)
        buttonExit.grid(column=2, row=self.n+2,  pady=10, padx=4)


    def regresar(self):
        self.window.destroy()
        ventana_fileRepresentation.Interfaz(self.data, self.path).window.deiconify()

    def salir(self):
        sys.exit(0)