from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
class filemanager:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        root.update()
        pathString = askopenfilename(initialdir='Mini OS',title='Select File',filetypes=[('All Files','*.*')])
        if pathString != "":
            openFile = open(pathString, 'r')
            fileString = openFile.read()
            print(fileString)
        root.destroy()


#root.mainloop()       
