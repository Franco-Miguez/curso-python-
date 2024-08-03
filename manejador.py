from empleado import Empleado
import os
import shutil

class Manejador():
    def crear(self, empleado : Empleado):
        """crea una carpeta con la informacion dentro

        Args:
            empleado (Empleado): el empleado a guardar
        """
        if os.path.exists(empleado.get_legajo()):
            print("Ese Empleado ya existe")
        else:
            os.mkdir(empleado.get_legajo())
            open( os.path.join( empleado.get_legajo(), "info.txt" ), "x" ).close()
            with open(os.path.join( empleado.get_legajo(), "info.txt" ), "w") as txt:
                txt.write(f"legajo={empleado.get_legajo()}\n")
                txt.write(f"nombre={empleado.get_nombre()}\n")
                txt.write(f"apellido={empleado.get_apellido()}\n")
                txt.write(f"dni={empleado.get_dni()}\n")
                txt.write(f"puesto={empleado.get_puesto()}\n")
                txt.write(f"foto={empleado.get_foto()}\n")
    
    def eliminar(self, legajo : str):
        """elimina la carpeta y lo que contine si el empleado existe

        Args:
            legajo (str): numero de lejago del empleado a eliminar
        """
        if os.path.isdir(legajo):
            shutil.rmtree(legajo)
        else:
            print("ese empleado no existe")

    def mostrar_empleados(self):
        for archivo in  os.listdir("."):
            if os.path.isdir(archivo) and archivo.isdigit():
                with open( os.path.join(archivo,"info.txt") ) as txt:
                    for linea in txt:
                        print(linea)

    def modificar(self, legajo : str,
                    nombre : str | None = "",
                    apellido : str | None = "",
                    dni : str | None = "",
                    puesto : str | None = "",
                    foto : str | None = "",
                    ):
        if os.path.isdir(legajo):
            info_nuevo = ""
            ruta = os.path.join(legajo,"info.txt")
            with open( ruta,) as txt:
                texto = txt.read().split("\n")
            
            info_nuevo += texto[0] + "\n"
            
            info_nuevo += f"nombre={nombre}\n" if nombre else f"{texto[1]}\n"
            info_nuevo += f"apellido={apellido}\n" if apellido else f"{texto[2]}\n"
            info_nuevo += f"dni={dni}\n" if dni else f"{texto[3]}\n"
            info_nuevo += f"puesto={puesto}\n" if puesto else f"{texto[4]}\n"
            info_nuevo += f"foto={foto}\n" if foto else f"{texto[5]}\n"
            
            with open(ruta, "w") as txt:
                txt.write(info_nuevo)


if __name__ == "__main__":
    mg = Manejador()
    
    empleado = Empleado("003", "Juan", "Calderon", 35684321,"Contador", "img.jpg")
    
    #mg.crear(empleado)
    #mg.eliminar("001")
    mg.modificar("002", nombre="Ana", foto="nueva.png")