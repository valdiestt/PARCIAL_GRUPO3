from Clase_usuario import Usuario 


# =====================================================================
# USUARIO VIP
# =====================================================================
class UsuarioVip(Usuario):
    def __init__(self, id_usuario, nombre, email, insignia="⭐ Miembro VIP"):
        # Llama al constructor de la clase base (Usuario)
        super().__init__(id_usuario, nombre, email)
        
        # Atributos exclusivos del servicio VIP
        self.insignia = insignia
        self.beneficios_activos = True
        self.contenido_exclusivo_visto = 0
