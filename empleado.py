from datetime import datetime
from PIL import Image

class Empleado():
    def __init__(
                self,
                legajo : str,
                nombre : str,
                apellido : str,
                dni : int,
                puesto : str,
                foto : str,
                creado : datetime | None = datetime.now()
                ) -> None:
        self.__LEGAJO = legajo
        self.__CREADO = creado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__puesto = puesto
        self.__foto = foto
    
    def set_nombre(self, nombre : str):
        self.__nombre = nombre
    
    def set_apellido(self, apellido : str):
        self.__apellido = apellido
    
    def set_dni(self, dni : int):
        self.__dni = dni
    
    def set_puesto(self, puesto : str):
        self.__puesto = puesto
    
    def set_foto(self, ruta : str):
        self.__foto = ruta
    
    def mostrar_foto(self):
        with Image.open(self.__foto) as img:
            img.show()
    
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    
    def get_dni(self):
        return self.__dni
    
    def get_puesto(self):
        return self.__puesto
    
    def get_creado(self):
        return self.__CREADO
    
    def get_legajo(self):
        return self.__LEGAJO
    
    def get_foto(self):
        return self.__foto
    
    def info(self) -> dict:
        """retorna un diccionario con todas las variables

        Returns:
            dict: nombre de variable como clave y su valor
        """
        return {"nombre" : self.__nombre,
                "apellido" : self.__apellido,
                "dni" : self.__dni,
                "puesto" : self.__puesto,
                "creado" : self.__CREADO,
                "legajo" : self.__LEGAJO
                }