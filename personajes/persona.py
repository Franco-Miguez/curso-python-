class Persona():
    def __init__(
                self,
                sexo : bool,
                dni : int,
                nombre : str | None = "Sin nombre" ,
                edad : int | None = 0
                ) -> None:
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._dni = dni
    
    def saludar(self) -> None:
        print(f"Hola a todos. Soy {self._nombre}")
    
    def mostrar_edad(self) -> int:
        return self._edad
