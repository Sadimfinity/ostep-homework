from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, ttk
import sys
import fileRepresentation as ventana_fileRepresentation

class Interfaz:
    def __init__(self, data, path):
        self.window = Tk()
        self.data = data
        self.n = int(data[10].decode('utf-8'))
        self.path = path
        # Inicializar la ventana con un título
        self.window.title('Mostrar mapa de símbolos')
        self.createAndPositionButtons()
        self.createAndPositionLabels()
        self.window.mainloop()

    def createAndPositionButtons(self):

        buttonReturn = Button(self.window, text='Regresar', command=self.regresar,
                         width=25, height=1, font=('mincho', 11))
        buttonExit = Button(self.window, text='Salir',command=self.salir,
                         width=25, height=1, font=('mincho', 11))

        buttonReturn.grid(column=1, row=self.n+2,  pady=10, padx=4)
        buttonExit.grid(column=2, row=self.n+2,  pady=10, padx=4)

    def createAndPositionLabels(self):
        labels = ['Símbolo', 'Inodo', 'Nombre del archivo','Tipo de archivo'] 
        for i, val in enumerate(labels):
            value = Label(self.window, text = val, font=('mincho', 12))
            value.grid(row=0, column=i, pady=4, padx=4)

        for i in range (13, 13+self.n):
            dataSplit = self.data[i].split()
            symbol = dataSplit[0].decode('utf-8')
            inode = dataSplit[1].decode('utf-8')
            filename = dataSplit[2].decode('utf-8') 
            filetype = 'Archivo' if dataSplit[3].decode('utf-8') == 'regular' else 'Directorio'
            
            values = [symbol,inode,filename,filetype]
            for j, val in enumerate(values):
                value = Label(self.window, text = val, font=('mincho', 11))
                value.grid(row=i-11, column=j, pady=4, padx=4)

    def regresar(self):
        self.window.destroy()
        ventana_fileRepresentation.Interfaz(self.data, self.path).window.deiconify()

    def salir(self):
        sys.exit(0)
    

