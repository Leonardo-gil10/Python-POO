class Reloj:
    # constructor
    def __init__(self, marca, tiporeloj, material):
        self.marca = marca
        self.tiporeloj = tiporeloj
        self.material = material
        self.precio_reloj = int(input("Digite el precio del Reloj:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("RELOJ REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Tiporeloj: ", self.tiporeloj)
        print("Material: ", self.material)
        print("Precio_reloj: ", self.precio_reloj)


class Relojinteligente(Reloj):  # subclase Refrigerador
    # constructor
    def __init__(self, marca, tiporeloj, material, tipo_pantalla):
        super().__init__(marca, tiporeloj, material)  # super clase heredada
        self.tipo_pantalla = tipo_pantalla  # atributo privado
        self.sistema_operativo = input("Ingrese el sistema operativo: ")

    # metodo encender
    def encender(self):
        respuesta = input("¿Deseas encender el reloj? (si/no): ")
        if respuesta.lower() == "si":
            print(f"El reloj {self.marca}, de material {self.material} con tipo de pantalla {self.tipo_pantalla} se está encendiendo.")
        else:
            print(f"El reloj {self.marca}, de material {self.material} con tipo de pantalla {self.tipo_pantalla} no se puede encender.")



# instanciando la subclase Smartphone
objeto_relojinteligente = Relojinteligente('HUAWEI WATCH ', 'BASICO', 'GROSOR ELASTICO', ' OLED')
objeto_relojinteligente.registrar()
objeto_relojinteligente.encender()