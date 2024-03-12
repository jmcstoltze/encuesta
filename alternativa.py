
# Se define clase alternativa
class Alternativa():

    # Método constructor con sus atributos
    def __init__(self, contenido: str, ayuda: str = "") -> None:
        self.contenido = contenido
        self.ayuda = ayuda

    # Mecanismo para mostrar sus atributos en forma de tupla
    @property
    def obtener_atributos(self) -> dict:
        
        # Devuelve un diccionario con los atributos
        return {"contenido": self.contenido, "ayuda": self.ayuda}
    
    # Método accesador de su contenido
    @property
    def obtener_contenido(self) -> str:
        return self.contenido

    # Método accesador de su ayuda
    @property
    def obtener_ayuda(self) -> str:
        return self.ayuda
    
    # Método mutador para atributo contenido
    @contenido.setter
    def contenido(self, contenido: str) -> None:
        self.contenido = contenido

    # Método mutador para atributo ayuda
    @ayuda.setter
    def ayuda(self, ayuda: str) -> None:
        self.ayuda = ayuda
