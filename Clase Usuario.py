class Usuario:
    # Atributo de clase
    red = "Instagram"

    def __init__(self, nombre_usuario, nombre_completo, correo):
        self._nombre_usuario = nombre_usuario
        self._nombre_completo = nombre_completo
        self._correo = correo
        self._seguidores = []       # lista de Usuario
        self._seguidos = []         # lista de Usuario
        self._publicaciones = []    # lista de Publicacion

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

    # --- Reglas ---
    def cantidad_seguidores(self):
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        return self.cantidad_seguidores() >= 1000

    # --- Acciones ---
    def seguir(self, otro):
        if otro is self:
            return False
        if otro in self._seguidos:
            return False
        self._seguidos.append(otro)
        otro._seguidores.append(self)
        return True

    def publicar(self, contenido):
        p = Publicacion(self, contenido)
        self._publicaciones.append(p)
        return p

    def dar_like(self, publicacion):
        return publicacion.dar_like(self)

    def comentar(self, publicacion, texto):
        return publicacion.comentar(self, texto)

    def a_diccionario(self):
        return {
            "red": self.red,
            "nombre_usuario": self._nombre_usuario,
            "nombre_completo": self._nombre_completo,
            "correo": self._correo,
            "seguidores": self.cantidad_seguidores(),
            "seguidos": self.cantidad_seguidos(),
            "publicaciones": self.cantidad_publicaciones(),
            "es_influencer": self.es_influencer()
 