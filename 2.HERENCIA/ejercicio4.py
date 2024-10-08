class Electronico:
    # constructor
    def __init__(self, marca, modelo, tipoprocesador):
        self.marca = marca
        self.modelo = modelo
        self.tipoprocesador = tipoprocesador
        self.memoria_ram = int(input("Digite la cantidad de memoria en GB:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("ELECTRONICO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Tipoprocesador: ", self.tipoprocesador)
        print("Memoria_Ram: ", self.memoria_ram)


class Laptop(Electronico):  # subclase Refrigerador
    # constructor
    def __init__(self, marca, modelo, tipoprocesador, tipo_discoduro):
        super().__init__(marca, modelo, tipoprocesador)  # super clase heredada
        self.tipo_discoduro = tipo_discoduro  # atributo privado
        self.duracion_bateria = int(input("digite la durecion de la bateria en hr: "))

    # método privado
    def encender(self):
        print("tipo_discoduro: ", self.tipo_discoduro)  # imprimiendo el tipo de disco

        if self.duracion_bateria > 0:
            print("--------------------")
            print(f"El instrumento Electronico {self.marca}, Modelo {self.modelo} con tipo de procesador {self.tipoprocesador} esta encendido!!")
        else:
            print("--------------------")
            print(f"El Instrumento Electronico {self.marca}, Modelo {self.modelo} con tipo de procesador {self.tipoprocesador} no enciende!!")


# instanciando la subclase Smartphone
objeto_laptop = Laptop('HP ', 'LENOVO', 'INTEL CORE 3', ' Disco SSD')
objeto_laptop.registrar()
objeto_laptop.encender()