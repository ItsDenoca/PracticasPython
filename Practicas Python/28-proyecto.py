import os

CARPETA = "contactos/" # Carpeta de contactos

def app():

    crear_directorio()


def crear_directorio():
    if not os.path.exists("contactos/"):
        # Crear la carpeta
        os.makedirs("contactos/")
    else:
        print("La carpeta ya existe")
