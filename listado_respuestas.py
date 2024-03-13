
# Importaciones necesarias desde usuario
from usuario import Usuario

# Define la clase Respuestas
class ListadoRespuestas():

    def __init__(self, usuario: Usuario) -> None:

        # Atributos de la instancia de la clase
        self.usuario = usuario
        self.listado_respuestas = []    # Listado de respuestas con números enteros

    # Métodos getter para los atributos de la clase
    @property
    def obtener_usuario(self) -> Usuario:
        return self.usuario
    
    @property
    def obtener_listado_respuestas(self) -> list[int]:
        return self.listado_respuestas
    
    # Métodos setter para los atributos de la clase
    @usuario.setter
    def usuario(self, nuevo_usuario: Usuario) -> None:
        self.usuario = nuevo_usuario

    @listado_respuestas.setter
    def listado_respuestas(self, nuevo_listado_respuestas: list[int]) -> None:
        self.listado_respuestas = nuevo_listado_respuestas
        