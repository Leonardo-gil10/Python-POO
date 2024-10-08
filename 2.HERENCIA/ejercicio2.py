class Dispositivo:
    # constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Digite el porcentaje de bateria en mah:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("DISPOSITIVO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
        print("Capacidad bateria: ", self.capacidad_bateria)


class Smartphone(Dispositivo):  # subclase Refrigerador
    # constructor
    def __init__(self, marca, modelo, año, sistemaoperativo):
        super().__init__(marca, modelo, año)  # super clase heredada
        self.sistemaoperativo = sistemaoperativo  # atributo privado
        self.tipoconectividad = int(input("Ingrese el tipo de conectividad: "))

    # método privado
    def encender(self):
        print("sistemaoperativo: ", self.sistemaoperativo)  # imprimiendo el sistema operativo

        if self.capacidad_bateria > 0:
            print("--------------------")
            print(f"El Dispositivo {self.marca}, Modelo {self.modelo} año {self.año} esta encendido!!")
        else:
            print("--------------------")
            print(f"El Dispositivo {self.marca}, Modelo {self.modelo} año {self.año} no enciende!!")


# instanciando la subclase Smartphone
objeto_smartphone = Smartphone('XIAOMI', 'REDMI NOTE 11', '2023', ' ANDROID')
objeto_smartphone.registrar()
objeto_smartphone.encender()