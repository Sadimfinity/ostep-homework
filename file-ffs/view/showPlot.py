from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, Frame, filedialog
import sys
import fileRepresentation as ventana_fileRepresentation

class Interfaz:
    def __init__(self, path):
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title('File Fast System')
        self.window.geometry('840x500') 
        self.createAndPositionTitles()
        self.createAndPositionLabels()
        self.createAndPositionButtons()
        self.window.mainloop()

    def createAndPositionLabels(self):
        file1 = Label(self.window, text = 'Archivo', font=('mincho', 11))
        name = Label(self.window, text = '/file_name', font=('mincho', 11)) 
        size = Label(self.window, text = 'Tamaño', font=('mincho', 11))
        dire = Label(self.window, text = 'Dir', font=('mincho', 11))
        name2 = Label(self.window, text = 'dassaddas', font=('mincho', 11)) 
        size2 = Label(self.window, text = 'Tamaño', font=('mincho', 11))
        file2 = Label(self.window, text = 'file', font=('mincho', 11))
        name2 = Label(self.window, text = '/file_name', font=('mincho', 11)) 
        size3 = Label(self.window, text = 'Tamaño', font=('mincho', 11))
        labels = [[file1, name, size], [dire, name2, size2], [file2, name2, size3]]

        for i in range(1, len(labels)+1):
            for j in range(len(labels[0])):
                labels[i-1][j].grid(row=i, column=j, pady=4, padx=4,)

    def createAndPositionButtons(self):
        buttonReturn = Button(self.window, text='Regresar', command=self.regresar,
                         width=25, height=1, font=('mincho', 11))
        buttonExit = Button(self.window, text='Salir',command=self.salir,
                         width=25, height=1, font=('mincho', 11))

        buttonReturn.grid(column=1, row=5,  pady=10, padx=4)
        buttonExit.grid(column=2, row=5,  pady=10, padx=4)

    def createAndPositionTitles(self):
        action = Label(self.window, text = 'Tipo', font=('mincho', 14))
        name = Label(self.window, text = 'Nombre', font=('mincho', 14)) 
        size = Label(self.window, text = 'Tamaño', font=('mincho', 14))
        labels = [action, name, size] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)

    def regresar(self):
        self.window.destroy()
        ventana_fileRepresentation.Interfaz().window.deiconify()

    def salir(self):
        sys.exit(0)