import os
import json
import logging

tareas = []

def cargar_tareas():
    global tareas
    if os.path.exists("tareas.json"):
        with open("tareas.json", "r") as file:
            tareas = json.load(file)

def guardar_tareas():
    with open("tareas.json", "w") as file:
        json.dump(tareas, file, indent=4)

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

def listar_tareas():
    for idx, tarea in enumerate(tareas, 1):
        print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['fecha_vencimiento']}")

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

def buscar_tareas(filtro):
    resultados = [tarea for tarea in tareas if filtro.lower() in tarea['titulo'].lower() or filtro.lower() in tarea['etiqueta'].lower()]
    if resultados:
        for idx, tarea in enumerate(resultados, 1):
            print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['fecha_vencimiento']}")
    else:
        print("No se encontraron tareas que coincidan con el filtro.")
