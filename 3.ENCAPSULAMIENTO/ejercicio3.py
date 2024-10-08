# Clase Producto con atributos encapsulados o privados
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo     # Atributo privado
        self.__autor = autor     # Atributo privado
        self.__isbn = isbn   # Atributo privado
        self.editorial = editorial # Atributo público

    # Método getter 
    def obtener_titulo(self):
        return self.__titulo

    # Método getter 
    def obtener_autor(self):
        return self.__autor
    
     # Método getter 
    def obtener_isbn(self):
        return self.__isbn

    # Método setter 
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Método setter 
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor
        
    # Método setter 
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    # Método para mostrar los detalles del producto
    def mostrar_detalles(self):
        print(f"\nTitulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Isbn: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# objeto
libro = Libro("Contabilidad financiera", "Hector Atoche", 978-6071508437 , "RMcGraw-Hill Education")

# 
libro.mostrar_detalles()

print("----------------------")

# imprimir atributos encapsulado
libro.establecer_titulo("Introducción a la Contabilidad")
print(f"\nTitulo: {libro.obtener_titulo() }") 
libro.establecer_autor("Horngren, Eliot")
print(f"Autor: {libro.obtener_autor() }")
libro.establecer_isbn("607504539")
print(f"Isbn: {libro.obtener_isbn() }")
print(f"Editorial: {libro.editorial }")