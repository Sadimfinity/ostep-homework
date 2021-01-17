from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, Frame, filedialog
import fileRepresentation as ventana_fileRepresentation

class Interfaz:
    def __init__(self):
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title("File Fast System")
        self.window.geometry("840x500") 
        self.createAndPositionButtons()
        self.createAndPositionEntries()
        self.createAndPositionLabels()

        self.txt = Text(self.window, height = 23, width = 50) 

        self.txt.grid(row=5, column=1, sticky=W, pady=(30,5), padx=4) 

        self.window.mainloop()

    def createAndPositionButtons(self):
        createDiretory = Button(self.window, text='Crear directorio',
                                width=15, height=1, font=('mincho', 11))
        createFile = Button(self.window, text='Crear Archivo',
                            width=15, height=1, font=('mincho', 11))
        deleteFile = Button(self.window, text='Eliminar Archivo',
                            width=15, height=1, font=('mincho', 11))
        execFfs = Button(self.window, text='Crear archivos/directorios',
                         width=25, height=1, font=('mincho', 11), command=self.windowFileRepresentation)
        loadFile = Button(self.window, text='Cargar archivo',
                          width=15, height=1, font=('mincho', 11), command=self.onOpen)
        buttons = [createDiretory, createFile, deleteFile]

        for i, val in enumerate(buttons):
            val.grid(row=i + 1, column=0, sticky=W, pady=4, padx=4)
        execFfs.grid(row=6, column=1, pady=4)
        loadFile.grid(row=7, column=2, pady=4)

    def createAndPositionEntries(self):
        for i in range(0,3):
            e = Entry(self.window, font=('mincho', 14))
            e.grid(row=i + 1, column=1, pady=4, padx=4)
        size = Entry(self.window, font=('mincho', 14))
        size.grid(row=2, column=2, pady=4, padx=4)

    def createAndPositionLabels(self):
        action = Label(self.window, text = "Acción", font=('mincho', 11))
        name = Label(self.window, text = "Nombre", font=('mincho', 11)) 
        size = Label(self.window, text = "Tamaño", font=('mincho', 11))
        infoLabel = Label(self.window, text = "En caso de tener el txt listo, puede cargar el archivo")
        labels = [action, name, size] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)
        infoLabel.grid(row=7, column=1, pady=4, padx=4)

    def onOpen(self):
        ftypes = [('Todos los archivos', '*')]
        dlg = filedialog.Open(self.window, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)


    def readFile(self, filename):

        with open(filename, "r") as f:
            text = f.read()

        return text

    def windowFileRepresentation(self):
        self.window.destroy()
        ventana_fileRepresentation.Interfaz()

calculadora = Interfaz()