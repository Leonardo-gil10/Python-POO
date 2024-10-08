class Carro:
#metodo Constructor
    def __init__(self, marca, modelo,color,año,puertas):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.año= año
        self.puertas= puertas
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Carro")
        print("Marca: " +self.marca)
        print("modelo:" +self.modelo)
        print("color:" +self.color)
        print("año:" +self.año)
        print("puertas:" +self.puertas)
        print("-----------------------------")
    
    #metodo encender
    def encender(self):
        print("El Carro "+self.modelo+" esta encendido")
        print("-----------------------------------------------")
        
    #metodo Apagar    
    def apagar(self):
        print("El Carro "+self.modelo+" esta apagado")
        print("-----------------------------------------------")
        
        
        
#Creamos los Objetos a partir de instanciar la clase CARRO      
carro1=Carro("Toyota","Higlander", "Plateado", "2022", "5")
carro2=Carro("Porshe","911", "Rojo", "1973", "2")
carro3=Carro("Tesla","Model 3", "Negro", "2024", "4")


#Imprimo los detalles de cada objeto
carro1.mostrar_detalles()
carro2.mostrar_detalles()
carro3.mostrar_detalles()

carro1.encender()
carro2.encender()
carro3.encender()

carro1.apagar()
carro2.apagar()
carro3.apagar()

