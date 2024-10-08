class Figurasgeometricas:
#metodo Constructor
    def __init__(self, nombre,lado,vertice):
        self.nombre= nombre
        self.lado= lado
        self.vertice= vertice
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion de las Figuras Geometricas")
        print("Nombre: " +self.nombre)
        print("lado:" +self.lado)
        print(":" +self.vertice)
        print("-----------------------------")
    
    #metodo del animal
    def mostrar(self):
        print("la figura "+self.nombre+" debe mostrar")
        print("-----------------------------------------------")
        
        
        
#Creamos los Objetos a partir de instanciar la clase Celular       
figurageometrica1=Figurasgeometricas("Hexagono"," 6 lados", "6 vertice")
figurageometrica2=Figurasgeometricas("Recatangulo","4 lados", "4 lados")
figurageometrica3=Figurasgeometricas("Cuadrado","4 lados", "4 Lados")

