
from tkinter import *
from tkinter import ttk


def Preview():
    pass

root=Tk()
root.geometry("500x200")
root.title("Upload Image free")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))



boton=ttk.Button(mainframe, text="Visualizar en la aplicación", command=Preview).grid(column=3, row=3, sticky=W)

root.mainloop()
