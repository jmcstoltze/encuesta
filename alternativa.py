
# Se define clase alternativa
class Alternativa():

    # Método constructor con sus atributos
    def __init__(self, contenido: str, ayuda: str = "") -> None:
        self.contenido = contenido
        self.ayuda = ayuda

    # Mecanismo para mostrar una alternativa
    @property
    def obtener_atributos(self) -> tuple:
        
        # Devuelve una tupla con los atributos
        return self.contenido, self.ayuda
    
    # Método mutador para atributo contenido
    @contenido.setter
    def contenido(self, contenido: str) -> None:
        self.contenido = contenido

    # Método mutador para atributo ayuda
    @contenido.ayuda
    def ayuda(self, ayuda: str) -> None:
        self.ayuda = ayuda
