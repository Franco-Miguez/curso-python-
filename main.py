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

class Persona():
    def __init__(
                self,
                sexo : bool,
                nombre : str | None = "Sin nombre" ,
                edad : int | None = 0
                ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def saludar(self) -> None:
        print(f"Hola a todos. Soy {self.nombre}")
    
    def mostrar_edad(self) -> int:
        return self.edad

{"001": "Nombre"}

class Empleado():
    def __init__(self, 
             legajo : str, 
             nombre : str, 
             edad : int, 
             sexo : bool, 
             dni : int, 
             trabaja : bool, 
             sueldo : float) -> None:
        self.legajo  = legajo
        self.nombre  = nombre
        self.edad    = edad
        self.sexo    = sexo
        self.dni     = dni
        self.trabaja = trabaja
        self.sueldo  = sueldo
        
    def mostrar_info(self) -> None:
        sexo_dato    = "Masculino" if self.sexo else "Femenino"
        estado       = "En Actividad" if self.trabaja else ">> INACTIVO <<"
        print(f"Nombre  : {self.nombre:20}\nEdad    : {self.edad:3}\nSexo    : {sexo_dato:12}\nDNI     : {self.dni:15}\nSueldo  : {self.sueldo:15}\nEstado  : {estado}\n\n")
        
    def mostrar_sueldo(self) -> float:
        return self.sueldo
    
    def subir_sueldo(self, porcentaje : float) -> None:
        self.sueldo *= 1 + (porcentaje/100)

m = Empleado("001","Juan",15,True,156546546,True,200)

print(m.mostrar_info())
m.subir_sueldo(20)
print(m.mostrar_info())