from datetime import datetime

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