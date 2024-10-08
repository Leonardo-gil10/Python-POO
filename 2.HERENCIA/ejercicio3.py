class Instrumento:
    # constructor
    def __init__(self, tipodeinstrumento, marca, materialfabricacion):
        self.tipodeinstrumento = tipodeinstrumento
        self.marca = marca
        self.materialfabricacion = materialfabricacion
        self.precio = int(input("Digite el precio del instrumento:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("INSTRUMENTO REGISTRADO")
        print("--------------------")
        print("Tipodeinstrumento: ", self.tipodeinstrumento)
        print("Marca: ", self.marca)
        print("Materialdefabricacion: ", self.materialfabricacion)
        print("Precio: ", self.precio)


class Guitarra(Instrumento):  # subclase Refrigerador
    # constructor
    def __init__(self, tipodeinstrumento, marca, materialdefabricacion, numero_cuerdas):
        super().__init__(tipodeinstrumento, marca, materialdefabricacion)  # super clase heredada
        self.numero_cuerdas = numero_cuerdas  # atributo privado
        self.acordesbasicos = input("Ingrese los acordes basicos conocidos: ")

    # método privado
    def tocar(self):
        print("numero_cuerdas: ", self.numero_cuerdas)  # imprimiendo el numero de cuerdas

        print("--------------------")
        print(f"El instrumento {self.tipodeinstrumento}, Marca {self.marca} material {self.materialfabricacion} Esta Sonando ♫♫♫ !!")
       

# instanciando la subclase carro
objeto_guitarra = Guitarra('clasica', 'Yamahac40', 'Madera', ' 8')
objeto_guitarra.registrar()
objeto_guitarra.tocar()