# Archivo: usuario_vip.py
from Clase_usuario import Usuario 

class UsuarioVip(Usuario):
    def __init__(self, nombre_usuario, nombre_completo, correo, insignia="⭐ Miembro VIP"):
        # Llama al constructor de la clase base (Usuario)
        super().__init__(nombre_usuario, nombre_completo, correo)
        
        # Atributos exclusivos del servicio VIP
        self.insignia = insignia
        self.beneficios_activos = True
        self.contenido_exclusivo_visto = 0

    # Sobreescribimos el print para que los VIP luzcan su insignia
    def __str__(self):
        verif = "✅" if self._verificado else ""
        return (
            f"@{self._nombre_usuario}{verif} {self.insignia} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )