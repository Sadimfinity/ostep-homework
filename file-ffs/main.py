from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label


class Interfaz:
    def __init__(self):
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title("File Fast System")
        self.createAndPositionButtons()
        self.createAndPositionEntries()
        self.createAndPositionLabels()
        self.window.mainloop()
        return

    def createAndPositionButtons(self):
        createDiretory = Button(self.window, text='Crear directorio',
                                width=15, height=1, font=('mincho', 11))
        createFile = Button(self.window, text='Crear Archivo',
                            width=15, height=1, font=('mincho', 11))
        deleteFile = Button(self.window, text='Eliminar Archivo',
                            width=15, height=1, font=('mincho', 11))
        execFfs = Button(self.window, text='Crear archivos/directorios',
                         width=25, height=1, font=('mincho', 11))
        loadFile = Button(self.window, text='Cargar archivo',
                          width=15, height=1, font=('mincho', 11))
        buttons = [createDiretory, createFile, deleteFile]

        for i, val in enumerate(buttons):
            val.grid(row=i + 1, column=0, sticky=W, pady=4, padx=4)

        return

    def createAndPositionEntries(self):
        for i in range(0,3):
            e = Entry(self.window, font=('mincho', 14))
            e.grid(row=i + 1, column=1, pady=4, padx=4)
        size = Entry(self.window, font=('mincho', 14))
        size.grid(row=2, column=2, pady=4, padx=4)
        return 

    def createAndPositionLabels(self):
        action = Label(self.window, text = "Acción", font=('mincho', 11))
        name = Label(self.window, text = "Nombre", font=('mincho', 11)) 
        size = Label(self.window, text = "Tamaño", font=('mincho', 11))
        labels = [action, name, size] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)
        return


calculadora = Interfaz()