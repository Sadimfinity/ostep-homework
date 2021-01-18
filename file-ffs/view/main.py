import subprocess
import os
from tkinter import Tk, Text, Button, END, re, font, W, Entry, Label, Frame, filedialog
import fileRepresentation as ventana_fileRepresentation

class Interfaz:
    def __init__(self):
        self.window = Tk()
        # Inicializar la ventana con un título
        self.window.title('File Fast System')
        self.window.geometry('840x500') 
        self.createAndPositionButtons()
        self.entries = self.createAndPositionEntries()
        self.createAndPositionLabels()
        self.path = ''
        self.txt = Text(self.window, height = 23, width = 50, state='disabled') 

        self.txt.grid(row=5, column=1, sticky=W, pady=(30,5), padx=4) 

        self.window.mainloop()

    def createAndPositionButtons(self):
        createDiretory = Button(self.window, text='Crear directorio',
                                width=15, height=1, font=('mincho', 11), command=self.createDirectory)
        createFile = Button(self.window, text='Crear Archivo',
                            width=15, height=1, font=('mincho', 11), command=self.createFile)
        deleteFile = Button(self.window, text='Eliminar Archivo',
                            width=15, height=1, font=('mincho', 11), command=self.deleteFile)
        execFfs = Button(self.window, text='Crear archivos/directorios',
                         width=25, height=1, font=('mincho', 11), command=self.execFFS)
        loadFile = Button(self.window, text='Cargar archivo',
                          width=15, height=1, font=('mincho', 11), command=self.onOpen)
        buttons = [createDiretory, createFile, deleteFile]

        for i, val in enumerate(buttons):
            val.grid(row=i + 1, column=0, sticky=W, pady=4, padx=4)
        execFfs.grid(row=6, column=1, pady=4)
        loadFile.grid(row=7, column=2, pady=4)

    def createDirectory(self):
        if self.entries[0].get() != '':
            self.txt.configure(state='normal')
            self.txt.insert(END, 'dir '+ self.entries[0].get()+ '\n')
            self.txt.configure(state='disabled')
            self.entries[0].delete(0, END)

    def createFile(self):
        if self.verifyNatural():
            self.txt.configure(state='normal')
            self.txt.insert(END, 'file ' + self.entries[1].get() + ' '+ self.entries[3].get()  +'\n')
            self.txt.configure(state='disabled')
        self.entries[1].delete(0, END)
        self.entries[3].delete(0, END)


    def verifyNatural(self):
        return self.entries[1].get() != '' and self.entries[3].get().isdigit()

    def deleteFile(self):
        if self.entries[2].get() != '':
            self.txt.configure(state='normal')
            self.txt.insert(END, 'delete ' + self.entries[2].get()+ '\n')
            self.txt.configure(state='disabled')
            self.entries[2].delete(0, END)


    def createAndPositionEntries(self):
        entries = []
        for i in range(0,3):
            entries.append(Entry(self.window, font=('mincho', 14)))
            entries[i].grid(row=i + 1, column=1, pady=4, padx=4)
        size = Entry(self.window, font=('mincho', 14))
        entries.append(size)
        size.grid(row=2, column=2, pady=4, padx=4)
        return entries

    def createAndPositionLabels(self):
        action = Label(self.window, text = 'Acción', font=('mincho', 11))
        name = Label(self.window, text = 'Nombre', font=('mincho', 11)) 
        size = Label(self.window, text = 'Tamaño', font=('mincho', 11))
        infoLabel = Label(self.window, text = 'En caso de tener el txt listo, puede cargar el archivo')
        labels = [action, name, size] 
        for i, val in enumerate(labels):
            val.grid(row=0, column=i, pady=4, padx=4)
        infoLabel.grid(row=7, column=1, pady=4, padx=4)

    def onOpen(self):
        ftypes = [('Todos los archivos', '*')]
        dlg = filedialog.Open(self.window, filetypes = ftypes)
        path = dlg.show()

        if path != '':
            text = self.readFile(path)
            self.txt.configure(state='normal')
            self.txt.insert(END, text)
            self.txt.configure(state='disabled')
            self.unableEntries()
            self.path = path
            

    def unableEntries(self):
        for i in range(len(self.entries)):
            self.entries[i].configure(state='disabled')

    def readFile(self, filename):

        with open(filename, 'r') as f:
            text = f.read()

        return text

    def execFFS(self):
        self.writeFile()
        b = subprocess.Popen('../src/ffs.py -f ' + self.path + ' -c', shell=True, stdout=subprocess.PIPE).stdout.readlines()
        print(b[1])
        self.window.destroy()
        ventana_fileRepresentation.Interfaz(b, self.path)

    def writeFile(self):
        if self.path == '':
            path = '../assets/input_user_file'
            f = open(path, 'w+')
            f.write(self.txt.get('1.0', END))
            f.close()
            self.path = path

calculadora = Interfaz()