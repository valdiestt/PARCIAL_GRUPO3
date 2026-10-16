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

