# Clase Médico
class Medico:
    def __init__(self, nombre, especialidad, hospital):
        self.nombre = nombre
        self.especialidad = especialidad
        self.hospital = hospital

    def trabajar(self):
        print(f"El Dr. {self.nombre}, especializado en {self.especialidad}, trabaja en el hospital {self.hospital}.")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombre, rama, empresa):
        self.nombre = nombre
        self.rama = rama
        self.empresa = empresa

    def trabajar(self):
        print(f"El ingeniero {self.nombre}, especializado en {self.rama}, trabaja en la empresa {self.empresa}.")

# Clase Docente
class Docente:
    def __init__(self, nombre, asignatura, institucion):
        self.nombre = nombre
        self.asignatura = asignatura
        self.institucion = institucion

    def trabajar(self):
        print(f"El profesor {self.nombre} imparte la asignatura de {self.asignatura} en la institución {self.institucion}.")

# Función que muestra el trabajo de cada profesional (polimorfismo)
def describir_trabajo(profesional):
    profesional.trabajar()

# Creación de objetos de cada clase
medico = Medico("Ana Pérez", "Cardiología", "Hospital Central")
ingeniero = Ingeniero("Carlos López", "Ingeniería Civil", "Constructora ABC")
docente = Docente("María Gómez", "Matemáticas", "Colegio Nacional")

# Llamado al método trabajar() para cada objeto
describir_trabajo(medico)
describir_trabajo(ingeniero)
describir_trabajo(docente)
