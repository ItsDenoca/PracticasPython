#nombre = input("¿Cual es tu nombre?")

#print(f"Hola{nombre}")

print(2 % 2)

# Leer datos que seran numeros

edad = input("¿Cual es tu edad?")

# Convertir edad string a entero
edad = int(edad)

if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aun no puedes votar")

# Mezclarlo con operadores
numero = input("Agrega un numero y te dire si es par o non\r\n")

numero = int(numero)

if numero % 2 == 0:
    print(f"El {numero} es par")
else:
    print(f"El numero {numero} es impar")
    