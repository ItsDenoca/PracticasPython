class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio # Default: Public, PROTECTED (1 guion bajo), PRIVATE(2 guiones bajos)
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}" )
        
        # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor o lo modifica
    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

# Crear una clase hijo de Restaurant ESTO ES UNA HERENCIA
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    # Reescribir un metodo (debe de llamarse igual)
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca} ")

    # Agregar un metodo que solo exista en Hotel
    def get_alberca(self):
        return self.alberca

hotel = Hotel("Hotel POO", "5 estrellas", 200, "Si")
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
