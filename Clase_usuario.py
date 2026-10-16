class Usuario:
    # Atributo de clase: compartido por TODAS las instancias
    # (todos los usuarios pertenecen a Instagram)
    red = "Instagram"

    # Reglas del plan gratis (constantes de clase)
    DURACION_HISTORIA = 24      # horas que dura una historia en el plan gratis
    MAX_LISTAS_PUBLICO = 3      # máximo de listas de público permitidas
    MAX_FIJADAS = 3             # máximo de publicaciones fijadas permitidas

    def __init__(self, nombre_usuario, nombre_completo, correo):
        # Atributos de instancia (encapsulados con _)
        self._nombre_usuario = nombre_usuario       # @usuario
        self._nombre_completo = nombre_completo     # nombre real
        self._correo = correo                       # correo electrónico

        # Listas que representan las RELACIONES del usuario
        self._seguidores = []          # lista de objetos Usuario que me siguen
        self._seguidos = []            # lista de objetos Usuario que yo sigo
        self._publicaciones = []       # lista de objetos Publicacion que he creado

        # Historias
        self._historias = []           # historias que yo publiqué
        self._historias_vistas = []    # historias de otros que yo vi
        self._vistas_por = []          # quiénes vieron mis historias

        # Listas de público y fijadas
        self._listas_publico = []      # nombres de las listas (máx 3)
        self._fijadas = []             # publicaciones fijadas (máx 3)

        # Personalización del perfil (por defecto no se pueden cambiar en el plan gratis)
        self._icono = "default"
        self._tipografia = "default"

    def __str__(self):
        # Método especial que define cómo se imprime el objeto con print()
        return (
            f"@{self._nombre_usuario} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )

    # ---------------------------------------------------------
    # ENCAPSULAMIENTO: métodos para leer (obtener) y modificar (cambiar)
    # los atributos privados. Nunca accedemos directamente a _atributo
    # desde fuera de la clase.
    # ---------------------------------------------------------

    def obtener_nombre_usuario(self):
        return self._nombre_usuario

    def obtener_nombre_completo(self):
        return self._nombre_completo

    def obtener_correo(self):
        return self._correo

    def cambiar_nombre_usuario(self, nuevo):
        # Validación: no permitir vacío
        if not nuevo:
            return False
        self._nombre_usuario = nuevo
        return True

    def cambiar_correo(self, nuevo):
        # Validación: no permitir vacío
        if not nuevo:
            return False
        self._correo = nuevo
        return True

    # --- Getters de las listas ---
    # Devolvemos la lista directamente para poder modificarla desde fuera
    # (por ejemplo, para añadir publicaciones creadas en main.py)
    def obtener_seguidores(self):
        return self._seguidores

    def obtener_seguidos(self):
        return self._seguidos

    def obtener_publicaciones(self):
        return self._publicaciones

    def obtener_historias(self):
        return self._historias

    def obtener_historias_vistas(self):
        return self._historias_vistas

    def obtener_vistas_por(self):
        return self._vistas_por

    def obtener_listas_publico(self):
        return self._listas_publico

    def obtener_fijadas(self):
        return self._fijadas

    def obtener_icono(self):
        return self._icono

    def obtener_tipografia(self):
        return self._tipografia

    # ---------------------------------------------------------
    # REGLAS: métodos que devuelven True/False según alguna condición
    # del usuario. Son "consultas", no modifican nada.
    # ---------------------------------------------------------

    def cantidad_seguidores(self):
        # len() sobre la lista _seguidores
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        # Regla: tiene 1000 seguidores o más
        return self.cantidad_seguidores() >= 1000

    def duracion_historia(self):
        # Devuelve la duración según el atributo de clase
        # En Usuario normal = 24, en UsuarioVip se sobrescribe a 48
        return self.DURACION_HISTORIA

    # --- Reglas de permisos (en Usuario normal son todos False) ---
    # En UsuarioVip se sobrescriben para devolver True

    def puede_ver_discreto(self):
        return False

    def puede_supercorazon(self):
        return False

    def puede_spotlight(self):
        return False

    def puede_cambiar_icono(self):
        return False

    def puede_cambiar_tipografia(self):
        return False

    # ---------------------------------------------------------
    # ACCIONES: métodos que modifican el estado del objeto o de otro
    # ---------------------------------------------------------

    def seguir(self, otro):
        # No puedes seguirte a ti mismo
        if otro is self:
            return False
        # No puedes seguir dos veces a la misma persona
        if otro in self._seguidos:
            return False

        # Añadir a mi lista de seguidos
        self._seguidos.append(otro)
        # Añadirme a la lista de seguidores del otro (relación bidireccional)
        otro._seguidores.append(self)
        return True

    def publicar_historia(self, contenido):
        # Guarda el contenido en la lista de historias propias
        self._historias.append(contenido)
        return contenido

    def ver_historia(self, otro):
        # Regla obligatoria: si veo una historia, APAREZCO en la lista de vistas
        # Si ya la vi, no hago nada
        if self in otro._vistas_por:
            return False
        # Registro la visita en el otro usuario
        otro._vistas_por.append(self)
        # Guardo en mi historial que vi esa historia
        self._historias_vistas.append(otro)
        return True

    def crear_lista_publico(self, nombre):
        # Validar que no exceda el máximo del plan gratis (3)
        if len(self._listas_publico) >= self.MAX_LISTAS_PUBLICO:
            return False
        self._listas_publico.append(nombre)
        return True

    def fijar_publicacion(self, publicacion):
        # Validar que no exceda el máximo del plan gratis (3)
        if len(self._fijadas) >= self.MAX_FIJADAS:
            return False
        self._fijadas.append(publicacion)
        return True

    def cambiar_icono(self, nuevo):
        # Plan gratis: NO puede cambiar el ícono
        return False

    def cambiar_tipografia(self, nueva):
        # Plan gratis: NO puede cambiar la tipografía
        return False
