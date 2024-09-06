import logging
from usuarios import cargar_usuarios, guardar_usuarios, registrar, autenticar
from tareas import cargar_tareas, guardar_tareas, crear_tarea, listar_tareas, editar_tarea, eliminar_tarea, cambiar_estado_tarea, buscar_tareas

#Logs como un registro de auditoria con fecha y la accion que se realizo
logging.basicConfig(filename='Operaciones.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

log = False
menu = True
cargar_usuarios()
cargar_tareas()

print("1. Iniciar sesion")
print("2. Registrarse")
print("3. Salir")
opcion = input("Selecciona una opcion: ")

while menu:
    if opcion == "1":
        if not autenticar():
            print("Acceso denegado")
        else:
            menu = False
            log = True
    elif opcion == "2":
        if not registrar():
            print("Error en el registro")
        print("Registrado con exito. Ahora inicia sesion.")
        if not autenticar():
            print("Acceso denegado")
        else:
            menu = False
            log = True
    elif opcion == "3":
        print("Nos vemos luego")
        menu = False
    else:
        print("Opción no valida")
        logging.warning("Selección invalida")

while log:
    print("\nBienvenido a MyTask")
    print("\n1) Ver mis tareas")
    print("2) Crear una tarea")
    print("3) Eliminar una tarea")
    print("4) Editar una tarea")
    print("5) Cambiar estado de una tarea")
    print("6) Buscar tarea")
    print("7) Salir del programa")
    opcion = input("\nSelecciona una opción: ")
    if opcion == "1":
        listar_tareas()
    elif opcion == "2":
        crear_tarea()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        editar_tarea()
    elif opcion == "5":
        cambiar_estado_tarea()
    elif opcion == "6":
        filtro = input("Ingresa un término para buscar: ")
        buscar_tareas(filtro)
    elif opcion == "7":
        print("Hasta luego!")
        log = False
    else:
        print("Opción no válida")
        logging.warning("Seleccion de opción no valida")
