class Moto:
#metodo Constructor
    def __init__(self, marca, modelo,color,año,cilindraje):
        self.marca= marca
        self.modelo= modelo
        self.color= color
        self.año= año
        self.cilindraje= cilindraje
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion de la Moto")
        print("Marca: " +self.marca)
        print("modelo:" +self.modelo)
        print("color:" +self.color)
        print("año:" +self.año)
        print("cilindraje:" +self.cilindraje)
        print("-----------------------------")
    
    #metodo de la Moto
    def encender(self):
        print("La Moto "+self.marca+" esta encendida")
        print("-----------------------------------------------")
        
    def Apagar(self):
        print("La Moto "+self.marca+" esta Apagada")
        print("-----------------------------------------------")
        
        
        
#Creamos los Objetos a partir de instanciar la clase Moto       
moto1=Moto("Ducati","Panegale", "Rojo", "2023", "1103 cc")
moto2=Moto("BMW","R 1250", "Gris", "2022", "1254 cc")
moto3=Moto("Yamaha","Live wire", "Negro", "2024", "Electrica")



#Imprimo los detalles de cada objeto
moto1.mostrar_detalles()
moto2.mostrar_detalles()
moto3.mostrar_detalles()

moto1.encender()
moto2.encender()
moto3.encender()

moto1.Apagar()
moto2.Apagar()
moto3.Apagar()
