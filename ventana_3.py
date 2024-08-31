import tkinter as tk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
ventana.configure(bg=COLOR_BACKGROUND)

def saludar(nombre : str, apellido : str):
    if nombre != "" and apellido != "" and nombre.isalpha() and apellido.isalpha():
        texto = f"Hola {nombre} {apellido}"
        tk.Label(ventana,text=texto).grid(column=0,row=3)
    else:
        messagebox.showinfo("info", "ingrese un nombre y apellido sin caracteres especiales o numerico")


texto = tk.Label(ventana, text="Nombre:", bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
texto_2 = tk.Label(ventana, text="Apellido", bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
entry_nombre = tk.Entry(ventana)
entry_apellido = tk.Entry(ventana)
boton_saludar = tk.Button(ventana,text="Saludar", width=20, height=10, command=lambda: saludar(entry_nombre.get(),entry_apellido.get()))

texto.grid(row=0, column=1)
texto_2.grid(column=1, row=1, ipadx=5)
entry_nombre.grid(row=0,column=2)
entry_apellido.grid(row=1,column=2)
boton_saludar.grid(row=0,column=0, rowspan=2)


ventana.mainloop()