import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


def cambiar_imagen(widget, img):
    widget.config(image=img)

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"
IMAGE_ICON = "./img/icono.ico"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
ventana.configure(bg=COLOR_BACKGROUND)
ventana.iconbitmap(IMAGE_ICON)

"""
texto = tk.Label(ventana,text="Hola")
texto.config(font=("Frozito",56), bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
texto.pack()
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

frame_top.pack_propagate(False)
frame_top.pack()
frame_down.pack()

entry_nombre = tk.Entry(ventana, fg="grey")
entry_nombre.insert(0,"Ingrese su nombre")
entry_nombre.pack()

tk.Button(ventana, text="Saludar", command=lambda: entry_nombre.delete(0,2)).pack()

text_info = tk.Text(ventana, height=10, width=100)
text_info.pack()

text_info.insert("1.0","Ingrese su texto...")

tk.Button(ventana, text="Texto", command=lambda: text_info.delete("1.0","1.5")).pack()

"""

barra_top = tk.Frame(ventana, width=400, height=50, bg="lightblue")
barra_izquierda = tk.Frame(ventana, width=50, height=400, bg="lightyellow")
frame_3 = tk.Frame(ventana, width=200, height=200, bg="red")
frame_4 = tk.Frame(ventana, width=200, height=200, bg="pink")


def mensaje_error():
    frame_3.pack_configure(anchor="center")



barra_top.pack_propagate(False)
barra_top.pack(anchor="nw")
barra_izquierda.pack(side="left")
frame_4.pack(side="bottom")
frame_3.pack(side="left", expand=True)
btn_nw = tk.Button(barra_top,text="NW", height=2, command=lambda: frame_3.pack_configure(anchor="nw")) 
btn_nw.pack(side="left", padx=5)
tk.Button(barra_top,text="N", height=2, command=lambda: frame_3.pack_configure(anchor="n")).pack(side="left", padx=5) 
tk.Button(barra_top,text="NE", height=2, command=lambda: frame_3.pack_configure(anchor="ne")).pack(side="left", padx=5) 
tk.Button(barra_top,text="E", height=2, command=lambda: frame_3.pack_configure(anchor="e")).pack(side="left", padx=5) 
tk.Button(barra_top,text="SE", height=2, command=lambda: frame_3.pack_configure(anchor="se")).pack(side="left", padx=5) 
tk.Button(barra_top,text="S", height=2, command=lambda: frame_3.pack_configure(anchor="s")).pack(side="left", padx=5) 
tk.Button(barra_top,text="SW", height=2, command=lambda: frame_3.pack_configure(anchor="sw")).pack(side="left", padx=5) 
tk.Button(barra_top,text="W", height=2, command=lambda: frame_3.pack_configure(anchor="w")).pack(side="left", padx=5) 
tk.Button(barra_top,text="CENTER", height=2, command=mensaje_error).pack(side="right", padx=5, ipadx=20) 

def salir(window: tk.Toplevel):
    if messagebox.askyesno("Salir", "quiere salir de esta ventana", icon="warning"):
        window.destroy()
    else:
        window.grab_release()

ventana_hija = tk.Toplevel(ventana)
ventana_hija.geometry("500x600")
ventana_hija.config(bg=COLOR_BACKGROUND)
ventana_hija.iconbitmap(IMAGE_ICON)
ventana_hija.grab_set()
ventana_hija.protocol("WM_DELETE_WINDOW", lambda: ventana_hija.destroy())

"""
btn_salir = tk.Button(ventana_hija,text="Salir", command=lambda: salir(ventana_hija), width=30, height=5)
btn_salir.pack(side="bottom", pady=20)


var = tk.StringVar(value="Blue")
var.trace_add("write", lambda a,b,c: ventana_hija.config(bg=var.get()))

btn_rosa = tk.Checkbutton(ventana_hija, text="Rosa", variable=var, onvalue="Rosita", offvalue="None")
btn_azul = tk.Checkbutton(ventana_hija, text="Azul", variable=var_2, onvalue="Azulcito", offvalue="None")
btn_rosa.pack(side="left", pady=5)
btn_azul.pack(side="left", pady=5)
img = tk.PhotoImage(file="./img/next.png")
btn_rosa = tk.Radiobutton(ventana_hija, variable=var, image=img, text="rosa", value="pink")
btn_azul = tk.Radiobutton(ventana_hija, variable=var, text="Azul", value="blue")
btn_rosa.pack(side="left")
btn_azul.pack(side="left")
tk.Radiobutton(ventana_hija, selectcolor="green").pack(side="left")

select = ttk.Combobox(ventana_hija, values=["Green","Blue","Black"], state="readonly", textvariable=var)
select.pack(side="left")

texto = tk.Label(ventana_hija, text=var.get())
texto.pack(side="bottom")

"""

tree = ttk.Treeview(ventana_hija)
tree.pack(side="top", fill="both", expand=True)

img = tk.PhotoImage(file="./img/next.png").subsample(3,3)

lista = [tree.insert("", tk.END,text=f"Archivo {x}", image=img) for x in range(5)]

lista_hija = [tree.insert(lista[0], tk.END,text=f"file_{x}.txt") for x in range(5)]



ventana.mainloop()
