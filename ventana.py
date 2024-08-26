import tkinter as tk
from PIL import Image
from PIL import ImageTk


def cambiar_imagen(widget, img):
    widget.config(image=img)

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
ventana.configure(bg=COLOR_BACKGROUND)

texto = tk.Label(ventana,text="Hola")
texto.config(font=("Frozito",56), bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
texto.pack()
"""
img = tk.PhotoImage(file="img.png")
label_img = tk.Label(ventana, image=img, bd=0)
label_img.pack()


img_salir = tk.PhotoImage(file="./img/next.png")
btn_salir = tk.Button(ventana, image=img_salir, command=lambda: cambiar_imagen(btn_salir, img))
btn_salir.config(bg="#ff4122", height=300, width=50, fg=COLOR_TEXT)
btn_salir.pack()

btn_rojo = tk.Button(ventana, width=10,height=10,bg="#ff2222", command=lambda: ventana.config(bg="#FF2222"))
btn_rojo.pack()
btn_azul = tk.Button(ventana, width=10,height=10,bg="#22FF22", command=lambda: ventana.config(bg="#22ff22"))
btn_azul.pack()


frame_top = tk.Frame(ventana, bg="#ff0000", height=200, width=200)
frame_down = tk.Frame(ventana, bg="#00ff00", height=200, width=200)

frame_top.pack()
frame_down.pack()
"""
entry_nombre = tk.Entry(ventana, fg="grey")
entry_nombre.insert(0,"Ingrese su nombre")
entry_nombre.pack()

tk.Button(ventana, text="Saludar", command=lambda: entry_nombre.delete(0,2)).pack()

text_info = tk.Text(ventana, height=10, width=100)
text_info.pack()

tk.Button(ventana, text="Texto", command=lambda: print(text_info.get("0"))).pack()

ventana.mainloop()
