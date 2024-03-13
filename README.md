
# Encuestas Interactivas

Este proyecto consiste en una implementación básica de un sistema para la creación y gestión de encuestas interactivas. Permite definir encuestas con preguntas y alternativas, así como limitar el acceso a las mismas por edad o región.

## Contenido


- [Encuestas Interactivas](#encuestas-interactivas)
  - [Contenido](#contenido)
  - [Encuesta.py](#encuestapy)
  - [Usuario.py](#usuariopy)
  - [Pregunta.py](#preguntapy)
  - [ListadoRespuestas.py](#listadorespuestaspy)
  - [Alternativa.py](#alternativapy)
  - [Diagrama de Clases](#diagrama-de-clases)
  - [Uso](#uso)
  - [Autor](#autor)

## Encuesta.py

Este módulo contiene la implementación de las clases relacionadas con la creación y gestión de encuestas.
La clase `Encuesta` es una clase abstracta que define la estructura básica de una encuesta. Contiene métodos para mostrar la encuesta y agregar un listado de respuestas.
La clase `EncuestaLimitadaPorEdad`  hereda de `Encuesta` y agrega funcionalidades relacionadas con limitar la encuesta por edad.
La clase `EncuestaLimitadaPorRegion` hereda de `Encuesta` y agrega funcionalidades relacionadas con limitar la encuesta por región.

## Usuario.py

Este módulo contiene la implementación de la clase `Usuario`, que representa a un usuario que responde una encuesta.
La clase `Usuario` representa a un usuario que responde una encuesta.

## Pregunta.py

Este módulo contiene la implementación de la clase `Pregunta`, que representa una pregunta dentro de una encuesta.
La clase `Pregunta` representa una pregunta dentro de una encuesta.

## ListadoRespuestas.py

Este módulo contiene la implementación de la clase `ListadoRespuestas`, que representa un listado de respuestas de un usuario.
La clase `ListadoRespuestas` representa un listado de respuestas de un usuario.

## Alternativa.py

Este módulo contiene la implementación de la clase `Alternativa`, que representa una alternativa de respuesta para una pregunta.
La clase `Alternativa` representa una alternativa de respuesta para una pregunta.

## Diagrama de Clases

Adjunto se encuentra el diagrama de clases en formato PNG que ilustra las relaciones entre las clases implementadas.

## Uso

Este proyecto aún se encuentra en desarrollo y no tiene una funcionalidad completa.

## Autor

Jose Contreras Stoltze
