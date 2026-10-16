from Clase_usuario import Usuario
from publicacion import Publicacion
from usuario_vip import UsuarioVip

# =========================================================
# FUNCIONES DE LOS MENÚS
# =========================================================
def mostrar_menu():
    print("\n" + "="*60)
    print("      SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS")
    print("="*60)
    print("1. Ver lista de usuarios registrados con sus estadísticas")
    print("2. Ver detalles completos de una cuenta (Perfil)")
    print("3. Gestión de Seguidores y Follows (Submenú)")
    print("4. Gestión de Publicaciones (Submenú)")
    print("5. Gestión de Membresía VIP (Submenú)")
    print("6. Salir de la simulación")
    print("="*60)

def main():
    red_social = {}
    
    print("\n========== INFORMACIÓN DE REGISTRO PREVIO DE USUARIOS DEFINIDOS ==========")
    datos_usuarios = [
        ["valedies_1", "Valeria Guadalupe Diestra Vuelot", "valediestra@gmail.com"],
        ["gbustillos_2", "Gustavo Enrique Bustillos Semeler", "gbustillos@gmail.com"],
        ["stayci_3", "Stayci Marisol Ovalle Muñoz", "sovalle@gmail.com"],
        ["sebastian_4", "Sebastián Mauricio Díaz Pasache", "sdiaz@gmail.com"]
    ]

    for datos in datos_usuarios:
        print(datos)
        red_social[datos[0]] = Usuario(datos[0], datos[1], datos[2])
        
    print("====================================================")

    # =========================================================
    # BUCLE DEL MENÚ PRINCIPAL
    # =========================================================
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == '1':
            print("\n========== INFORMACIÓN DE CUENTA INSTAGRAM ==========")
            print("|===== User ====|========= Nombre Completo =========|======== Correo =======|")
            for datos in datos_usuarios:
                print(datos)
                
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
                            nuevo_icono = input("Escribe el estilo para tu nuevo icono (ej. Oscuro): ").strip()
                            if perfil.cambiar_icono(nuevo_icono):
                                print(f"✅ ¡Éxito! El icono de la app cambió a '{nuevo_icono}'.")
                            else:
                                print("❌ Error al cambiar icono.")
                                
                        elif sub_perfil == '2':
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
                
        elif opcion == '3':
            while True:
                print("\n" + "-"*50)
                print("      OPCIÓN 3: GESTIÓN DE SEGUIDORES Y SEGUIDOS")
                print("-"*50)
                print("1. Simular un 'Follow' (Un usuario sigue a otro)")
                print("2. Ver a quién sigue un usuario (Seguidos)")
                print("3. Ver quién sigue a un usuario (Seguidores)")
                print("4. Volver al menú principal")
                print("-"*50)

                sub3 = input("Elige una subopción (1-4): ").strip()

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

                elif sub3 == '3':
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

                elif sub3 == '4':
                    print("↩️ Regresando al menú principal...")
                    break

        elif opcion == '4':
            while True:
                print("\n--- OPCIÓN 4: PUBLICACIONES ---")
                print("1. Crear una nueva publicación (Identificarse primero)")
                print("2. Ver feed, likes y comentarios de un usuario")
                print("3. Comentar la publicación de alguien")
                print("4. Volver al menú principal")
                sub4 = input("Elige (1-4): ").strip()

                if sub4 == '1':
                    autor = input("Identifícate (Ingresa tu @usuario): ").strip()
                    if autor in red_social:
                        texto = input("Escribe el contenido de tu publicación: ")
                        # ADAPTACIÓN: Instanciamos directamente Publicacion ya que Usuario no tiene el método
                        nueva_pub = Publicacion(red_social[autor], texto)
                        red_social[autor].obtener_publicaciones().append(nueva_pub)
                        print("✅ ¡Publicación subida con éxito!")
                    else:
                        print("❌ Ese usuario no existe.")

                elif sub4 == '2':
                    buscar = input("¿De qué @usuario quieres ver el feed?: ").strip()
                    if buscar in red_social:
                        pubs = red_social[buscar].obtener_publicaciones()
                        if not pubs:
                            print(f"@{buscar} no tiene publicaciones.")
                        else:
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub}")
                                
                            print("\n--- INTERACCIÓN CON EL FEED ---")
                            print("A. Ver detalles (Quién dio like y leer comentarios)")
                            print("B. Dar un Like a una publicación")
                            print("C. Salir de este feed")
                            accion = input("Elige (A/B/C): ").strip().upper()

                            if accion == 'A':
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
                                except ValueError:
                                    print("❌ Debes ingresar un número válido.")
                                except IndexError:
                                    print("❌ Ese número de publicación no existe.")
                                    
                            elif accion == 'B':
                                interactor = input("Identifícate (Tu @usuario): ").strip()
                                if interactor in red_social:
                                    try:
                                        idx = int(input("Ingresa el número [#] de la publicación a dar like: "))
                                        # ADAPTACIÓN: Usamos el método propio de la clase Publicacion
                                        if pubs[idx].dar_like(red_social[interactor]):
                                            print(f"✅ ¡Le diste like a la publicación [{idx}]!")
                                        else:
                                            print("⚠️ Ya le habías dado like a esta publicación antes.")
                                    except (ValueError, IndexError):
                                        print("❌ Número de publicación inválido.")
                                else:
                                    print("❌ Ese usuario no existe.")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub4 == '3':
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
                                # ADAPTACIÓN: Usamos el método propio de la clase Publicacion
                                if pubs[indice].comentar(red_social[interactor], comentario):
                                    print("✅ ¡Comentario enviado!")
                                else:
                                    print("❌ Error al enviar el comentario.")
                            except (ValueError, IndexError):
                                print("❌ Número inválido.")
                    else:
                        print("❌ Usuarios no encontrados.")

                elif sub4 == '4':
                    break

        elif opcion == '5':
            while True:
                # ADAPTACIÓN: Se eliminaron las verificaciones y reportes ya que no existen en los archivos .py enviados
                print("\n--- OPCIÓN 5: GESTIÓN DE MEMBRESÍA VIP ---")
                print("1. Establecer el VIP a un usuario")
                print("2. Darse de baja (Volver a cuenta gratuita)")
                print("3. Revisar el estado VIP de un usuario")
                print("4. Volver al menú principal")
                sub5 = input("Elige (1-4): ").strip()

                if sub5 == '1':
                    buscar = input("Identifícate (@usuario): ").strip()
                    if buscar in red_social:
                        usr_actual = red_social[buscar]
                        if isinstance(usr_actual, UsuarioVip):
                            print(f"❌ ¡@{buscar} ya cuenta con una membresía VIP activa!")
                        else:
                            # Creamos la versión VIP
                            nuevo_vip = UsuarioVip(buscar, usr_actual.obtener_nombre_completo(), usr_actual.obtener_correo())
                            
                            # ADAPTACIÓN: Encendemos los beneficios usando el método que SÍ existe en usuario_vip.py
                            nuevo_vip.establecer_estado_plus(True)
                            
                            # Traspaso total de las listas
                            nuevo_vip._seguidores = usr_actual.obtener_seguidores()
                            nuevo_vip._seguidos = usr_actual.obtener_seguidos()
                            nuevo_vip._publicaciones = usr_actual.obtener_publicaciones()
                            nuevo_vip._historias = usr_actual.obtener_historias()
                            nuevo_vip._historias_vistas = usr_actual.obtener_historias_vistas()
                            nuevo_vip._vistas_por = usr_actual.obtener_vistas_por()
                            nuevo_vip._listas_publico = usr_actual.obtener_listas_publico()
                            nuevo_vip._fijadas = usr_actual.obtener_fijadas()
                            nuevo_vip._icono = usr_actual.obtener_icono()
                            nuevo_vip._tipografia = usr_actual.obtener_tipografia()
                            
                            red_social[buscar] = nuevo_vip
                            
                            print(f"\n🎉 ¡Felicidades! @{buscar} ha adquirido la membresía VIP.")
                            print("✨ TUS NUEVOS BENEFICIOS ✨")
                            print("  - Insignia exclusiva y cero anuncios.")
                            print("  - Duración máxima de historias extendida a 48h.")
                            print("  - Límite de publicaciones fijadas aumentado a un máximo de 6.")
                            print("  - Puedes cambiar el icono de la app.")
                            print("  - Puedes cambiar la tipografía de tus textos.")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '2':
                    buscar = input("Identifícate (@usuario): ").strip()
                    if buscar in red_social:
                        usr_actual = red_social[buscar]
                        if not isinstance(usr_actual, UsuarioVip):
                            print(f"❌ @{buscar} ya es un usuario gratuito. No puedes darte de baja.")
                        else:
                            # Creamos la versión Normal
                            usuario_normal = Usuario(buscar, usr_actual.obtener_nombre_completo(), usr_actual.obtener_correo())
                            
                            # Traspaso total inverso
                            usuario_normal._seguidores = usr_actual.obtener_seguidores()
                            usuario_normal._seguidos = usr_actual.obtener_seguidos()
                            usuario_normal._publicaciones = usr_actual.obtener_publicaciones()
                            usuario_normal._historias = usr_actual.obtener_historias()
                            usuario_normal._historias_vistas = usr_actual.obtener_historias_vistas()
                            usuario_normal._vistas_por = usr_actual.obtener_vistas_por()
                            usuario_normal._listas_publico = usr_actual.obtener_listas_publico()
                            usuario_normal._fijadas = usr_actual.obtener_fijadas()
                            
                            red_social[buscar] = usuario_normal
                            
                            print(f"\n📉 @{buscar} se ha dado de baja del servicio VIP.")
                            print("🔒 ESTADO ACTUAL DE TU CUENTA 🔒")
                            print("  - Has perdido los beneficios del VIP (Insignia, icono y tipografías).")
                            print("  - Tu cuenta vuelve a ser Standard (verás anuncios).")
                            print("  - Duración de historias reducida a 24h.")
                            print("  - Máximo de publicaciones fijadas se reduce a 3.")
                    else:
                        print("❌ Usuario no encontrado.")
                
                elif sub5 == '3':
                    buscar = input("¿De qué @usuario quieres ver el estado VIP?: ").strip()
                    if buscar in red_social:
                        usr = red_social[buscar]
                        print(f"\n--- ESTADO DE @{buscar} ---")
                        print(f"Influencer (>1000 seg): {'Sí 🌟' if usr.es_influencer() else 'No'}")
                        print(f"Suscripción VIP: {'Activa 💎' if isinstance(usr, UsuarioVip) else 'Gratuita'}")
                    else:
                        print("❌ Usuario no encontrado.")
                        
                elif sub5 == '4':
                    break
                else:
                    print("❌ Opción inválida.")

        elif opcion == '6':
            print("\nSaliendo de la simulación del Grupo 3... ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo (1 al 6).")

if __name__ == "__main__":
    main()