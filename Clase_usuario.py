class Usuario:
    # =====================================================================
    # ATRIBUTOS DE CLASE
    # =====================================================================
    # Reglas del plan gratis (constantes)
    DURACION_HISTORIA = 24      # horas que dura una historia en el plan gratis
    MAX_LISTAS_PUBLICO = 3      # máximo de listas de público permitidas
    MAX_FIJADAS = 3             # máximo de publicaciones fijadas permitidas

    def __init__(self, nombre_usuario, nombre_completo, correo):
        # Constructor de la clase Usuario.
        # Inicializa los atributos de instancia encapsulados y las listas de relaciones.
        
        # --- Atributos de instancia (encapsulados con _) ---
        self._nombre_usuario = nombre_usuario       # @usuario
        self._nombre_completo = nombre_completo     # nombre real
        self._correo = correo                       # correo electrónico

        # --- Relaciones simples (Listas) ---
        self._seguidores = []          # Lista de objetos Usuario que me siguen
        self._seguidos = []            # Lista de objetos Usuario que yo sigo
        self._publicaciones = []       # Lista de objetos Publicacion que he creado

        # --- Atributos necesarios para la conversión VIP/Normal en el menú ---
        self._historias = []           
        self._historias_vistas = []    
        self._vistas_por = []          
        self._listas_publico = []      
        self._fijadas = []             

        # --- Personalización (Bloqueado en plan gratis) ---
        self._icono = "default"
        self._tipografia = "default"

    def __str__(self):
        # Retorna un resumen rápido del perfil al usar print().
        return (
            f"@{self._nombre_usuario} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )

    # =====================================================================
    # ENCAPSULAMIENTO: Getters (Métodos de acceso)
    # =====================================================================
    def obtener_nombre_usuario(self):
        return self._nombre_usuario

    def obtener_nombre_completo(self):
        return self._nombre_completo

    def obtener_correo(self):
        return self._correo

    # --- Getters de las listas de relaciones ---
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

    # =====================================================================
    # REGLAS Y CONSULTAS: Métodos que devuelven información sin modificar
    # =====================================================================
    def cantidad_seguidores(self):
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        # Regla de negocio: Es influencer si tiene 1000 o más seguidores.
        return self.cantidad_seguidores() >= 1000

    def duracion_historia(self):
        # Devuelve la duración de la historia según el atributo de clase.
        return self.DURACION_HISTORIA

    # --- Permisos base ---
    def puede_cambiar_icono(self):
        return False

    def puede_cambiar_tipografia(self):
        return False

    # =====================================================================
    # ACCIONES: Métodos que modifican el estado
    # =====================================================================

    def seguir(self, otro):
        # Permite seguir a otro usuario.
        # Relación simple: Añade a 'otro' en mis seguidos y me añade a mí en sus seguidores.
        if not isinstance(otro, Usuario) or otro is self:
            return False  # No puede seguirse a sí mismo ni a objetos inválidos
        
        if otro in self._seguidos:
            return False  # Ya lo sigue

        self._seguidos.append(otro)
        otro._seguidores.append(self)
        return True

    def dejar_de_seguir(self, otro):
        # Permite dejar de seguir a un usuario.
        if otro not in self._seguidos:
            return False  # No lo sigue

        self._seguidos.remove(otro)
        if self in otro._seguidores:
            otro._seguidores.remove(self)
        return True

    def agregar_publicacion(self, publicacion):
        # Método formal para agregar publicaciones.
        if publicacion not in self._publicaciones:
            self._publicaciones.append(publicacion)
            return True
        return False

    def fijar_publicacion(self, publicacion):
        # Valida que no se exceda el máximo de fijadas del plan gratis (3)
        if len(self._fijadas) >= self.MAX_FIJADAS:
            return False
        self._fijadas.append(publicacion)
        return True

    # --- Personalización (Bloqueado en plan gratis) ---
    def cambiar_icono(self, nuevo):
        # En el plan gratis, no se permite cambiar el ícono.
        return False

    def cambiar_tipografia(self, nueva):
        # En el plan gratis, no se permite cambiar la tipografía.
        return False