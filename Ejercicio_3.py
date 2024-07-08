empleados = {
                "001" : ("Juan", 25, True, 48565285, True),
                "002" : ("Ana", 32, False, 345868565, True),
                "003" : ("Charly", 75, True, 20356489, False)
            }

id = input("ID: ")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
sexo = input("Sexo: ")
sexo = True if sexo == "Masculino" else False
dni = int(input("DNI: "))
trabaja = bool( input("Trabaja 0 (no) 1 (si)") )

empleado_nuevo = { id : (nombre, edad, sexo, dni, trabaja) }


empleados.update( empleado_nuevo )

print(empleados)
