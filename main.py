from manejador import Manejador 
from empleado import Empleado
import os
from PIL import Image

while True:
    while True:
        print("\n\n1. agregar", "2. eliminar", "3. mostrar empleados", "4. mostrar foto", "5. modificar", "6. sali", sep="\n")
        eleccion = input()
        if eleccion.isdigit():
            if  0 < int(eleccion)  and  int(eleccion) < 7:
                break
            else:
                print("elija una opcción correcta")
        else:
            print("Ingrese un valor numerico entre 1 y 6")

    if eleccion == "1":
        legajo = input("Legajo: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        puesto = input("Puesto: ")
        foto = input("Ruta de foto: ")

        empleado = Empleado(legajo, nombre, apellido, dni, puesto, foto)
        Manejador.crear(empleado)

    elif eleccion == "2":
        legajo = input("Usted esta por eliminar un Empleado\ningrese numero de Legajo:")
        Manejador.eliminar(legajo)

    elif eleccion == "3":
        Manejador.mostrar_empleados()
    elif eleccion == "4":
        legajo = input("Numero de legajo: ")
        if os.path.isdir(legajo):
            ruta = os.path.join(legajo, "img.jpg")
            if os.path.isfile( ruta ):
                with Image.open(ruta) as img:
                    img.show()
            else:
                print(" !! NO CONTIENE IMAGEN ESE EMPLEADO ¡¡ ")
        else:
            print("!! NO EXISTE ESE EMPLEADO ¡¡")
    elif eleccion == "5":
        legajo = input("Ingrese el empleado que quiere modificar: ")
        if os.path.isdir(legajo):
            print("Ingrese los datos a cambiar en cada campo si lo deja en blanco no seran modificados")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            puesto = input("Puesto: ")
            foto = input("Ruta de foto: ")
            
            Manejador.modificar(legajo, nombre, apellido, dni, puesto, foto)
        
    else:
        quit()
