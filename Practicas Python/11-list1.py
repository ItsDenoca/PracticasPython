# LISTAS 
lenguajes = ["Python", "Kotlin", "Java", "Javascript"]

print(lenguajes)

# Los arrays (lists) comienzan en la posicion 0
print(lenguajes[0])

# Ordenar elementos
lenguajes.sort() # Con la funcion sort tus elementos se ordenan alfabeticamente
print(lenguajes)

# Acceder a un elemento dentro de un texto
aprendiendo = f"Estoy aprendiendo{lenguajes}"
print(aprendiendo)

# Modificando valores de un arreglo
lenguajes[2] = "PHP"
print(lenguajes)

# Agregar elementos a un arreglo (list)
lenguajes.append("Ruby")
print(lenguajes)

# Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar de un arreglo (list)
lenguajes.pop() # .pop eliminta el ultimo elemento
print(lenguajes)

# Eliminar con .pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)

