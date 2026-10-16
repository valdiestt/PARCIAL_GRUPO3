class Usuario:
    # Atributo de clase
    red = "Instagram"

    # Reglas del plan gratis
    DURACION_HISTORIA = 24      # horas
    MAX_LISTAS_PUBLICO = 3
    MAX_FIJADAS = 3

    def __init__(self, nombre_usuario, nombre_completo, correo):
        self._nombre_usuario = nombre_usuario
        self._nombre_completo = nombre_completo
        self._correo = correo
        self._seguidores = []          # lista de Usuario
        self._seguidos = []            # lista de Usuario
        self._publicaciones = []       # lista de Publicacion
        self._historias = []           # historias publicadas
        self._historias_vistas = []    # historias de otros que yo vi
        self._vistas_por = []          # quiénes vieron mis historias
        self._listas_publico = []      # listas de público (máx 3)
        self._fijadas = []             # publicaciones fijadas (máx 3)
        self._icono = "default"
        self._tipografia = "default"

    def __str__(self):
        return (
            f"@{self._nombre_usuario} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )

    # --- Encapsulamiento ---
    def obtener_nombre_usuario(self):
        return self._nombre_usuario

    def obtener_nombre_completo(self):
        return self._nombre_completo

    def obtener_correo(self):
        return self._correo

    def cambiar_nombre_usuario(self, nuevo):
        if not nuevo:
            return False
        self._nombre_usuario = nuevo
        return True

    def cambiar_correo(self, nuevo):
        if not nuevo:
            return False
        self._correo = nuevo
        return True

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

    # --- Reglas ---
    def cantidad_seguidores(self):
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        return self.cantidad_seguidores() >= 1000

    def duracion_historia(self):
        return self.DURACION_HISTORIA

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

    # --- Acciones ---
    def seguir(self, otro):
        if otro is self:
            return False
        if otro in self._seguidos:
            return False
        self._seguidos.append(otro)
        otro._seguidores.append(self)
        return True

    def publicar_historia(self, contenido):
        self._historias.append(contenido)
        return contenido

    def ver_historia(self, otro):
        # Obligatorio: si veo la historia, aparezco en la lista de vistas
        if self in otro._vistas_por:
            return False
        otro._vistas_por.append(self)
        self._historias_vistas.append(otro)
        return True

    def crear_lista_publico(self, nombre):
        if len(self._listas_publico) >= self.MAX_LISTAS_PUBLICO:
            return False
        self._listas_publico.append(nombre)
        return True

    def fijar_publicacion(self, publicacion):
        if len(self._fijadas) >= self.MAX_FIJADAS:
            return False
        self._fijadas.append(publicacion)
        return True

    def cambiar_icono(self, nuevo):
        # Plan gratis: no permitido
        return False

    def cambiar_tipografia(self, nueva):
        # Plan gratis: no permitido
        return False

    def a_diccionario(self):
        return {
            "red": self.red,
            "tipo": "Usuario",
            "nombre_usuario": self._nombre_usuario,
            "nombre_completo": self._nombre_completo,
            "correo": self._correo,
            "seguidores": self.cantidad_seguidores(),
            "seguidos": self.cantidad_seguidos(),
            "publicaciones": self.cantidad_publicaciones(),
            "historias": len(self._historias),
            "duracion_historia": self.duracion_historia(),
            "listas_publico": len(self._listas_publico),
            "fijadas": len(self._fijadas),
            "puede_cambiar_icono": self.puede_cambiar_icono(),
            "puede_cambiar_tipografia": self.puede_cambiar_tipografia(),
            "es_influencer": self.es_influencer()
        }