import os
import json
import hashlib
import logging

usuarios = {}

def cargar_usuarios():
    global usuarios
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)

def guardar_usuarios():
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

def registrar():
    print("--- Registro de nuevo usuario ---")
    while True:
        usuario = input("Nombre de usuario: ").strip()
        if not usuario:
            print("El nombre de usuario no puede estar vacío. Inténtalo de nuevo.")
            continue
        if usuario in usuarios:
            print("El nombre de usuario ya existe.")
            logging.warning(f"Intento de registro con nombre de usuario ya existente: {usuario}")
            return False
        break

    while True:
        contraseña = input("Contraseña: ").strip()
        if not contraseña:
            print("La contraseña no puede estar vacía. Inténtalo de nuevo.")
            continue
        break

    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    usuarios[usuario] = hash_contraseña
    guardar_usuarios()
    logging.info(f"Usuario registrado: {usuario}")
    return True

def autenticar():
    print("--- Inicio de sesión ---")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

    if usuario in usuarios and usuarios[usuario] == hash_contraseña:
        print(f"Bienvenido, {usuario}!")
        logging.info(f"Usuario autenticado: {usuario}")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
        logging.warning(f"Falló inicio de sesión para el usuario: {usuario}")
        return None
