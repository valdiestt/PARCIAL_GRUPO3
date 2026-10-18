class Publicacion:
    # Constructor: se ejecuta cuando creamos una nueva publicación
    # Recibe al autor y el contenido inicial de la publicación
    def __init__(self, autor, contenido):
        self._autor = autor
        self._contenido = contenido
        self._likes = []          # Almacena los usuarios que dieron like
        self._comentarios = []    # Almacena los comentarios
        self._compartidos = 0     # Contador, veces que se compartió

    # Define cómo se muestra la publicación cuando usamos print()
    def __str__(self):
        return (
            f"@{self._autor.obtener_nombre_usuario()}: "
            f"{self._contenido} | "
            f"Likes: {self.cantidad_likes()} | "
            f"Comentarios: {self.cantidad_comentarios()} | "
            f"Compartidos: {self._compartidos}"
        )

    # --- Encapsulamiento: métodos para consultar y modificar
    # los atributos de la publicación ---

    # Devuelve la información que guarda cada atributo de la publicación
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

    # Cambia el contenido solamente si se completa la validación
    def cambiar_contenido(self, nuevo_contenido):
        if not isinstance(nuevo_contenido, str) or not nuevo_contenido.strip():
            return False

        self._contenido = nuevo_contenido
        return True

    # --- Contadores ---
    # Devuelve cuántos usuarios dieron like, comentaron, compartieron
    # y la suma de interacciones
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
    
    # Evalua si una publicaión es viral
    def es_viral(self):
        return self.cantidad_interacciones() >= 1000

    # --- Acciones ---

    # Registra un like si el usuario todavía no lo ha dado
    def dar_like(self, usuario):
        if usuario in self._likes:
            return False

        self._likes.append(usuario)
        return True
    
    # Permite quitar el like de un usuario
    def quitar_like(self, usuario):
        if usuario not in self._likes:
            return False

        self._likes.remove(usuario)
        return True
    
    # Registra un comentario escrito por un usuario
    def comentar(self, usuario, texto):
        if not isinstance(texto, str) or not texto.strip():
            return False

        nombre = usuario.obtener_nombre_usuario()
        comentario = f"@{nombre}: {texto}"
        self._comentarios.append(comentario)
        return True

    # Contador de compartidos
    def compartir(self):
        self._compartidos += 1
        return self._compartidos

    # Conversión de la pubicación a un diccionario
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