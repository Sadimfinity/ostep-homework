from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, ttk
import symbolMap as ventana_symbolMap
import showPlot as ventana_showPlot
import sys
import subprocess

class Interfaz:
    def __init__(self, data, path):
        self.data = data
        self.path = path
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
        labels = ['Cilindros', 'Inodos', 'Data']
        for i, val in enumerate(labels):
            value = Label(self.window, text = val, font=('mincho', 11))
            value.grid(row=0, column=i, pady=4, padx=4)

        for i in range(0,10):
            group = Label(self.window, text = str(i), font=('mincho', 11))
            group.grid(row=i+1, column=0, pady=4, padx=4)

        for i in range (0, 10):
            dataSplit = self.data[i].split()
            inodes = dataSplit[1].decode("utf-8") 
            dataGroup = dataSplit[2].decode("utf-8")  + ' ' + dataSplit[3].decode("utf-8")  + ' ' + dataSplit[4].decode("utf-8") 
            values = [inodes, dataGroup]
            for j, val in enumerate(values):
                value = Label(self.window, text = val, font=('mincho', 11))
                value.grid(row=i+1, column=j+1, pady=4, padx=4)

    def windowShowMap(self):
        self.window.destroy()
        data = subprocess.Popen('../src/ffs.py -f ' + self.path + ' -c -M', shell=True, stdout=subprocess.PIPE).stdout.readlines()
        ventana_symbolMap.Interfaz(data, self.path)

    def windowShowPlot(self):
        self.window.destroy()
        data = subprocess.Popen('../src/ffs.py -f ' + self.path + ' -c -T', shell=True, stdout=subprocess.PIPE).stdout.readlines()
        ventana_showPlot.Interfaz(data, self.path)
    
