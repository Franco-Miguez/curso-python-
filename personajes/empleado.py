from persona import Persona

class Empleado(Persona):   
    def __init__(self, 
                legajo : str, 
                nombre : str, 
                edad : int, 
                sexo : bool, 
                dni : int, 
                trabaja : bool, 
                sueldo : float) -> None:
        super().__init__(sexo,nombre,edad,dni)
        self._legajo  = legajo
        self._trabaja = trabaja
        self._sueldo  = sueldo
        
    def mostrar_info(self) -> None:
        sexo_dato    = "Masculino" if self.sexo else "Femenino"
        estado       = "En Actividad" if self.trabaja else ">> INACTIVO <<"
        print(f"Nombre  : {self.nombre:20}\nEdad    : {self.edad:3}\nSexo    : {sexo_dato:12}\nDNI     : {self.dni:15}\nSueldo  : {self.sueldo:15}\nEstado  : {estado}\n\n")
        
    def mostrar_sueldo(self) -> float:
        return self.sueldo
    
    def subir_sueldo(self, porcentaje : float) -> None:
        self.sueldo *= 1 + (porcentaje/100)
        