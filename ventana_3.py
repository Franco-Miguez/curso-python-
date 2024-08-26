import tkinter as tk
from PIL import Image
from PIL import ImageTk

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
ventana.configure(bg=COLOR_BACKGROUND)

texto = tk.Label(ventana, text="Nombre:", bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
texto_2 = tk.Label(ventana, text="Apellido", bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
entry_nombre = tk.Entry(ventana)
entry_apellido = tk.Entry(ventana)

texto.grid(row=0, column=0)
texto_2.grid(column=0, row=1)
entry_nombre.grid(row=0,column=1)
entry_apellido.grid(row=1,column=1)


ventana.mainloop()