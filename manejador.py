from empleado import Empleado
import os
import shutil

class Manejador():
    @classmethod
    def crear(cls, empleado : Empleado):
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
                txt.write(f"creado={empleado.get_creado()}\n")
                
    @classmethod
    def eliminar(cls, legajo : str):
        """elimina la carpeta y lo que contine si el empleado existe

        Args:
            legajo (str): numero de lejago del empleado a eliminar
        """
        if os.path.isdir(legajo):
            shutil.rmtree(legajo)
        else:
            print("ese empleado no existe")

    @classmethod
    def mostrar_empleados(cls):
        for archivo in  os.listdir("."):
            if os.path.isdir(archivo) and archivo.isdigit():
                with open( os.path.join(archivo,"info.txt") ) as txt:
                    info = txt.read()
                    info = info.split("\n") #separo por lineas
                    nuevo_txt = "\n" 
                    for linea in info:
                        if len(linea.split("=")) > 1:
                            nuevo_txt += f"{linea.split('=')[0]}:  {linea.split('=')[1]}\n" # divido la lenea en 2 uno es el nombre del dato y el otro el valor 
                    print(nuevo_txt)
                        

    @classmethod
    def modificar(cls, legajo : str,
                    nombre : str | None = "",
                    apellido : str | None = "",
                    dni : str | None = "",
                    puesto : str | None = "",
                    foto : str | None = "",
                    ):
        """actualiza la información si no se le pasa valor queda la anterior

        Args:
            legajo (str): empleado a modificar
            nombre (str | None, optional): nombre nuevo. Defaults to "".
            apellido (str | None, optional): apellido nuevo. Defaults to "".
            dni (str | None, optional): dni nuevo. Defaults to "".
            puesto (str | None, optional): puesto nuevo. Defaults to "".
            foto (str | None, optional): ruta nueva. Defaults to "".
        """
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
            info_nuevo += f"{texto[6]}\n"
            
            with open(ruta, "w") as txt:
                txt.write(info_nuevo)


if __name__ == "__main__":
    
    empleado = Empleado("003", "Juan", "Calderon", 35684321,"Contador", "img.jpg")
    
    Manejador.mostrar_empleados()