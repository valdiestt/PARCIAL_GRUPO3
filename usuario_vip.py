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