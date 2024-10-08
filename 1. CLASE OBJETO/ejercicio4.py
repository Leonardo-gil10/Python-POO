class Empleado:
#metodo Constructor
    def __init__(self, nombre, edad,cargo,salario,area):
        self.nombre= nombre
        self.edad= edad
        self.cargo= cargo
        self.salario= salario
        self.area= area
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Empleado")
        print("Nombre: " +self.nombre)
        print("edad:" +self.edad)
        print("cargo:" +self.cargo)
        print("salario:" +self.salario)
        print("area:" +self.area)
        print("-----------------------------")
    
    #metodo del Empleado
    def operar(self):
        print("El Empleado "+self.nombre+" esta Operando")
        print("-----------------------------------------------")
        
    def evaluar(self):
        print("El Empleado "+self.nombre+" esta Evaluando")
        print("-----------------------------------------------")
         
        
#Creamos los Objetos a partir de instanciar la clase Empleado       
empleado1=Empleado("Leonardo","30 años", "Auxliliar Contable", "1500000", "contable")
empleado2=Empleado("Jorge","26 años", "Administrador", "1300000", "Administracion")
empleado3=Empleado("Deimer","29 años", "Economista", "2000000", "Publicidad")


#Imprimo los detalles de cada objeto
empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()

empleado1.operar()
empleado2.operar()
empleado3.operar()

empleado1.evaluar()
empleado2.evaluar()
empleado3.evaluar()


