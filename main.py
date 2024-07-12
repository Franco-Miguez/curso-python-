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

"""