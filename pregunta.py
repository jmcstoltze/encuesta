
# Importaciones necesarias para su funcionamiento
from typing import List
from alternativa import Alternativa

# Se define la clase pregunta
class Pregunta():

    # Método constructor de la clase y sus atributos
    def __init__(self, enunciado: str, ayuda: str = "", requerida: bool = False, alternativas: List[dict] = []) -> None:
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas

    # Método accesador de los atributos
    @property
    def obtener_atributos(self) -> tuple:
        return self.enunciado, self.ayuda, self.requerida, self.alternativas
    
    
    # Métodos seteadores para los atributos
    @enunciado.setter
    def enunciado(self, enunciado: str) -> None:
        self.enunciado = enunciado

    @ayuda.setter
    def ayuda(self, ayuda: str) -> None:
        self.ayuda = ayuda

    @requerida.setter
    def requerida(self, requerida: bool) -> None:
        self.requerida = requerida

    # Aún no se define el mecanismo para modificar este atributo
    @alternativas.setter
    def alternativas(self, alternativas: List[dict]) -> None:
        pass
    
    # Método para mostrar pregunta, ayuda, alternativas y ayuda de las alternativas
    def mostrar_pregunta(self) -> None:

        # Obtiene los atributos de la instancia
        enunciado, ayuda, requerida, alternativas = self.obtener_atributos

        # Imprime el enunciado de la pregunta
        print(enunciado)

        # Si la pregunta tiene ayuda la imprime
        if ayuda != "":
            print(ayuda)
        
        # Imprime si es requerida o no (True or False)
        print(requerida)

        # Imprime las alternativas con ayuda (si la tienen)
        for alt in alternativas:
            contenido = alt['contenido']    # Primer valor del diccionario
            print(contenido)                # Lo imprime
            ayuda = alt['ayuda']            # Segundo valor del diccionario
            if ayuda:
                print(ayuda)                # Si no está en blanco lo imprime
