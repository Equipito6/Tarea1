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
