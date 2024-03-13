
from alternativa import Alternativa

# Se define la clase pregunta
class Pregunta():

    # Método constructor de la clase y sus atributos
    def __init__(self, enunciado: str, ayuda: str = "", requerida: bool = False, alternativas: list[Alternativa] = []) -> None:
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas

    # Método accesador de los atributos
    @property
    def obtener_atributos(self) -> tuple:
        return (self.enunciado, self.ayuda, self.requerida, self.alternativas)
    
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
    def alternativas(self, alternativas: list[dict]) -> None:
        
        # Se debiese implementar el llenado de esta lista en base a instancias de Alternativa
        # expresadas en diccionarios de dos claves y dso valores que se obtienenen
        # desde el método mostrar_alternativa()
        pass
    
    # Método para mostrar pregunta, ayuda, alternativas y ayuda de las alternativas
    def mostrar_pregunta(self) -> list[dict]:

        # Asigna los componentes de la pregunta
        enun = self.enunciado
        ayud = self.ayuda
        requ = self.requerida
        dict_alternativas = {}
        
        # Itera y asigna los componentes de las alternativas
        for alt in self.alternativas:
            contenido = alt['contenido']                  
            ayuda = alt['ayuda']            
            dict_alternativas['contenido'] = contenido
            dict_alternativas['ayuda'] = ayuda

        # Devuelve un diccionario con los componentes de la pregunta     
        return {
            'enunciado': enun,
            'ayuda': ayud,
            'requerida': requ,
            'alternativas': dict_alternativas
            }
