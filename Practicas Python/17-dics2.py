# Iniciar un diccionario vacio
jugador = {}
print(jugador)

# Se une un jugador
jugador["nombre"] = "Denoca"
jugador["puntaje"] = 0
print(jugador)

# Incrementando el puntaje
jugador["puntaje"] = 200
print(jugador)


# Acceder a un valor
print(jugador.get("consola", "No existe el valor"))

# Iterar en el diccionario
for llave, valor in jugador.items():
    print(valor)


# Eliminar jugador y puntaje
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)

