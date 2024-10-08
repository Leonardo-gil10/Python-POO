class Electrodomestico:
    # constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Digite el consumo electrico en kw:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("ELECTRODOMESTICO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("capacidad: ", self.capacidad)
        print("Consumo electrico: ", self.consumo_electrico)


class Refrigerador(Electrodomestico):  # subclase Refrigerador
    # constructor
    def __init__(self, marca, color, capacidad, tiporefrigerador):
        super().__init__(marca, color, capacidad)  # super clase heredada
        self.tiporefrigerador = tiporefrigerador  # atributo privado
        self.temperatura = int(input("Ingrese la temperatura: "))

    # método privado
    def ajustar(self):
        print("tiporefrigerador: ", self.tiporefrigerador)  # imprimiendo el tipo de refrigerador

        if self.temperatura > 10:
            print("--------------------")
            print(f"El electrodomestico {self.marca}, de color {self.color} con capacidad {self.capacidad} tiene una temperatura estable!!")
        else:
            print("--------------------")
            print(f"El carro {self.marca}, con placa {self.placa} de color {self.color} no enciende!!")


# instanciando la subclase carro
objeto_refrigerador = Refrigerador('HACEB', 'GRIS', '2000LT', ' FROST')
objeto_refrigerador.registrar()
objeto_refrigerador.ajustar()