playlist = {} # Diccionario vacio
playlist["canciones"] = []

# Funcion principal
def app():

       # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input("¿Como deseas nombrar la playlist?\r\n")
        
        if nombre_playlist:
            playlist["nombre"] = nombre_playlist
            agregar_playlist = False   # Ya tenemos un nombre, desactivar el true
            
            agregar_canciones() # Mandar llamar la funcion para agregar canciones

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #Preguntar al usuario que cancion desean agregar
        nombre_playlist = playlist ["nombre"]

        pregunta =  f"\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n"
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'

        cancion = input(pregunta)
        if cancion == "X":
            # Dejar de agregar canciones
            agregar_cancion = False
            
            mostrar_resumen() #Mostrar resumen de la playlsist

        else:
            # Agregar canciones de la playlist
            playlist["canciones"].append(cancion)
    
def mostrar_resumen():
    nomnbre_playlist = playlist["nombre"]
    print(f"Playlist: {nomnbre_playlist} \r\n")
    print("Canciones:\r\n")
    for cancion in playlist["canciones"]:
        print(cancion)

app()
