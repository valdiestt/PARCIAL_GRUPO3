
# =========================================================
# IMPORTACIÓN DE CLASES PARA LA SIMULACIÓN DE USUARIOS DE INSTAGRAM
# =========================================================
from Clase_usuario import Usuario
from publicacion import Publicacion
from usuario_vip import UsuarioVip

# =========================================================
# IMPORTACIÓN DE LA LIBRERÍA MATPLOTLIB PARA GRAFICAR ESTADÍSTICAS DE USUARIOS (AL SALIR DEL MENÚ)
# =========================================================
# python -m pip install matplotlib (ejecutar en el terminal)
import matplotlib

# =========================================================
# TODAS LAS FUNCIONES DE LA SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS (MENÚ PRINCIPAL)
# =========================================================
def mostrar_menu():
    print("\n" + "="*60)
    print("      SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS")
    print("="*60)
    print("1. Ver lista de usuarios registrados con sus estadísticas")
    print("2. Ver detalles completos de una cuenta (Perfil con Submenú)")
    print("3. Gestión de Seguidores y Follows (Submenú)")
    print("4. Gestión de Publicaciones (Submenú)")
    print("5. Gestión de Membresía Instagram Plus / VIP (Submenú)")
    print("6. Salir de la simulación")
    print("="*60)


def menu_historias_y_beneficios(red_social):
    """Conecta los metodos que ya existen en Usuario y UsuarioVip."""
    nombre = input("Identificate con tu @usuario: ").strip()
    if nombre not in red_social:
        print("❌ Usuario no encontrado.")
        return
    usuario = red_social[nombre]

    while True:
        print("\n--- HISTORIAS Y BENEFICIOS ---")
        print("1. Publicar una historia")
        print("2. Ver historias de otro usuario")
        print("3. Destacar una historia Spotlight (Plus)")
        print("4. Enviar supercorazon a una historia (Plus)")
        print("5. Crear lista de publico")
        print("6. Fijar publicacion propia")
        print("7. Consultar historias, vistas, listas y beneficios")
        print("8. Volver a membresias")
        accion = input("Elige (1-8): ").strip()

        if accion == '1':
            contenido = input("Historia (se permite texto vacio): ")
            usuario.publicar_historia(contenido)
            print("✅ Historia publicada.")

        elif accion == '2':
            destino_nombre = input("¿De quien quieres ver historias?: ").strip()
            if destino_nombre not in red_social:
                print("❌ Usuario no encontrado.")
                continue
            destino = red_social[destino_nombre]
            if destino is usuario:
                print("❌ No puedes ver tus propias historias como otra persona.")
                continue
            historias = destino.obtener_historias().copy()
            if not historias:
                print("Ese usuario aun no ha publicado historias.")
                continue
            if isinstance(destino, UsuarioVip):
                destacadas = destino.obtener_historias_spotlight()
                for historia in destacadas:
                    if historia in historias:
                        historias.remove(historia)
                historias = destacadas + historias
            for i, historia in enumerate(historias, 1):
                print(f"{i}. {historia}")
            if usuario.ver_historia(destino):
                print("✅ Visualizacion registrada." if not usuario.puede_ver_discreto()
                      else "✅ Historia vista discretamente (Plus).")
            else:
                print("No se registro otra vista (puede que ya las hayas visto).")

        elif accion == '3':
            if not isinstance(usuario, UsuarioVip):
                print("❌ Spotlight es exclusivo de Plus.")
                continue
            historias = usuario.obtener_historias()
            for i, historia in enumerate(historias):
                print(f"[{i}] {historia}")
            try:
                indice = int(input("Numero de historia Spotlight: "))
                if not 0 <= indice < len(historias):
                    raise IndexError
                exito = usuario.destacar_historia(historias[indice])
                print("✅ Historia destacada." if exito else "❌ No se pudo destacar otra vez.")
            except (ValueError, IndexError):
                print("❌ Numero invalido.")

        elif accion == '4':
            if not isinstance(usuario, UsuarioVip):
                print("❌ Los supercorazones son exclusivos de Plus.")
                continue
            destino_nombre = input("¿A quien envias el supercorazon?: ").strip()
            if destino_nombre not in red_social:
                print("❌ Usuario no encontrado.")
                continue
            destino = red_social[destino_nombre]
            historias = destino.obtener_historias()
            for i, historia in enumerate(historias):
                print(f"[{i}] {historia}")
            try:
                indice = int(input("Numero de historia: "))
                if not 0 <= indice < len(historias):
                    raise IndexError
                exito = usuario.enviar_supercorazon(destino, historias[indice])
                print("✅ Supercorazon enviado." if exito else "❌ No se pudo enviar.")
            except (ValueError, IndexError):
                print("❌ Numero invalido.")

        elif accion == '5':
            nombre_lista = input("Nombre de la lista: ")
            exito = usuario.crear_lista_publico(nombre_lista)
            print("✅ Lista creada." if exito else "❌ No se pudo crear: nombre repetido o limite alcanzado.")

        elif accion == '6':
            publicaciones = usuario.obtener_publicaciones()
            for i, publicacion in enumerate(publicaciones):
                print(f"[{i}] {publicacion}")
            try:
                indice = int(input("Numero de publicacion para fijar: "))
                if not 0 <= indice < len(publicaciones):
                    raise IndexError
                exito = usuario.fijar_publicacion(publicaciones[indice])
                print("✅ Publicacion fijada." if exito else "❌ Limite de fijadas alcanzado.")
            except (ValueError, IndexError):
                print("❌ Numero invalido.")

        elif accion == '7':
            print(f"Cuenta: {usuario}")
            print(f"Duracion de historias: {usuario.duracion_historia()} horas")
            limite = usuario.limite_fijadas() if isinstance(usuario, UsuarioVip) else Usuario.MAX_FIJADAS
            print(f"Publicaciones fijadas: {len(usuario.obtener_fijadas())}/{limite}")
            print(f"Historias: {usuario.obtener_historias()}")
            print("Historias que viste:", [u.obtener_nombre_usuario()
                                            for u in usuario.obtener_historias_vistas()])
            print("Personas que vieron tus historias:", [u.obtener_nombre_usuario()
                                                         for u in usuario.obtener_vistas_por()])
            print(f"Listas de publico: {usuario.obtener_listas_publico()}")
            print(f"Ver discreto: {usuario.puede_ver_discreto()} | "
                  f"Supercorazon: {usuario.puede_supercorazon()} | "
                  f"Spotlight: {usuario.puede_spotlight()}")
            print(f"Cambiar icono: {usuario.puede_cambiar_icono()} | "
                  f"Cambiar tipografia: {usuario.puede_cambiar_tipografia()}")
            if isinstance(usuario, UsuarioVip):
                print(f"Insignia: {usuario._insignia}")
                print(f"Historias Spotlight: {usuario.obtener_historias_spotlight()}")
                print(f"Supercorazones enviados: {usuario.obtener_supercorazones_enviados()}")

        elif accion == '8':
            break
        else:
            print("❌ Opcion invalida.")

def main():
    red_social = {}

# =========================================================
# INFORMACIÓN DE REGISTRO PREVIO DE USUARIOS DEFINIDOS
# =========================================================
    print("\n========== INFORMACIÓN DE REGISTRO PREVIO DE USUARIOS DEFINIDOS ==========")
    datos_usuarios = [
        ["valedies_1", "Valeria Guadalupe Diestra Buelot", "valediestra@gmail.com"],
        ["gbustillos_2", "Gustavo Enrique Bustillos Semeler", "gbustillos@gmail.com"],
        ["stayci_3", "Stayci Marisol Ovalle Muñoz", "sovalle@gmail.com"],
        ["sebastian_4", "Sebastián Mauricio Díaz Pasache", "sdiaz@gmail.com"]
    ]

    for datos in datos_usuarios:
        print(datos)
        red_social[datos[0]] = Usuario(datos[0], datos[1], datos[2])

    print("====================================================")

# =========================================================
# BUCLE DEL MENÚ PRINCIPAL (OPCIONES 1-6)
# =========================================================
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

# =========================================================
# OBTENCIÓN DE DATOS DE USUARIOS AL ESCOGER LA OPCIÓN 1 (SEMIORGANIZADO EN TABLA)
# =========================================================
        if opcion == '1':
            print("\n====================== INFORMACIÓN DE CUENTA INSTAGRAM ======================")
            print("|===== User ====|========= Nombre Completo =========|======== Correo =======|")
            for cuenta in red_social.values():
                print(f"@{cuenta.obtener_nombre_usuario()} | {cuenta.obtener_nombre_completo()} | "
                      f"{cuenta.obtener_correo()} | Seguidores: {cuenta.cantidad_seguidores()} | "
                      f"Publicaciones: {cuenta.cantidad_publicaciones()}")
            print("================|===================================|========================|")

# =========================================================
# SERIE DE OPCIONES PARA LA OPCIÓN 2 (PREVIAMENTE HABER BUSCADO UN USUARIO DEFINIDO)
# =========================================================
        elif opcion == '2':
            print("\n--- BUSCAR PERFIL ---")
            buscar = input("Ingresa el @nombre_usuario que quieres revisar: ").strip()
            if buscar in red_social:
                perfil = red_social[buscar]
                es_vip = isinstance(perfil, UsuarioVip)

                print(f"\n--- 👤 Perfil de @{buscar} ---")
                print(f"📛 Nombre: {perfil.obtener_nombre_completo()}")
                print(f"👥 Seguidores: {perfil.cantidad_seguidores()} | 👣 Seguidos: {perfil.cantidad_seguidos()}")
                print(f"🌟 Influencer: {'Sí' if perfil.es_influencer() else 'No'}")
                print(f"👑 VIP: {'Sí 💎' if es_vip else 'No (Standard)'}")
                print(f"🎨 Personalización -> Icono: '{perfil.obtener_icono()}' | Tipografía: '{perfil.obtener_tipografia()}'")

                if es_vip:
                    while True:
                        print("\n--- ✨ OPCIONES EXCLUSIVAS VIP ✨ ---")
                        print("1. Cambiar icono de la APP")
                        print("2. Cambiar tipografía")
                        print("3. Salir del perfil")
                        sub_perfil = input("Elige una opción VIP (1-3): ").strip()

                        if sub_perfil == '1':
                        # Si de la opción 2, se escoge la subopción 1
                            nuevo_icono = input("Escribe el estilo para tu nuevo icono (ej. Oscuro): ").strip()
                            if perfil.cambiar_icono(nuevo_icono):
                                print(f"✅ ¡Éxito! El icono de la app cambió a '{nuevo_icono}'.")
                            else:
                                print("❌ Error al cambiar icono.")

                        elif sub_perfil == '2':
                        # Si de la opción 2, se escoge la subopción 2
                            nueva_fuente = input("Escribe tu nueva tipografía (ej. Cursiva): ").strip()
                            if perfil.cambiar_tipografia(nueva_fuente):
                                print(f"✅ ¡Éxito! Tu aplicación ahora usa la tipografía '{nueva_fuente}'.")
                            else:
                                print("❌ Error al cambiar tipografía.")
                        elif sub_perfil == '3':
                            break
                        else:
                            print("❌ Opción inválida.")
                else:
                    input("\n(Presiona ENTER para volver al menú principal...)")
            else:
                print("❌ Usuario no encontrado.")

# =========================================================
# SERIE DE OPCIONES PARA LA OPCIÓN 3 (GESTIÓN DE SEGUIDORES Y SEGUIDOS)
# =========================================================
        elif opcion == '3':
            while True:
                print("\n" + "-"*50)
                print("      OPCIÓN 3: GESTIÓN DE SEGUIDORES Y SEGUIDOS")
                print("-"*50)
                print("1. Simular un 'Follow' (Un usuario sigue a otro)")
                print("2. Dejar de seguir a un usuario")
                print("3. Ver a quién sigue un usuario (Seguidos)")
                print("4. Ver quién sigue a un usuario (Seguidores)")
                print("5. Volver al menú principal")
                print("-"*50)

                sub3 = input("Elige una subopción (1-5): ").strip()

                if sub3 == '1':
                    seguidor = input("¿Quién va a seguir?: ").strip()
                    seguido = input("¿A quién va a seguir?: ").strip()
                    if seguidor in red_social and seguido in red_social:
                        if red_social[seguidor].seguir(red_social[seguido]):
                            print(f"✅ ¡Confirmado! @{seguidor} empezó a seguir a @{seguido}.")
                        else:
                            print("❌ Acción denegada (ya lo sigue o intentó seguirse a sí mismo).")
                    else:
                        print("❌ Uno o ambos usuarios no existen.")

                elif sub3 == '2':
                    seguidor = input("¿Quién va a dejar de seguir?: ").strip()
                    seguido = input("¿A quién va a dejar de seguir?: ").strip()
                    if seguidor in red_social and seguido in red_social:
                        if red_social[seguidor].dejar_de_seguir(red_social[seguido]):
                            print(f"✅ ¡Confirmado! @{seguidor} ha dejado de seguir a @{seguido}.")
                        else:
                            print("❌ Acción denegada (no lo seguía).")
                    else:
                        print("❌ Uno o ambos usuarios no existen.")

                elif sub3 == '3':
                    buscar = input("Ingresa el @usuario que deseas consultar: ").strip()
                    if buscar in red_social:
                        seguidos = red_social[buscar].obtener_seguidos()
                        if len(seguidos) == 0:
                            print(f"👤 @{buscar} no sigue a nadie todavía.")
                        else:
                            print(f"👤 @{buscar} sigue a {len(seguidos)} cuenta(s):")
                            for cuenta in seguidos:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub3 == '4':
                    buscar = input("Ingresa el @usuario que deseas consultar: ").strip()
                    if buscar in red_social:
                        seguidores = red_social[buscar].obtener_seguidores()
                        if len(seguidores) == 0:
                            print(f"👤 @{buscar} no tiene seguidores todavía.")
                        else:
                            print(f"👤 @{buscar} es seguido por {len(seguidores)} cuenta(s):")
                            for cuenta in seguidores:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub3 == '5':
                    print("↩️ Regresando al menú principal...")
                    break

# =========================================================
# SERIE DE OPCIONES PARA LA OPCIÓN 4 (GESTIÓN DE PUBLICACIONES, LIKES Y COMENTARIOS)
# =========================================================
        elif opcion == '4':
            while True:
                print("\n--- OPCIÓN 4: PUBLICACIONES ---")
                print("1. Crear una nueva publicación (Identificarse primero)")
                print("2. Ver las publicaciones de un usuario")
                print("3. Comentar la publicación de alguien")
                print("4. Compartir la publicación de alguien")
                print("5. Volver al menú principal")
                sub4 = input("Elige (1-5): ").strip()

                if sub4 == '1':
                # Si de la opción 4, se escoge la subopción 1
                    autor = input("Identifícate (Ingresa tu @usuario): ").strip()
                    if autor in red_social:
                        texto = input("Escribe el contenido de tu publicación: ")
                        nueva_pub = Publicacion(red_social[autor], texto)
                        red_social[autor].obtener_publicaciones().append(nueva_pub)
                        print("✅ ¡Publicación subida con éxito!")
                    else:
                        print("❌ Ese usuario no existe.")

                elif sub4 == '2':
                # Si de la opción 4, se escoge la subopción 2
                    buscar = input("¿De qué @usuario quieres ver el feed?: ").strip()
                    if buscar in red_social:
                        pubs = red_social[buscar].obtener_publicaciones()
                        if not pubs:
                            print(f"@{buscar} no tiene publicaciones.")
                        else:
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub}")

                            print("\n--- INTERACCIÓN CON EL FEED ---")
                            print("A. Ver cantidad de likes, comentarios y compartidos de una publicación")
                            print("B. Dar o quitar un Like a una publicación")
                            print("C. Salir de este feed")
                            accion = input("Elige (A/B/C): ").strip().upper()

                            if accion == 'A':
                                # Si de la subopción 2, se escoge la opción específica A
                                try:
                                    idx = int(input("Ingresa el número [#] de la publicación: "))
                                    pub = pubs[idx]
                                    print(f"\n--- DETALLES DE LA PUBLICACIÓN [{idx}] ---")
                                    print(f"Contenido: {pub.obtener_contenido()}")

                                    likes = pub.obtener_likes()
                                    lista_likes = ", ".join([f"@{u.obtener_nombre_usuario()}" for u in likes]) if likes else "Nadie aún"
                                    print(f"❤️ Likes ({pub.cantidad_likes()}): {lista_likes}")

                                    print("💬 Comentarios:")
                                    comentarios = pub.obtener_comentarios()
                                    if comentarios:
                                        for c in comentarios:
                                            print(f"   {c}")
                                    else:
                                        print("   Sin comentarios aún.")

                                    print(f"🔁 Compartidos: {pub.obtener_compartidos()}")
                                except ValueError:
                                    print("❌ Debes ingresar un número válido.")
                                except IndexError:
                                    print("❌ Ese número de publicación no existe.")

                            elif accion == 'B':
                                # Si de la subopción 2, se escoge la opción específica B
                                interactor = input("Identifícate (Tu @usuario): ").strip()
                                if interactor in red_social:
                                    try:
                                        idx = int(input("Ingresa el número [#] de la publicación a dar/quitar like: "))
                                        usuario_interactor = red_social[interactor]

                                        if usuario_interactor in pubs[idx].obtener_likes():
                                            pubs[idx].quitar_like(usuario_interactor)
                                            print(f"💔 Le quitaste tu like a la publicación [{idx}].")
                                        else:
                                            pubs[idx].dar_like(usuario_interactor)
                                            print(f"✅ ¡Le diste like a la publicación [{idx}]!")

                                    except (ValueError, IndexError):
                                        print("❌ Número de publicación inválido.")
                                else:
                                    print("❌ Ese usuario no existe.")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub4 == '3':
                # Si de la opción 4, se escoge la subopción 3
                    interactor = input("¿Quién va a comentar? (Tu @usuario): ").strip()
                    autor = input("¿A quién quieres comentarle? (@usuario): ").strip()
                    if interactor in red_social and autor in red_social:
                        pubs = red_social[autor].obtener_publicaciones()
                        if not pubs:
                            print("❌ Este usuario no tiene publicaciones para comentar.")
                        else:
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub.obtener_contenido()}")
                            try:
                                indice = int(input("Ingresa el número [#] de la publicación a comentar: "))
                                comentario = input("Escribe tu comentario: ")
                                if pubs[indice].comentar(red_social[interactor], comentario):
                                    print("✅ ¡Comentario enviado!")
                                else:
                                    print("❌ Error al enviar el comentario.")
                            except (ValueError, IndexError):
                                print("❌ Número inválido.")
                    else:
                        print("❌ Usuarios no encontrados.")

                elif sub4 == '4':
                # Si de la opción 4, se escoge la subopción 4
                    interactor = input("¿Quién va a compartir? (Tu @usuario): ").strip()
                    autor = input("¿De quién es la publicación a compartir? (@usuario): ").strip()
                    if interactor in red_social and autor in red_social:
                        pubs = red_social[autor].obtener_publicaciones()
                        if not pubs:
                            print("❌ Este usuario no tiene publicaciones.")
                        else:
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub.obtener_contenido()}")
                            try:
                                indice = int(input("Ingresa el número [#] de la publicación a compartir: "))
                                # Se usa el método compartir() de la clase Publicacion
                                total_compartidos = pubs[indice].compartir()
                                print(f"✅ ¡Publicación compartida por @{interactor}! Ahora tiene {total_compartidos} compartidos en total.")
                            except (ValueError, IndexError):
                                print("❌ Número de publicación inválido.")
                    else:
                        print("❌ Usuarios no encontrados.")

                elif sub4 == '5':
                # Si de la opción 4, se escoge la subopción 5
                    break
                else:
                    print("❌ Opción inválida.")

# =========================================================
# SERIE DE OPCIONES PARA LA OPCIÓN 5 (GESTIÓN DE MEMBRESÍA INSTAGRAM PLUS / VIP)
# =========================================================
        elif opcion == '5':
            while True:
                print("\n--- OPCIÓN 5: GESTIÓN DE MEMBRESÍA INSTAGRAM PLUS / VIP ---")
                print("1. Establecer el Instagram Plus / VIP a un usuario")
                print("2. Darse de baja (Volver a cuenta gratuita)")
                print("3. Revisar el estado Instagram Plus / VIP de un usuario")
                print("4. Historias, listas y beneficios")
                print("5. Volver al menú principal")
                sub5 = input("Elige (1-5): ").strip()

                if sub5 == '1':
                # Si de la opción 5, se escoge la subopción 1
                    buscar = input("Identifícate (@usuario): ").strip()
                    if buscar in red_social:
                        usr_actual = red_social[buscar]
                        if isinstance(usr_actual, UsuarioVip):
                            print(f"❌ ¡@{buscar} ya cuenta con una membresía VIP activa!")
                        else:
                            # Cambiamos el tipo del MISMO objeto: nadie pierde sus
                            # referencias de seguidores, seguidos, likes o publicaciones.
                            usr_actual.__class__ = UsuarioVip
                            usr_actual._insignia = "💎 Instagram Plus"
                            usr_actual._historias_spotlight = []
                            usr_actual._supercorazones_enviados = []
                            usr_actual.establecer_estado_plus(True)

                            print(f"\n🎉 ¡Felicidades! @{buscar} ha adquirido la membresía Instagram Plus / VIP.")
                            print("✨ TUS NUEVOS BENEFICIOS ✨")
                            print("  - Insignia exclusiva Instagram Plus.")
                            print("  - Duración máxima de historias extendida a 48h.")
                            print("  - Límite de publicaciones fijadas aumentado a un máximo de 6.")
                            print("  - Puedes cambiar el icono de la app.")
                            print("  - Puedes cambiar la tipografía de tus textos.")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '2':
                # Si de la opción 5, se escoge la subopción 2
                    buscar = input("Identifícate (@usuario): ").strip()
                    if buscar in red_social:
                        usr_actual = red_social[buscar]
                        if not isinstance(usr_actual, UsuarioVip):
                            print(f"❌ @{buscar} ya es un usuario gratuito. No puedes darte de baja.")
                        else:
                            # Se conserva el mismo objeto y todas sus relaciones.
                            usr_actual.establecer_estado_plus(False)
                            usr_actual.__class__ = Usuario
                            usr_actual._icono = "default"
                            usr_actual._tipografia = "default"

                            print(f"\n📉 @{buscar} se ha dado de baja del servicio Instagram Plus / VIP.")
                            print("🔒 ESTADO ACTUAL DE TU CUENTA 🔒")
                            print("  - Has perdido los beneficios del VIP (Insignia, icono y tipografías).")
                            print("  - Tu cuenta vuelve a ser Standard.")
                            print("  - Duración de historias reducida a 24h.")
                            print("  - Máximo de publicaciones fijadas se reduce a 3.")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '3':
                # Si de la opción 5, se escoge la subopción 3
                    buscar = input("¿De qué @usuario quieres ver el estado VIP?: ").strip()
                    if buscar in red_social:
                        usr = red_social[buscar]
                        print(f"\n--- ESTADO DE @{buscar} ---")
                        print(f"Influencer (>1000 seg): {'Sí 🌟' if usr.es_influencer() else 'No'}")
                        print(f"Suscripción VIP: {'Activa 💎' if isinstance(usr, UsuarioVip) else 'Gratuita'}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '4':
                    menu_historias_y_beneficios(red_social)

                elif sub5 == '5':
                    break
                else:
                    print("❌ Opción inválida.")

# =========================================================
# SALIDA DE LA SIMULACIÓN (OPCIÓN 6)
# =========================================================
        elif opcion == '6':
            print("\nCerrando simulación y generando gráfica final de estadísticas...")

            try:
                import matplotlib.pyplot as plt

                # Extrayendo datos dinámicos en tiempo real de la simulación
                nombres = list(red_social.keys())
                seguidores = [red_social[u].cantidad_seguidores() for u in nombres]
                seguidos = [red_social[u].cantidad_seguidos() for u in nombres]
                publicaciones = [red_social[u].cantidad_publicaciones() for u in nombres]

                # Configuraciones matemáticas para agrupar las barras (sin usar numpy)
                x = range(len(nombres))
                ancho_barra = 0.25

                pos_seguidores = [pos - ancho_barra for pos in x]
                pos_seguidos = [pos for pos in x]
                pos_publicaciones = [pos + ancho_barra for pos in x]

                # Creando el gráfico con los colores de Instagram
                fig, ax = plt.subplots(figsize=(10, 6))

                ax.bar(pos_seguidores, seguidores, ancho_barra, label='Seguidores', color='#E1306C')
                ax.bar(pos_seguidos, seguidos, ancho_barra, label='Seguidos', color='#833AB4')
                ax.bar(pos_publicaciones, publicaciones, ancho_barra, label='Publicaciones', color='#405DE6')

                # Detalles estéticos de la ventana
                ax.set_ylabel('Cantidades')
                ax.set_title('Resumen Final de Estadísticas - Red Social G3')
                ax.set_xticks(x)
                ax.set_xticklabels(nombres)
                ax.legend()

                # Forzamos a que el gráfico se dibuje y se muestre en una ventana emergente
                plt.tight_layout()
                plt.show()
                print("✅ Gráfica cerrada exitosamente.")

            except ImportError:
                print("⚠️ NOTA: No se pudo generar el gráfico porque no tienes instalada la librería.")

            print("\nSaliendo de la simulación del Grupo 3... ¡Hasta luego!")
            break

        else:
            print("\n❌ Opción no válida. Intenta de nuevo (1 al 6).")

if __name__ == "__main__":
    main()
