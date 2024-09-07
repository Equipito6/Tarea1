import logging
from usuarios import cargar_usuarios, registrar, autenticar
from tareas import cargar_tareas, crear_tarea, listar_tareas, editar_tarea, eliminar_tarea, cambiar_estado, buscar_tareas, tareas_completadas, guardar_tareas, obtener_tareas

# Logs como un registro de auditoría con fecha y la acción que se realizó
logging.basicConfig(filename='Operaciones.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

log = False
menu = True
cargar_usuarios()
usuario_actual = None

print("1. Iniciar sesión")
print("2. Registrarse")
print("3. Salir")
opcion = input("Selecciona una opción: ")

while menu:
    if opcion == "1":
        usuario_actual = autenticar()
        if not usuario_actual:
            print("Acceso denegado")
        else:
            cargar_tareas(usuario_actual)
            menu = False
            log = True
    elif opcion == "2":
        if not registrar():
            print("Error en el registro")
        print("Registrado con éxito. Ahora inicia sesión.")
        usuario_actual = autenticar()
        if not usuario_actual:
            print("Acceso denegado")
        else:
            cargar_tareas(usuario_actual)
            menu = False
            log = True
    elif opcion == "3":
        print("Nos vemos luego")
        menu = False
    else:
        print("Opción no válida")
        logging.warning("Selección inválida")
    if menu:
        opcion = input("Selecciona una opción: ")

while log:
    print(f"\nBienvenido a MyTask, {usuario_actual}")
    print("\n1) Ver mis tareas")
    print("2) Crear una tarea")
    print("3) Eliminar una tarea")
    print("4) Editar una tarea")
    print("5) Cambiar estado de una tarea")
    print("6) Ver tareas completadas")
    print("7) Buscar tarea")
    print("8) Salir del programa")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        listar_tareas(usuario_actual)
        tareas_usuario = obtener_tareas()  # Obtener la lista de tareas del usuario

        if not tareas_usuario:  # Si no hay tareas, regresar al menú principal
            print("No tienes tareas pendientes.")
            continue  # Volver al menú principal
        
        print("\nOpciones:")
        print("1. Ver detalles de una tarea")
        print("2. Volver al menú principal")
        subopcion = input("Selecciona una opción: ")

        if subopcion == "1":
            tarea_num = int(input("Número de la tarea que quieres ver: ")) - 1
            listar_tareas(usuario_actual, detalle=True, tarea_num=tarea_num)
        elif subopcion == "2":
            continue
        else:
            print("Opción no válida")
            logging.warning("Selección inválida en el menú de tareas")
    elif opcion == "2":
        crear_tarea(usuario_actual)
        guardar_tareas(usuario_actual)
    elif opcion == "3":
        eliminar_tarea(usuario_actual)
        guardar_tareas(usuario_actual)
    elif opcion == "4":
        editar_tarea(usuario_actual)
        guardar_tareas(usuario_actual)
    elif opcion == "5":
        cambiar_estado(usuario_actual)
        guardar_tareas(usuario_actual)
    elif opcion == "6":
        tareas_completadas(usuario_actual)
    elif opcion == "7":
        filtro = input("Ingresa un término para buscar (título, etiqueta, estado o fecha de vencimiento): ")
        buscar_tareas(filtro)
    elif opcion == "8":
        print("Hasta luego!")
        log = False
    else:
        print("Opción no válida")
        logging.warning("Selección inválida")
