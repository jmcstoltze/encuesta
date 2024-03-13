
# Se importa la clase Encuesta
from encuesta import Encuesta

# Define la clase usuario
class Usuario():

    # Método constructor de la clase y sus parámetros
    def __init__(self, correo: str, edad: int, region: int) -> None:

        self.correo = correo
        self.edad = edad
        self.region = region

    # Métodos getter para los tres parámetros
    @property
    def obtener_correo(self) -> str:
        return self.correo
    
    @property
    def obtener_edad(self) -> str:
        return self.edad
    
    @property
    def obtener_region(self) -> str:
        return self.region
    
    # Métodos setter para los tres parámetros
    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        self.correo = nuevo_correo

    @edad.setter
    def edad(self, nueva_edad: str) -> None:
        self.edad = nueva_edad

    @region.setter
    def region(self, nueva_region: str) -> None:
        self.region = nueva_region
    
    # Método para contestar la encuesta que recibe 
    def contestar_encuesta(self, encuesta: Encuesta) -> list[int]:
        
        # Se debe implementar el comportamiento del método y como se llena la lista que retorna
        # Un listado de respuestas sólo puede existir como parte de una encuesta.

        listado_respuestas = []

        # Lógica para el llenado de la lista
        return listado_respuestas
    