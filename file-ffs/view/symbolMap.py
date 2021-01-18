from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, ttk
import sys
import fileRepresentation as ventana_fileRepresentation



class Interfaz:
    def __init__(self, path):
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title("Mostrar mapa de símbolos")
        #self.window.geometry("1000x800") 
        self.createAndPositionButtons()
        #self.createAndPositionEntries()
        self.createAndPositionLabels()
        
        self.window.mainloop()
        Button(self, text="Quit", command=self.window.destroy).pack()


        return

    def createAndPositionButtons(self):

        buttonReturn = Button(self.window, text='Regresar', command=self.regresar,
                         width=25, height=1, font=('mincho', 11))
        buttonExit = Button(self.window, text='Salir',command=self.salir,
                         width=25, height=1, font=('mincho', 11))

        buttonReturn.grid(column=1, row=5,  pady=10, padx=4)
        buttonExit.grid(column=2, row=5,  pady=10, padx=4)

        return


    def createAndPositionLabels(self):
        symbol = Label(self.window, text = "SYMBOL", font=('mincho', 11))
        inode = Label(self.window, text = "INODE", font=('mincho', 11)) 
        filename = Label(self.window, text = "FILENAME", font=('mincho', 11))
        filetype = Label(self.window, text = "FILETYPE", font=('mincho', 11))

        labels = [symbol, inode, filename,filetype] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)

        symbol0 = Label(self.window, text = "symbolo 0", font=('mincho', 11))
        symbol1 = Label(self.window, text = "symbolo 1", font=('mincho', 11))
        symbol2 = Label(self.window, text = "symbolo 2", font=('mincho', 11))
        symbol3 = Label(self.window, text = "symbolo 3", font=('mincho', 11))
        symbols = [symbol0,symbol1,symbol2,symbol3]
        for i, val in enumerate(symbols):
            val.grid(row=i+1, column=0, pady=4, padx=4)
        
        inode0 = Label(self.window, text = "inode 0", font=('mincho', 11))
        inode1 = Label(self.window, text = "inode 1", font=('mincho', 11))
        inode2 = Label(self.window, text = "inode 2", font=('mincho', 11))
        inode3 = Label(self.window, text = "inode 3", font=('mincho', 11))
        inodes = [inode0,inode1,inode2,inode3]
        for i, val in enumerate(inodes):
            val.grid(row=i+1, column=1, pady=4, padx=4)
        
        filename0 = Label(self.window, text = "filename 0", font=('mincho', 11))
        filename1 = Label(self.window, text = "filename 1", font=('mincho', 11))
        filename2 = Label(self.window, text = "filename 2", font=('mincho', 11))
        filename3 = Label(self.window, text = "filename 3", font=('mincho', 11))
        filenames = [filename0,filename1,filename2,filename3]
        for i, val in enumerate(filenames):
            val.grid(row=i+1, column=2, pady=4, padx=4)
        
        filetype0 = Label(self.window, text = "filetype 0", font=('mincho', 11))
        filetype1 = Label(self.window, text = "filetype 1", font=('mincho', 11))
        filetype2 = Label(self.window, text = "filetype 2", font=('mincho', 11))
        filetype3 = Label(self.window, text = "filetype 3", font=('mincho', 11))
        filetypes = [filetype0,filetype1,filetype2,filetype3]
        for i, val in enumerate(filetypes):
            val.grid(row=i+1, column=3, pady=4, padx=4)

        return


    def regresar(self):
        self.window.destroy()
        ventana_fileRepresentation.Interfaz().window.deiconify()

    def salir(self):
        sys.exit(0)
    

