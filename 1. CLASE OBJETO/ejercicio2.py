class Animal:
#metodo Constructor
    def __init__(self, nombre, edad,raza,alimento,color):
        self.nombre= nombre
        self.edad= edad
        self.raza= raza
        self.alimento= alimento
        self.color= color
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Animal")
        print("Nombre: " +self.nombre)
        print("edad:" +self.edad)
        print("raza:" +self.raza)
        print("alimento:" +self.alimento)
        print("color:" +self.color)
        print("-----------------------------")
    
    #metodo del animal
    def comer(self):
        print("El Animal "+self.nombre+" esta comiendo")
        print("-----------------------------------------------")
        
    def dormir(self):
        print("El Animal "+self.nombre+" esta dormido")
        print("-----------------------------------------------")
       
        
        
        
        
#Creamos los Objetos a partir de instanciar la clase Animal       
animal1=Animal("Lucas","3 años", "Belier", "Legumbres", "Blanco")
animal2=Animal("Doky","2 años", "Siames", "Alimento para Gato", "Negro")
animal3=Animal("Max","5 años", "Labrador", "Croquetas", "Cafe")


#Imprimo los detalles de cada objeto
animal1.mostrar_detalles()
animal2.mostrar_detalles()
animal3.mostrar_detalles()

animal1.comer()
animal2.comer()
animal3.comer()

animal1.dormir()
animal2.dormir()
animal3.dormir()






        