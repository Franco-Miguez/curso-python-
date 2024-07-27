import PIL.Image
from persona import Persona
from PIL import Image
"""
nombres = []

nombres.append(input("Ingrese un nombre: "))

user = input("Usuario: ")
password = input("Contraseña: ")

while password != "1234" or user != "Pepe":
    print("La contraseña y el usuario no estan")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    
print("Genial estas dentro")
"""
"""
nombres = ["Juan", "Pedro", "Charly", "Fede"]

print("Nombres de Jugadores:")
for i in range(4):
    print(f"\t* {i + 1}. {nombres[i]}")
    if i == 2: break
else:
    print("Termino")
    
user = input("Usuario: ")
password = input("Contraseña: ")

for i in range(3):
    if password != "1234" or user != "Pepe":
        print("La contraseña y el usuario no estan")
        user = input("Usuario: ")
        password = input("Contraseña: ")
    else:
        break
else:
    print("Te quedaste sin intentos")
    quit()
    
print("Genial estas dentro")


for numero in range(5):
    letra = input("Ingrese una letra: ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        continue
    print("#####\tLetra incorrecta\t#####")




while True:
    celular = input("ingrese su celular: ")
    if celular.isdigit():
        celular = int(celular)
        print("Genial fue guardado!!")
        break
    else:
        if celular.find(" ") != -1:
            print("No ingrese espacios")
        elif celular.find("-") != -1:
            print("No ingrese -")
        print("Ingrese solo numeros")


def saludar(*nombres : str,
            apellido_familiar : str | None = ""
            ):
    for nombre in nombres:
        print(f"Hola {nombre} {apellido_familiar}")

def saludar_empleados(nombres : list [str] ) -> None: 
    for i in range(len(nombres)):
        nombres[i] = nombres[i].capitalize()
        print(f"Hola {nombres[i]}")

#saludar("Juan","Nacho","Pedro", apellido_familiar="Calderon")
def saludar_empleado(**empleado):
    for i in empleado:
        print(f"{i.capitalize()}: {empleado.get(i)}")

def sumar(*numeros :  int) -> int:
    #global resultado
    for i in numeros:
        try:
            if type(i) == int or type(i) == float:
                resultado += i
            else:
                resultado += int(i)
        except ValueError:
            print(f"el valor {i} no es un numero")
    return resultado


resultado = 0


#print( sumar(5,6, "ABC",8,"3") )

while True:
    try:
        numero = int( input("Ingrese numero: ") )
    except ValueError:

        print("A ingresado un valor incorrecto")
    else:
        numero **= 2
        break
    finally:
        print("#"*8, "Fin", "#"*8)

print("Fin del programa")



def nombres(*nombres : str):
    for nombre in nombres:
        if not nombre.isalpha():
            raise NameError(f"Ingreso un nombre con caracteres especiales {nombre}")
    
    print(*nombres)
        

nombres("Juan", "Pedro", "@Eric", "Ana")

"""

#empleado = Empleado("001","Juan",15,True,156546546,True,200)

class Inventario():
    sucursales = 2
    def __init__(self, productos : int) -> None:
        self._productos = productos
    
    @classmethod
    def sumar_sucursal(cls) -> None:
        cls.sucursales += 1 

p = Persona(True, 415681526, "juan", 15)


with open("user.txt", "r") as archivo:
    for linea in archivo:
        print(linea)

img = Image.open("nuevo.jpeg")

img.show()


