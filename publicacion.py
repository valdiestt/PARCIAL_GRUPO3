class Publicacion:
    def __init__(self, autor, contenido):
        self._autor = autor
        self._contenido = contenido
        self._likes = []
        self._comentarios = []
        self._compartidos = 0

    def __str__(self):
        return (
            f"@{self._autor.obtener_nombre_usuario()}: "
            f"{self._contenido} | "
            f"Likes: {self.cantidad_likes()} | "
            f"Comentarios: {self.cantidad_comentarios()} | "
            f"Compartidos: {self._compartidos}"
        )

    # --- Encapsulamiento ---
    def obtener_autor(self):
        return self._autor

    def obtener_contenido(self):
        return self._contenido

    def obtener_likes(self):
        return self._likes

    def obtener_comentarios(self):
        return self._comentarios

    def obtener_compartidos(self):
        return self._compartidos

    def cambiar_contenido(self, nuevo_contenido):
        if not isinstance(nuevo_contenido, str) or not nuevo_contenido.strip():
            return False

        self._contenido = nuevo_contenido
        return True

    # --- Reglas y contadores ---
    def cantidad_likes(self):
        return len(self._likes)

    def cantidad_comentarios(self):
        return len(self._comentarios)

    def cantidad_compartidos(self):
        return self._compartidos

    def cantidad_interacciones(self):
        return (
            self.cantidad_likes()
            + self.cantidad_comentarios()
            + self.cantidad_compartidos()
        )

    def es_viral(self):
        return self.cantidad_interacciones() >= 1000

    # --- Acciones ---
    def dar_like(self, usuario):
        if usuario in self._likes:
            return False

        self._likes.append(usuario)
        return True

    def quitar_like(self, usuario):
        if usuario not in self._likes:
            return False

        self._likes.remove(usuario)
        return True

    def comentar(self, usuario, texto):
        if not isinstance(texto, str) or not texto.strip():
            return False

        nombre = usuario.obtener_nombre_usuario()
        comentario = f"@{nombre}: {texto}"
        self._comentarios.append(comentario)
        return True

    def compartir(self):
        self._compartidos += 1
        return self._compartidos

    def a_diccionario(self):
        return {
            "autor": self._autor.obtener_nombre_usuario(),
            "contenido": self._contenido,
            "likes": [
                usuario.obtener_nombre_usuario()
                for usuario in self._likes
            ],
            "comentarios": self._comentarios.copy(),
            "compartidos": self._compartidos,
            "interacciones": self.cantidad_interacciones(),
            "es_viral": self.es_viral()
        }