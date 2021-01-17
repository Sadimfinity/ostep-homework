from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, ttk
import symbolMap as ventana_symbolMap
import showPlot as ventana_showPlot
import sys



class Interfaz:
    def __init__(self):
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

        showFileFrame.grid(column=1, row=5,  pady=10, padx=4)
        showSymbolMap.grid(column=1, row=6,  pady=10, padx=4)

        return


    def createAndPositionLabels(self):
        cylinders = Label(self.window, text = "CILINDROS", font=('mincho', 11))
        inodes = Label(self.window, text = "INODES", font=('mincho', 11)) 
        data = Label(self.window, text = "DATA", font=('mincho', 11))

        labels = [cylinders, inodes, data] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)

        cylinder0 = Label(self.window, text = "Grupo 0", font=('mincho', 11))
        cylinder1 = Label(self.window, text = "Grupo 1", font=('mincho', 11))
        cylinder2 = Label(self.window, text = "Grupo 2", font=('mincho', 11))
        cylinder3 = Label(self.window, text = "Grupo 3", font=('mincho', 11))
        cilindros = [cylinder0,cylinder1,cylinder2,cylinder3]
        for i, val in enumerate(cilindros):
            val.grid(row=i+1, column=0, pady=4, padx=4)
        
        inode0 = Label(self.window, text = "Resultado del inode 0", font=('mincho', 11))
        inode1 = Label(self.window, text = "Resultado del inode 1", font=('mincho', 11))
        inode2 = Label(self.window, text = "Resultado del inode 2", font=('mincho', 11))
        inode3 = Label(self.window, text = "Resultado del inode 3", font=('mincho', 11))
        inodes = [inode0,inode1,inode2,inode3]
        for i, val in enumerate(inodes):
            val.grid(row=i+1, column=1, pady=4, padx=4)
        
        data0 = Label(self.window, text = "Resultado data 0", font=('mincho', 11))
        data1 = Label(self.window, text = "Resultado data 1", font=('mincho', 11))
        data2 = Label(self.window, text = "Resultado data 2", font=('mincho', 11))
        data3 = Label(self.window, text = "Resultado data 3", font=('mincho', 11))
        datas = [data0,data1,data2,data3]
        for i, val in enumerate(datas):
            val.grid(row=i+1, column=2, pady=4, padx=4)

        return


    def windowShowMap(self):
        self.window.destroy()
        ventana_symbolMap.Interfaz()

    def windowShowPlot(self):
        self.window.destroy()
        ventana_showPlot.Interfaz()
    
