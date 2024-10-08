# Clase padre Vehiculo
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def descripcion(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase Carro (hereda de Vehiculo)
class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca)
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        print(f"Este es un carro de la marca {self.marca}, modelo {self.modelo}, año {self.anio}.")

# Clase Moto (hereda de Vehiculo)
class Moto(Vehiculo):
    def __init__(self, marca, cilindrada):
        super().__init__(marca)
        self.cilindrada = cilindrada

    def descripcion(self):
        print(f"Esta es una moto de la marca {self.marca} con una cilindrada de {self.cilindrada} cc.")

# Clase Bicicleta (hereda de Vehiculo)
class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo, material):
        super().__init__(marca)
        self.tipo = tipo
        self.material = material

    def descripcion(self):
        print(f"Esta es una bicicleta de la marca {self.marca}, tipo {self.tipo}, fabricada en {self.material}.")

# Función que muestra la descripción del vehículo (polimorfismo)
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Creación de objetos de cada clase
carro = Carro("Toyota", "Corolla", 2020)
moto = Moto("Yamaha", 150)
bicicleta = Bicicleta("Trek", "Montaña", "Aluminio")

# Llamado al método descripcion() para cada objeto
mostrar_descripcion(carro)
mostrar_descripcion(moto)
mostrar_descripcion(bicicleta)
