from tkinter import *
from tkinter import ttk


def reset():
    seleccionado.set(None)

def seleccionar():
    pass



root = Tk()

root.geometry("200x200")

frm = ttk.Frame(root, padding=10)
frm.grid()

seleccionado = StringVar()

ttk.Label(frm, text="Te gustó el curso?").grid(column=0, row=0)

radio1 = ttk.Radiobutton(frm, command=seleccionar ,text="Sí, Absolutamente", value=0, variable=seleccionado)
radio2 = ttk.Radiobutton(frm, command=seleccionar ,text="Sí, pero puede mejorar", value=1, variable=seleccionado)
radio3 = ttk.Radiobutton(frm, command=seleccionar ,text="Puede mejorar", value=2, variable=seleccionado)
radio4 = ttk.Radiobutton(frm, command=seleccionar ,text="No, no mucho", value=3, variable=seleccionado)
radio5 = ttk.Radiobutton(frm, command=seleccionar ,text="No, para nada!", value=4, variable=seleccionado)


radio1.grid(column=0, row=3)
radio2.grid(column=0, row=4)
radio3.grid(column=0, row=5)
radio4.grid(column=0, row=6)
radio5.grid(column=0, row=7)




boton = ttk.Button(frm, text="Reiniciar", command=reset)

boton.grid(column=0, row=8)

root.mainloop()