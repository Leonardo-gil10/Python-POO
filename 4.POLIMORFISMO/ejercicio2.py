# Clase Carro
class Carro:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        print(f"Este es un carro de la marca {self.marca}, modelo {self.modelo}, año {self.anio}.")

# Clase Moto
class Moto:
    def __init__(self, marca, cilindrada):
        self.marca = marca
        self.cilindrada = cilindrada

    def descripcion(self):
        print(f"Esta es una moto de la marca {self.marca} con una cilindrada de {self.cilindrada} cc.")

# Clase Bicicleta
class Bicicleta:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def descripcion(self):
        print(f"Esta es una bicicleta de tipo {self.tipo}, fabricada en {self.material}.")

# Función que muestra la descripción del vehículo 
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Creación de objetos de cada clase
carro = Carro("Toyota", "Corolla", 2020)
moto = Moto("Yamaha", 150)
bicicleta = Bicicleta("Montaña", "Aluminio")

# Llamado al método descripcion() para cada objeto
mostrar_descripcion(carro)
mostrar_descripcion(moto)
mostrar_descripcion(bicicleta)
