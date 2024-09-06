import os
import json
import logging
import hashlib

tareas = []
completadas = []

def cargar_tareas():
    global tareas, completadas
    if os.path.exists("tareas.json"):
        with open("tareas.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict):
                tareas = data.get("tareas", [])
                completadas = data.get("completadas", [])
            else:
                tareas = data
                completadas = []

def guardar_tareas():
    with open("tareas.json", "w") as file:
        data = {
            "tareas": tareas,
            "completadas": completadas
        }
        json.dump(data, file, indent=4)

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

def listar_tareas(op):
    for idx, tarea in enumerate(tareas, 1):
        print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['fecha_vencimiento']}")
    if op == "1":
        while True:
            print("\nOpciones:")
            print("1. Ver detalles de una tarea")
            print("2. Volver al menú principal")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                while True:
                    id_tarea = input("Ingrese el número de la tarea para ver los detalles o '0' para volver al menú: ")
                    if id_tarea.isdigit() and int(id_tarea) in range(1, len(tareas) + 1):
                        id_tarea = int(id_tarea) - 1
                        tarea = tareas[id_tarea]
                        print("\nDetalles de la tarea:")
                        print(f"Título: {tarea['titulo']}")
                        print(f"Descripción: {tarea['descripcion']}")
                        print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
                        print(f"Etiqueta: {tarea['etiqueta']}")
                        print(f"Estado: {tarea['estado']}")
                        break
                    elif id_tarea == "0":
                        return
                    else:
                        print("ID de tarea inválido. Intente de nuevo.")
            elif opcion == "2":
                return
            else:
                print("Opción no válida. Intente de nuevo.")

def tareas_completadas():
    if not completadas:
        print("No hay tareas completadas.")
    else:
        print("\nTareas Completadas:")
        for idx, tarea in enumerate(completadas, 1):
            print(f"{idx}. {tarea['titulo']} - {tarea['fecha_vencimiento']} - {tarea['etiqueta']}")
        print("\n")

def editar_tarea(op):
    listar_tareas(op)
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

def eliminar_tarea(op):
    listar_tareas(op)
    indice = int(input("Numero de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        guardar_tareas()
        logging.info(f"Tarea eliminada: {tarea['titulo']}")
    else:
        print("indice invalido")
        logging.warning("Intento de eliminacion con indice invalido")

def cambiar_estado(op):
    listar_tareas(op)
    indice = int(input("Numero de la tarea a cambiar estado: ")) - 1
    if 0 <= indice < len(tareas):
        estado = input("Nuevo estado (pendiente, en progreso, completada): ")
        tareas[indice]["estado"] = estado
        if estado.lower() == "completada" or estado.lower() == "completado":
            logging.info(f"Estado de la tarea ha cambiado: {tareas[indice]['titulo']} a {estado}")
            print("pase a los completados")
            completadas.append(tareas[indice])
            del tareas[indice]
            guardar_tareas()
        else:
            logging.info(f"Estado de la tarea ha cambiado: {tareas[indice]['titulo']} a {estado}")
            guardar_tareas()
    else:
        print("indice invalido")
        logging.warning("Intento de cambio de estado con indice invalido")

def buscar_tareas(filtro):
    filtro = filtro.lower()
    resultados = [
        tarea for tarea in tareas + completadas
        if filtro in tarea['titulo'].lower() 
        or filtro in tarea['etiqueta'].lower() 
        or filtro in tarea['fecha_vencimiento']
    ]
    if resultados:
        for idx, tarea in enumerate(resultados, 1):
            print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['fecha_vencimiento']}")
    else:
        print("No se encontraron tareas que coincidan con el filtro.")
