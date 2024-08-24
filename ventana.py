import tkinter as tk

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
ventana.configure(bg=COLOR_BACKGROUND)

texto = tk.Label(ventana,text="Hola")
texto.config(font=("Frozito",56), bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
texto.pack()

ventana.mainloop()