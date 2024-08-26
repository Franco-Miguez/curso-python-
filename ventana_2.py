import tkinter as tk
from PIL import Image
from PIL import ImageTk

COLOR_BACKGROUND = "#012538"
COLOR_TEXT = "#FFFFFF"

ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("800x600+300+50")
#ventana.resizable(0,0)
ventana.configure(bg=COLOR_BACKGROUND)

barra_top = tk.Frame(ventana, width=400, height=50, bg="lightblue")
barra_izquierda = tk.Frame(ventana, width=50, height=400, bg="lightyellow")

barra_top.place(relx=.3 , y=0)
barra_izquierda.place(x=0, y=100)

for num in range(4):
    tk.Button(barra_top,text="Boton").place(x=num*60,y=20) 


ventana.mainloop()