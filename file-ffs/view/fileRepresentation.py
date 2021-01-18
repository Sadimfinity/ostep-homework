from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, ttk
import symbolMap as ventana_symbolMap
import showPlot as ventana_showPlot
import sys

class Interfaz:
    def __init__(self, data, path):
        self.data = data
        self.path = path
        for val in data: print(val.decode(("utf-8")))
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title("Representación de Archivos con File Fast System")
        #self.window.geometry("1000x800") 
        self.createAndPositionButtons()
        #self.createAndPositionEntries()
        self.createAndPositionLabels()

        self.window.mainloop()


        return

    def createAndPositionButtons(self):

        showFileFrame = Button(self.window, text='Mostrar trama de archivos y directorios',command=self.windowShowPlot,
                         width=38, height=1, font=('mincho', 11))
        showSymbolMap = Button(self.window, text='Mostrar mapa de símbolos',command=self.windowShowMap,
                         width=25, height=1, font=('mincho', 11))

        showFileFrame.grid(column=1, row=11,  pady=10, padx=4)
        showSymbolMap.grid(column=1, row=12,  pady=10, padx=4)

        return


    def createAndPositionLabels(self):
        cylinders = Label(self.window, text = "Cilindros", font=('mincho', 11))
        inodes = Label(self.window, text = "INODES", font=('mincho', 11)) 
        data = Label(self.window, text = "DATA", font=('mincho', 11))

        labels = [cylinders, inodes, data] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)

        for i in range(0,10):
            group = Label(self.window, text = str(i), font=('mincho', 11))
            group.grid(row=i+1, column=0, pady=4, padx=4)

        for i in range (1, 11):
            dataSplit = self.data[i].split()
            inodes = dataSplit[1].decode("utf-8") 
            dataGroup = dataSplit[2].decode("utf-8")  + ' ' + dataSplit[3].decode("utf-8")  + ' ' + dataSplit[4].decode("utf-8") 
            values = [inodes, dataGroup]
            for j, val in enumerate(values):
                value = Label(self.window, text = val, font=('mincho', 11))
                value.grid(row=i, column=j+1, pady=4, padx=4)

    def windowShowMap(self):
        self.window.destroy()
        ventana_symbolMap.Interfaz(self.path)

    def windowShowPlot(self):
        self.window.destroy()
        ventana_showPlot.Interfaz(self.path)
    
