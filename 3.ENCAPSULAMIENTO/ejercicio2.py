# Clase Producto con atributos encapsulados o privados
class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre     # Atributo privado
        self.__precio = precio     # Atributo privado
        self.cantidad = cantidad   # Atributo público
        self.categoria = categoria # Atributo público

    # Método getter 
    def obtener_nombre(self):
        return self.__nombre

    # Método getter 
    def obtener_precio(self):
        return self.__precio

    # Método setter 
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método setter 
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Método para mostrar los detalles del producto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# objeto
producto = Producto("Coca cola", 5000, 5, "Refresco")

# 
producto.mostrar_detalles()

print("----------------------")

# imprimir atributos encapsulado
producto.establecer_nombre("Leche")
print(f"\nNombres: {producto.obtener_nombre() }") 
producto.establecer_precio(3500)
print(f"Precio: {producto.obtener_precio() }")
print(f"Precio: {producto.cantidad }")
print(f"Precio: {producto.categoria }")