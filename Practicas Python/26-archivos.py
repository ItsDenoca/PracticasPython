def app():
    # Crear el archivo
    archivo = open("archivo.txt", "w") #W es un archivo de escritura, sino existe lo creara

    # Generar numeros en archivo
    for i in range (0, 20):
        archivo.write("Esta es la linea " + str(i) + "\r\n" )

    # Cerrar archivo
    archivo.close()

app()
