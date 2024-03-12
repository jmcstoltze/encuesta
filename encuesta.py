
# Importaciones necesarias para la implementación
from abc import ABC, abstractmethod

# Se define la clase Encuesta
class Encuesta(ABC):

    # Método constructor de la clase con parámetro y atributos
    def __init__(self, listado_preguntas: list[dict]) -> None:
        self.nombre = ""
        self.listado_preguntas = listado_preguntas
        self.listado_respuestas = ""

    # Sólo el nombre puede consultarse y modificarse libremente
    # Accesador del atributo nombre
    @property
    def obtener_nombre(self) -> str:
        return self.nombre

    # Mutador del atributo nombre
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.nombre = nombre

    # Método para mostrar la encuesta
    def mostrar_encuesta(self) -> None:

        # Imprime su nombre
        print(self.nombre)

        # Itera el listado de preguntas e imprime invocando al método correspondiente
        for pregunta in self.listado_preguntas:
            print(pregunta.mostrar_pregunta())

    # Método abstracto para agregar un listado de respuestas a la lista
    @abstractmethod
    def agregar_listado_respuestas(self) -> None:
        pass

# Define la clase encuesta limitada por edad
class EncuestaLimitidaPorEdad(Encuesta):

    # Método constructor de la clase y sus atributos
    def __init__(self, listado_preguntas: list[dict], edad_minima: int, edad_maxima: int) -> None:

        # Invoca al constructor de la clase de la cual hereda
        super().__init__(self, listado_preguntas)

        # Edad mínima y máxima para responder la encuesta
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima       
    
    # Método para agregar un listado de respuestas a la encuesta por parte del usuario
    def agregar_listado_respuestas(self, edad_usuario: int, listado_respuestas ) -> None:
        
        #if edad_usuario in range [self.edad_minima, self.edad_maxima]:
        # Por implementar
        pass

# Se define la clase encuesta limitada por región
class EncuestaLimitadadPorRegion(Encuesta):

    # Método constructor de la clase con parámetros y atributos
    def __init__(self, listado_preguntas: list[dict], listado_regiones: list[int]) -> None:

        # Se invoca al constructor de la clase de la cual hereda
        super().__init__(self, listado_preguntas)

        # Establece el listado de regiones que obtienes desde regiones.py
        self.listado_regiones = listado_regiones

    # Método setter del listado de regiones (modificable aunque no se especifica)
    @listado_regiones.setter
    def listado_regiones(self, nuevo_listado_regiones) -> None:
        self.listado_regiones = nuevo_listado_regiones

    # Método para agregar un listado de respuestas por parte del usuario
    def agregar_listado_respuestas(self, region_usuario: int, listado_respuestas) -> None:
        # Se debe implementar que el usuario pertenezca a la region establecida para la encuesta
        # if region_usuario in listado_regiones:
        pass
