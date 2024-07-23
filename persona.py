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
        """Muestra un saludo y su nombre
        """
        print(f"Hola a todos. Soy {self._nombre}")
    
    def mostrar_edad(self) -> int:
        """devuelve una edad

        Returns:
            int: devuelve la edad
        """
        return self._edad

    def cambiar_nombre(self, nombre : str) -> str:
        """actualizar el nombre

        Args:
            nombre (str): Nuevo nombre a poner

        Returns:
            str: el nombre que fue cambiado
        """
        nombre_anterior = self._nombre
        self._nombre = nombre
        
        return nombre_anterior
        
