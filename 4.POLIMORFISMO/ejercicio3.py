# Clase padre Animal
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, raza, edad):
        super().__init__(nombre, edad)
        self.raza = raza

    def sonido(self):
        print(f"El perro {self.nombre}, de raza {self.raza} y con {self.edad} años, hace: ¡Guau Guau!")

# Clase Gato (hereda de Animal)
class Gato(Animal):
    def __init__(self, nombre, color, edad):
        super().__init__(nombre, edad)
        self.color = color

    def sonido(self):
        print(f"El gato {self.nombre}, de color {self.color} y con {self.edad} años, hace: ¡Miau Miau!")

# Clase Pájaro (hereda de Animal)
class Pajaro(Animal):
    def __init__(self, nombre, especie, edad):
        super().__init__(nombre, edad)
        self.especie = especie

    def sonido(self):
        print(f"El pájaro {self.nombre}, de la especie {self.especie} y con {self.edad} años, hace: ¡shii shii!")

# Función que hace que cualquier animal haga su sonido (polimorfismo)
def hacer_sonido(animal):
    animal.sonido()

# Creación de objetos de cada clase
perro = Perro("Max", "Labrador", 5)
gato = Gato("Luna", "Blanco", 3)
pajaro = Pajaro("kiwi", "Canario", 2)

# Llamado al método sonido() para cada objeto
hacer_sonido(perro)
hacer_sonido(gato)
hacer_sonido(pajaro)
