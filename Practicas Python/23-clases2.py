class Restaurant:
    
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public, PROTECTED (1 guion bajo), PRIVATE(2 guiones bajos)
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}" )
        
        # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un valor o lo modifica
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio


# Instanciar la clase
restaurant = Restaurant("Pizzeria Mexico", "Comida Italiana", "$50")
#restaurant.__precio = 80 # De esta forma se pueden modificar los precios (ENCAPSULAMIENTO)
restaurant.mostrar_informacion()
restaurant.set_precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant("Hamburguesas Python", "Comida casual", "$40")

#restaurant2.__precio = 50 # No sera posible modificarlo con PRIVATE
restaurant2.mostrar_informacion()
restaurant2.set_precio(50)
restaurant2.get_precio()

