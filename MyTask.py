import os
import sys
import json
import logging
from datetime import datetime
import hashlib

#Logs como un registro de auditoria con fecha y la accion que se realizo
logging.basicConfig(filename='Operaciones.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

usuarios = {}
tareas = []

#Aqui se cargan los usuarios desde el archivo
def cargar_usuarios():
    global usuarios
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)

#Funcion para guardar usuarios en un archivo de manera local
def guardar_usuarios():
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

#Funcion para cargar tareas desde un archivo local
def cargar_tareas():
    global tareas
    if os.path.exists("tareas.json"):
        with open("tareas.json", "r") as file:
            tareas = json.load(file)

#Aqui se guardan las tareas como base de datos local
def guardar_tareas():
    with open("tareas.json", "w") as file:
        json.dump(tareas, file, indent=4)

#Funcion para registrar un nuevo usuario con nombre y contrasena
def registrar():
    print("--- Registro de nuevo usuario ---")
    print("---------------------------------")
    usuario = input("Nombre de usuario: ")
    if usuario in usuarios:
        print("El nombre de usuario ya existe.")
        logging.warning(f"Intento de registro con nombre de usuario ya existente a: {usuario}")
        return False

    contraseña = input("Contraseña: ")
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    usuarios[usuario] = hash_contraseña
    guardar_usuarios()
    logging.info(f"Usuario registrado: {usuario}")
    return True

#Funcion para autenticación de usuario
def autenticar():
    print("--- Inicio de sesion ---")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

    if usuario in usuarios and usuarios[usuario] == hash_contraseña:
        logging.info(f"Autenticacion exitosa para el usuario: {usuario}")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        logging.warning(f"Fallo de autenticacion para el usuario: {usuario}")
        return False

#Funcion para crear una tarea con estado pendiente por defecto
def crear_tarea():
    titulo = input("Titulo de la tarea: ")
    descripcion = input("Descripcion: ")
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
    etiqueta = input("Etiqueta (Urgente, Importante, Trabajo, etc): ")
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_vencimiento": fecha_vencimiento,
        "etiqueta": etiqueta,
        "estado": "pendiente"
    }
    tareas.append(tarea)
    guardar_tareas()
    logging.info(f"Tarea creada: {titulo}")

#Funcion para listar tareas con su titulom, el estado y fecha de vencimiento
def listar_tareas():
    for idx, tarea in enumerate(tareas, 1):
        print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['fecha_vencimiento']}")

#Funcion para editar una tarea segun lo que se requiera cambiar
def editar_tarea():
    listar_tareas()
    indice = int(input("Numero de la tarea a editar: ")) - 1
    if 0 <= indice < len(tareas):
        tarea = tareas[indice]
        titulo = input(f"Titulo [{tarea['titulo']}]: ") or tarea['titulo']
        descripcion = input(f"Descripcion [{tarea['descripcion']}]: ") or tarea['descripcion']
        fecha_vencimiento = input(f"Fecha de vencimiento [{tarea['fecha_vencimiento']}]: ") or tarea['fecha_vencimiento']
        etiqueta = input(f"Etiqueta [{tarea['etiqueta']}]: ") or tarea['etiqueta']
        tarea.update({
            "titulo": titulo,
            "descripcion": descripcion,
            "fecha_vencimiento": fecha_vencimiento,
            "etiqueta": etiqueta
        })
        guardar_tareas()
        logging.info(f"Tarea editada: {tarea['titulo']}")
    else:
        print("Índice inválido")
        logging.warning("Intento de edicion con indice invalido")

#Funcion para eliminar una tarea
def eliminar_tarea():
    listar_tareas()
    indice = int(input("Numero de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        guardar_tareas()
        logging.info(f"Tarea eliminada: {tarea['titulo']}")
    else:
        print("indice invalido")
        logging.warning("Intento de eliminacion con indice invalido")

#Funcion para cambiar el estado de una tarea
def cambiar_estado_tarea():
    listar_tareas()
    indice = int(input("Numero de la tarea a cambiar estado: ")) - 1
    if 0 <= indice < len(tareas):
        estado = input("Nuevo estado (pendiente, en progreso, completada): ")
        tareas[indice]["estado"] = estado
        guardar_tareas()
        logging.info(f"Estado de la tarea ha cambiado: {tareas[indice]['titulo']} a {estado}")
    else:
        print("indice invalido")
        logging.warning("Intento de cambio de estado con indice invalido")

#Aqui simulamos toda la interaccion del usuario
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
    print("\n")
    print("Bienvenido a MyTask")
    print("\n")
    print("1) Ver mis tareas")
    print("2) Crear una tarea")
    print("3) Eliminar una tarea")
    print("4) Editar una tarea")
    print("5) Cambiar estado de una tarea")
    print("6) Salir del programa")
    opcion = input("\nSelecciona una opción: ")
    if opcion == "1":
        print("Lista de las tareas actuales")
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
        print("Nos vemos luego")
        log = False
    else:
        print("Opción no válida")
        logging.warning("Seleccion de opcion no valida")
