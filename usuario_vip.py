from Clase_usuario import Usuario 


# =====================================================================
# USUARIO VIP
# =====================================================================
class UsuarioVip(Usuario):
    """Representa un usuario con suscripción Instagram Plus."""

    # Beneficios exclusivos de Instagram Plus
    DURACION_HISTORIA = 48
    MAX_FIJADAS = 6

    def __init__(self, nombre_usuario, nombre_completo,
                 correo, insignia="💎 Instagram Plus"):

        # Inicializar atributos heredados de Usuario
        super().__init__(
            nombre_usuario,
            nombre_completo,
            correo
        )


    # --- Permisos exclusivos de Instagram Plus ---

    def puede_ver_discreto(self):
        """Permite ver historias sin aparecer en las vistas."""
        return self._beneficios_activos

    def puede_supercorazon(self):
        """Verifica si puede enviar supercorazones."""
        return self._beneficios_activos

    def puede_spotlight(self):
        """Verifica si puede destacar historias."""
        return self._beneficios_activos

    def puede_cambiar_icono(self):
        """Verifica si puede personalizar el icono."""
        return self._beneficios_activos

    def puede_cambiar_tipografia(self):
        """Verifica si puede personalizar la tipografia."""
        return self._beneficios_activos


    # --- Personalización exclusiva de Instagram Plus ---

    def cambiar_icono(self, nuevo):
        """Permite cambiar el icono si tiene Instagram Plus activo."""

        if not self.puede_cambiar_icono():
            return False

        if not isinstance(nuevo, str) or not nuevo.strip():
            return False

        self._icono = nuevo.strip()
        return True

    def cambiar_tipografia(self, nueva):
        """Permite cambiar la tipografia del perfil."""

        if not self.puede_cambiar_tipografia():
            return False

        if not isinstance(nueva, str) or not nueva.strip():
            return False

        self._tipografia = nueva.strip()
        return True

    # --- Visualización discreta de historias ---

    def ver_historia(self, otro):
        """Permite ver historias sin aparecer en las visualizaciones."""

        # Validar que sea otro usuario
        if not isinstance(otro, Usuario) or otro is self:
            return False

        # Evitar registrar dos veces al mismo usuario
        if otro in self._historias_vistas:
            return False

        # Si tiene Instagram Plus, puede ver discretamente
        if self.puede_ver_discreto():
            self._historias_vistas.append(otro)
            return True

        # Si no tiene Plus activo, usa el método normal
        return super().ver_historia(otro)

    # --- Historias Spotlight ---

    def destacar_historia(self, historia):
        """Marca una historia propia como Spotlight."""

        if not self.puede_spotlight():
            return False

        # La historia debe pertenecer al usuario
        if historia not in self._historias:
            return False

        # Evitar historias destacadas repetidas
        if historia in self._historias_spotlight:
            return False

        self._historias_spotlight.append(historia)
        return True

    def obtener_historias_spotlight(self):
        """Devuelve las historias marcadas como Spotlight."""
        return self._historias_spotlight.copy()

    # --- Supercorazones Instagram Plus ---

    def enviar_supercorazon(self, otro, historia):
        """Envia un supercorazon a una historia existente."""

        if not self.puede_supercorazon():
            return False

        # Validar destinatario
        if not isinstance(otro, Usuario) or otro is self:
            return False

        # Verificar que la historia exista
        if historia not in otro.obtener_historias():
            return False

        registro = (otro, historia)

        # Evitar enviar dos veces a la misma historia
        if registro in self._supercorazones_enviados:
            return False

        self._supercorazones_enviados.append(registro)
        return True

    def obtener_supercorazones_enviados(self):
        """Consulta los supercorazones enviados."""

        return [
            (usuario.obtener_nombre_usuario(), historia)
            for usuario, historia in self._supercorazones_enviados
        ]

    # --- Listas de publico Instagram Plus ---

    def crear_lista_publico(self, nombre):
        """Permite crear listas sin limite con Plus activo."""

        # Validar el nombre
        if not isinstance(nombre, str) or not nombre.strip():
            return False

        nombre = nombre.strip()

        # Evitar nombres duplicados
        if nombre in self._listas_publico:
            return False

        # Los usuarios Plus no tienen limite de listas
        if self._beneficios_activos:
            self._listas_publico.append(nombre)
            return True

        # Sin Plus se aplica el limite del usuario normal
        return super().crear_lista_publico(nombre)


    # --- Validaciones de limites Instagram Plus ---

    def establecer_estado_plus(self, activo):
        """Actualiza el estado de la suscripcion Plus."""

        if not isinstance(activo, bool):
            return False

        self._beneficios_activos = activo
        return True

    def duracion_historia(self):
        """Devuelve la duracion segun la suscripcion."""

        if self._beneficios_activos:
            return self.DURACION_HISTORIA

        return Usuario.DURACION_HISTORIA

    def limite_fijadas(self):
        """Devuelve el limite de publicaciones fijadas."""

        if self._beneficios_activos:
            return self.MAX_FIJADAS

        return Usuario.MAX_FIJADAS

    def fijar_publicacion(self, publicacion):
        """Aplica el limite de fijadas segun el plan."""

        if len(self._fijadas) >= self.limite_fijadas():
            return False

        return super().fijar_publicacion(publicacion)
