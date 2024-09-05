from pymongo import MongoClient
from bson.objectid import ObjectId

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gestor_de_tareas']
collection = db['tareas']

# Función para simular el inicio de sesión
def iniciar_sesion():
    global sesion_iniciada, usuario_actual
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    if nombre_usuario:
        sesion_iniciada = True
        usuario_actual = nombre_usuario
        print(f"Loggeado como {nombre_usuario}")
    else:
        print("Logeo fallido. Por favor ingresa un nombre de usuario válido.")

# Función para cerrar sesión
def cerrar_sesion():
    global sesion_iniciada, usuario_actual
    sesion_iniciada = False
    usuario_actual = None
    print("Sesión cerrada correctamente.")

# Función para agregar una tarea
def agregar_tarea():
    if not sesion_iniciada:
        print("Por favor, inicia sesión primero.")
        return
    titulo = input("Ingresa el título de la tarea: ")
    descripcion = input("Ingresa la descripción de la tarea: ")
    fecha_vencimiento = input("Ingresa la fecha de vencimiento (YYYY-MM-DD): ")
    etiqueta = input("Ingresa la etiqueta de la tarea (urgente, trabajo, personal, otros): ")
    tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'fecha_vencimiento': fecha_vencimiento,
        'etiqueta': etiqueta,
        'estado': 'pendiente'
    }
    collection.insert_one(tarea)
    print(f"Tarea '{titulo}' agregada exitosamente.")

# Función para listar todas las tareas
def listar_tareas():
    if not sesion_iniciada:
        print("Por favor, inicia sesión primero.")
        return
    tareas = collection.find()
    if not tareas:
        print("No se encontraron tareas.")
        return
    for idx, tarea in enumerate(tareas, start=1):
        print(f"{idx}. {tarea['titulo']} - {tarea['descripcion']} - Vence: {tarea['fecha_vencimiento']} - Etiqueta: {tarea['etiqueta']} - Estado: {tarea['estado']}")

# Función para actualizar una tarea
def actualizar_tarea():
    if not sesion_iniciada:
        print("Por favor, inicia sesión primero.")
        return
    id_tarea = input("Ingresa el ID de la tarea que deseas actualizar (ObjectId en formato hexadecimal): ")
    if ObjectId.is_valid(id_tarea):
        tarea = collection.find_one({'_id': ObjectId(id_tarea)})
        if tarea:
            titulo = input(f"Ingresa el nuevo título (actual: {tarea['titulo']}): ") or tarea['titulo']
            descripcion = input(f"Ingresa la nueva descripción (actual: {tarea['descripcion']}): ") or tarea['descripcion']
            fecha_vencimiento = input(f"Ingresa la nueva fecha de vencimiento (YYYY-MM-DD) (actual: {tarea['fecha_vencimiento']}): ") or tarea['fecha_vencimiento']
            etiqueta = input(f"Ingresa la nueva etiqueta (urgente, trabajo, personal, otros) (actual: {tarea['etiqueta']}): ") or tarea['etiqueta']
            estado = input(f"Ingresa el nuevo estado (pendiente, en_progreso, completada) (actual: {tarea['estado']}): ") or tarea['estado']
            
            collection.update_one(
                {'_id': ObjectId(id_tarea)},
                {'$set': {
                    'titulo': titulo,
                    'descripcion': descripcion,
                    'fecha_vencimiento': fecha_vencimiento,
                    'etiqueta': etiqueta,
                    'estado': estado
                }}
            )
            print(f"Tarea {id_tarea} actualizada exitosamente.")
        else:
            print("Tarea no encontrada.")
    else:
        print("ID de tarea no válido.")

# Función para eliminar una tarea
def eliminar_tarea():
    if not sesion_iniciada:
        print("Por favor, inicia sesión primero.")
        return
    id_tarea = input("Ingresa el ID de la tarea que deseas eliminar (ObjectId en formato hexadecimal): ")
    if ObjectId.is_valid(id_tarea):
        result = collection.delete_one({'_id': ObjectId(id_tarea)})
        if result.deleted_count > 0:
            print(f"Tarea {id_tarea} eliminada exitosamente.")
        else:
            print("Tarea no encontrada.")
    else:
        print("ID de tarea no válido.")

# Menú de la aplicación
def mostrar_menu():
    print("\nGestión de Tareas CLI")
    print("1. Iniciar sesión")
    print("2. Cerrar sesión")
    print("3. Agregar tarea")
    print("4. Listar tareas")
    print("5. Actualizar tarea")
    print("6. Eliminar tarea")
    print("7. Salir")

# Función principal
def main():
    while True:
        mostrar_menu()
        eleccion = input("Elige una opción: ")
        
        if eleccion == '1':
            iniciar_sesion()
        elif eleccion == '2':
            cerrar_sesion()
        elif eleccion == '3':
            agregar_tarea()
        elif eleccion == '4':
            listar_tareas()
        elif eleccion == '5':
            actualizar_tarea()
        elif eleccion == '6':
            eliminar_tarea()
        elif eleccion == '7':
            print("Saliendo de la aplicación. ¡Adiós!")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
