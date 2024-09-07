import os
import json
import logging

tareas = []
completadas = []

def cargar_tareas(usuario):
    global tareas, completadas
    archivo_tareas = "tareas.json"
    if os.path.exists(archivo_tareas):
        with open(archivo_tareas, "r") as file:
            data = json.load(file)
            tareas_usuario = data.get(usuario, {})
            tareas = tareas_usuario.get("tareas", [])
            completadas = tareas_usuario.get("completadas", [])
    else:
        tareas = []
        completadas = []

def guardar_tareas(usuario):
    archivo_tareas = "tareas.json"
    if os.path.exists(archivo_tareas):
        with open(archivo_tareas, "r") as file:
            data = json.load(file)
    else:
        data = {}

    data[usuario] = {
        "tareas": tareas,
        "completadas": completadas
    }

    with open(archivo_tareas, "w") as file:
        json.dump(data, file, indent=4)

def obtener_tareas():
    """Retorna la lista de tareas actuales."""
    return tareas

def crear_tarea(usuario):
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
    etiqueta = input("Etiqueta (Urgente, Importante, Trabajo, etc): ")
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_vencimiento": fecha_vencimiento,
        "etiqueta": etiqueta,
        "estado": "pendiente"
    }
    cargar_tareas(usuario)
    tareas.append(tarea)
    guardar_tareas(usuario)
    logging.info(f"Tarea creada: {titulo}")

def listar_tareas(usuario, detalle=False, tarea_num=None):
    cargar_tareas(usuario)
    tareas_a_mostrar = tareas if not detalle else [tareas[tarea_num]] if tarea_num is not None else tareas

    if tareas_a_mostrar:
        for idx, tarea in enumerate(tareas_a_mostrar, 1):
            if detalle and tarea_num is not None:  # Mostrar detalles completos de la tarea seleccionada
                print(f"Título: {tarea['titulo']}")
                print(f"Estado: {tarea['estado']}")
                print(f"Etiqueta: {tarea['etiqueta']}")
                print(f"Fecha de vencimiento: {tarea['fecha_vencimiento']}")
                print(f"Descripción: {tarea['descripcion']}")
                print()
            else:
                print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['etiqueta']} - {tarea['fecha_vencimiento']}")
    else:
        print("No hay tareas para mostrar.")
        return False  # Indicamos que no hay tareas disponibles

    return True  # Indicamos que hay tareas disponibles


def tareas_completadas(usuario):
    cargar_tareas(usuario)
    if not completadas:
        print("No hay tareas completadas.")
    else:
        print("\nTareas Completadas:")
        for idx, tarea in enumerate(completadas, 1):
            print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['etiqueta']} - {tarea['fecha_vencimiento']}")
        print("\n")

def editar_tarea(usuario):
    if not listar_tareas(usuario):
        return  # Regresa al menú principal si no hay tareas disponibles

    indice = int(input("Número de la tarea a editar: ")) - 1
    if 0 <= indice < len(tareas):
        tarea = tareas[indice]
        titulo = input(f"Título [{tarea['titulo']}]: ") or tarea['titulo']
        descripcion = input(f"Descripción [{tarea['descripcion']}]: ") or tarea['descripcion']
        fecha_vencimiento = input(f"Fecha de vencimiento [{tarea['fecha_vencimiento']}]: ") or tarea['fecha_vencimiento']
        etiqueta = input(f"Etiqueta [{tarea['etiqueta']}]: ") or tarea['etiqueta']
        tarea.update({
            "titulo": titulo,
            "descripcion": descripcion,
            "fecha_vencimiento": fecha_vencimiento,
            "etiqueta": etiqueta
        })
        guardar_tareas(usuario)
        logging.info(f"Tarea editada: {tarea['titulo']}")
    else:
        print("Índice inválido")
        logging.warning("Intento de edición con índice inválido")

def eliminar_tarea(usuario):
    if not listar_tareas(usuario):
        return  # Regresa al menú principal si no hay tareas disponibles

    indice = int(input("Número de la tarea a eliminar: ")) - 1
    if 0 <= indice < len(tareas):
        tarea = tareas.pop(indice)
        guardar_tareas(usuario)
        logging.info(f"Tarea eliminada: {tarea['titulo']}")
    else:
        print("Índice inválido")
        logging.warning("Intento de eliminación con índice inválido")

def cambiar_estado(usuario):
    if not listar_tareas(usuario):
        return  # Regresa al menú principal si no hay tareas disponibles

    indice = int(input("Número de la tarea a cambiar estado: ")) - 1
    if 0 <= indice < len(tareas):
        estado = input("Nuevo estado (pendiente, en progreso, completada): ").lower()
        tareas[indice]["estado"] = estado
        if estado == "completada":
            logging.info(f"Estado de la tarea ha cambiado: {tareas[indice]['titulo']} a {estado}")
            completadas.append(tareas[indice])
            del tareas[indice]
            guardar_tareas(usuario)
        else:
            logging.info(f"Estado de la tarea ha cambiado: {tareas[indice]['titulo']} a {estado}")
            guardar_tareas(usuario)
    else:
        print("Índice inválido")
        logging.warning("Intento de cambio de estado con índice inválido")

def buscar_tareas(filtro):
    filtro = filtro.lower()
    resultados = [
        tarea for tarea in tareas + completadas
        if filtro in tarea['titulo'].lower() 
        or filtro in tarea['etiqueta'].lower() 
        or filtro in tarea['estado'].lower()  # Filtro también por estado
        or filtro in tarea['fecha_vencimiento']
    ]
    if resultados:
        for idx, tarea in enumerate(resultados, 1):
            print(f"{idx}. {tarea['titulo']} - {tarea['estado']} - {tarea['etiqueta']} - {tarea['fecha_vencimiento']}")
    else:
        print("No se encontraron tareas que coincidan con el filtro.")
