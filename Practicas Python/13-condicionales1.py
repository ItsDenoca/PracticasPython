# Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print("Puedes pagar")


balances = 0
if balances > 0:
    print("Puedes pagar")
else:     # El else se ejecuta cuando la condicion de arriba no se cumpla
    print("No tiene saldo")


# LIKES 
likes = 200
if likes >= 200:
    print("Excelente, 200 likes")
else:
    print("Casi llegas a los 200") 


# IF con texto
lenguaje = "PHP"
if not lenguaje == "Python":
    print("Excelente decision")

# Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado == True:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")


# Evaluar un elemnto de una lista
lenguajes = ["Python", "Kotlin", "Java", "Javascript"]
if "PHP" in lenguajes:
    print("PHP si existe")
else:
    print("No, no esta en la lista")


# IF anidados 
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("Acceso total")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")