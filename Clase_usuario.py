from publicacion import Publicacion

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
        
        # --- NUEVOS ATRIBUTOS DE INCIDENCIAS ---
        self._verificado = False
        self._reportado = False

    def __str__(self):
        # Le agregamos el check visual si está verificado
        verif = "✅" if self._verificado else ""
        return (
            f"@{self._nombre_usuario}{verif} | "
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

    # --- Nuevas acciones para INCIDENCIAS ---
    def verificar_cuenta(self):
        self._verificado = True
        
    def reportar_cuenta(self):
        self._reportado = True
        
    def esta_verificado(self):
        return self._verificado
        
    def esta_reportado(self):
        return self._reportado

    # --- Diccionario Actualizado ---
    def a_diccionario(self):
        return {
            "red": self.red,
            "nombre_usuario": self._nombre_usuario,
            "nombre_completo": self._nombre_completo,
            "correo": self._correo,
            "seguidores": self.cantidad_seguidores(),
            "seguidos": self.cantidad_seguidos(),
            "publicaciones": self.cantidad_publicaciones(),
            "es_influencer": self.es_influencer(),
            "verificado": self._verificado,
            "reportado": self._reportado
        }