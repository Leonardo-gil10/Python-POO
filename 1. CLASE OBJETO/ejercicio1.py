class Celular:
#metodo Constructor
    def __init__(self, marca, bateria,color,modelo,camara):
        self.marca= marca
        self.bateria= bateria
        self.color= color
        self.modelo= modelo
        self.camara= camara
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Celular")
        print("Marca: " +self.marca)
        print("bateria:" +self.bateria)
        print("color:" +self.color)
        print("modelo:" +self.modelo)
        print("camara:" +self.camara)
        print("-----------------------------")
    
    #metodo para Encender el celular
    def encender(self):
        self.energia = int(input("Digite el valor de la carga: "))
        
        if self.energia > 0 :
            print("El celular "+self.modelo+" se puede encender")
            print(f" |||||||| {self.energia} % de carga")
            print("-----------------------------------------------")
        else:
            print("El celular "+self.modelo+" no se puede encender" )
            
        
        
#Creamos los Objetos a partir de instanciar la clase Celular       
celular1=Celular("Xiaomi","80 %", "Azul", "Redmi Note 11", "128mpx")
celular2=Celular("Samsung", "75 %", "Negro", "Galaxy A20", "32MPX")
celular3=Celular("Apple", "100 %", "Gris", "iphone 11", "64mpx")


#Imprimo los detalles de cada objeto
celular1.mostrar_detalles()
celular2.mostrar_detalles()
celular3.mostrar_detalles()

celular1.encender()
celular2.encender()
celular3.encender()




        