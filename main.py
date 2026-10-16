# =========================================================
from Clase_usuario import Usuario
from publicacion import Publicacion
from usuario_vip import UsuarioVip
# =========================================================

# FUNCIONES DE LOS MENÚS
def mostrar_menu():
    print("\n" + "="*60)
    print("      SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS")
    print("="*60)
    print("1. Ver lista de usuarios registrados con sus estadísticas")
    print("2. Ver detalles completos de una cuenta (Perfil)")
    print("3. Gestión de Seguidores y Follows (Submenú)")
    print("4. Gestión de Publicaciones (Submenú)")
    print("5. Gestión de Incidencias de Cuenta (Submenú)")
    print("6. Salir de la simulación")
    print("="*60)

def main():
    red_social = {}
    
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
                print(f"\n--- 👤 Perfil de @{buscar} ---")
                print(f"📛 Nombre: {perfil.obtener_nombre_completo()}")
                print(f"👥 Seguidores: {perfil.cantidad_seguidores()} | 👣 Seguidos: {perfil.cantidad_seguidos()}")
                print(f"🌟 Influencer: {'Sí' if perfil.es_influencer() else 'No'}")
                print(f"✅ Verificado: {'Sí' if perfil.esta_verificado() else 'No'}")
                print(f"🚨 Reportado: {'Sí' if perfil.esta_reportado() else 'No'}")
            else:
                print("❌ Usuario no encontrado.")
                
        elif opcion == '3':
            # =========================================================
            # SUBMENÚ DE LA OPCIÓN 3: GESTIÓN DE SEGUIDORES Y SEGUIDOS
            # =========================================================
            while True:
                print("\n" + "-"*50)
                print("    OPCIÓN 3: GESTIÓN DE SEGUIDORES Y SEGUIDOS")
                print("-"*50)
                print("1. Simular un 'Follow' (Un usuario sigue a otro)")
                print("2. Ver a quién sigue un usuario (Seguidos)")
                print("3. Ver quién sigue a un usuario (Seguidores)")
                print("4. Volver al menú principal")
                print("-"*50)

                sub3 = input("Elige una subopción (1-4): ").strip()

                if sub3 == '1':
                    print("\n--- SIMULACIÓN DE FOLLOW ---")
                    seguidor = input("¿Quién va a seguir? (Ingresa su @usuario): ").strip()
                    seguido = input("¿A quién va a seguir? (Ingresa su @usuario): ").strip()
                    
                    if seguidor in red_social and seguido in red_social:
                        exito = red_social[seguidor].seguir(red_social[seguido])
                        if exito:
                            print(f"✅ ¡Confirmado! @{seguidor} empezó a seguir a @{seguido}.")
                        else:
                            print("❌ Acción denegada (ya lo sigue o intentó seguirse a sí mismo).")
                    else:
                        print("❌ Error: Uno o ambos usuarios no existen.")

                elif sub3 == '2':
                    print("\n--- LISTA DE SEGUIDOS (A quién sigue) ---")
                    buscar = input("Ingresa el @usuario que deseas consultar: ").strip()
                    if buscar in red_social:
                        lista_seguidos = red_social[buscar].obtener_seguidos()
                        if len(lista_seguidos) == 0:
                            print(f"👤 @{buscar} no sigue a nadie todavía.")
                        else:
                            print(f"👤 @{buscar} sigue a {len(lista_seguidos)} cuenta(s):")
                            for cuenta in lista_seguidos:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub3 == '3':
                    print("\n--- LISTA DE SEGUIDORES (Quién lo sigue) ---")
                    buscar = input("Ingresa el @usuario que deseas consultar: ").strip()
                    if buscar in red_social:
                        lista_seguidores = red_social[buscar].obtener_seguidores()
                        if len(lista_seguidores) == 0:
                            print(f"👤 @{buscar} no tiene seguidores todavía.")
                        else:
                            print(f"👤 @{buscar} es seguido por {len(lista_seguidores)} cuenta(s):")
                            for cuenta in lista_seguidores:
                                print(f"   - @{cuenta.obtener_nombre_usuario()}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub3 == '4':
                    print("↩️ Regresando al menú principal...")
                    break

                else:
                    print("❌ Opción no válida. Ingresa un número del 1 al 4.")

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
                        red_social[autor].publicar(texto)
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
                            # 1. Mostramos las publicaciones
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub}")
                                
                            # 2. Agregamos el mini-menú de interacción
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
                                    print(f"Contenido: {pub.contenido}")
                                    
                                    # Formatear la lista de likes
                                    lista_likes = ", ".join([f"@{u}" for u in pub.likes]) if pub.likes else "Nadie aún"
                                    print(f"❤️ Likes ({len(pub.likes)}): {lista_likes}")
                                    
                                    print("💬 Comentarios:")
                                    if pub.comentarios:
                                        for c in pub.comentarios:
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
                                        # Llamamos al método dar_like que ya tenían programado
                                        exito = red_social[interactor].dar_like(pubs[idx])
                                        if exito:
                                            print(f"✅ ¡Le diste like a la publicación [{idx}]!")
                                        else:
                                            print("⚠️ Ya le habías dado like a esta publicación antes.")
                                    except ValueError:
                                        print("❌ Debes ingresar un número válido.")
                                    except IndexError:
                                        print("❌ Ese número de publicación no existe.")
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
                            print("Publicaciones disponibles:")
                            for i, pub in enumerate(pubs):
                                print(f"[{i}] {pub.contenido}")
                            try:
                                indice = int(input("Ingresa el número [#] de la publicación a comentar: "))
                                comentario = input("Escribe tu comentario: ")
                                red_social[interactor].comentar(pubs[indice], comentario)
                                print("✅ ¡Comentario enviado!")
                            except ValueError:
                                print("❌ Ingresa un número entero válido.")
                            except IndexError:
                                print("❌ Ese número de publicación no existe.")
                    else:
                        print("❌ Usuarios no encontrados.")

                elif sub4 == '4':
                    break

        elif opcion == '5':
            while True:
                print("\n--- OPCIÓN 5: INCIDENCIAS Y ESTADO ---")
                print("1. Verificar cuenta (Otorga el check azul)")
                print("2. Reportar a un usuario por mal comportamiento")
                print("3. Revisar estado de incidencias de un usuario")
                print("4. Volver al menú principal")
                sub5 = input("Elige (1-4): ").strip()

                if sub5 == '1':
                    buscar = input("¿Qué @usuario deseas verificar?: ").strip()
                    if buscar in red_social:
                        red_social[buscar].verificar_cuenta()
                        print(f"✅ ¡La cuenta @{buscar} ha sido verificada exitosamente!")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '2':
                    buscar = input("¿Qué @usuario deseas reportar?: ").strip()
                    if buscar in red_social:
                        red_social[buscar].reportar_cuenta()
                        print(f"🚨 ¡La cuenta @{buscar} ha sido reportada!")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '3':
                    buscar = input("¿De qué @usuario quieres ver el estado?: ").strip()
                    if buscar in red_social:
                        usr = red_social[buscar]
                        print(f"\n--- ESTADO DE @{buscar} ---")
                        print(f"Verificado: {'Sí ✅' if usr.esta_verificado() else 'No ❌'}")
                        print(f"Reportado: {'Sí 🚨' if usr.esta_reportado() else 'No 🟢'}")
                        print(f"Influencer (>1000 seg): {'Sí 🌟' if usr.es_influencer() else 'No'}")
                    else:
                        print("❌ Usuario no encontrado.")

                elif sub5 == '4':
                    break

        elif opcion == '6':
            print("\nSaliendo de la simulación del Grupo 3... ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()