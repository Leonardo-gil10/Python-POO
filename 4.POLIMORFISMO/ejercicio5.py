# Clase padre Profesional
class Profesional:
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def trabajar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

# Clase Médico (hereda de Profesional)
class Medico(Profesional):
    def __init__(self, nombre, especialidad, hospital, experiencia):
        super().__init__(nombre, experiencia)
        self.especialidad = especialidad
        self.hospital = hospital

    def trabajar(self):
        print(f"El Dr. {self.nombre}, especializado en {self.especialidad}, trabaja en el hospital {self.hospital} "
              f"y tiene {self.experiencia} años de experiencia.")

# Clase Ingeniero (hereda de Profesional)
class Ingeniero(Profesional):
    def __init__(self, nombre, rama, empresa, experiencia):
        super().__init__(nombre, experiencia)
        self.rama = rama
        self.empresa = empresa

    def trabajar(self):
        print(f"El ingeniero {self.nombre}, especializado en {self.rama}, trabaja en la empresa {self.empresa} "
              f"y tiene {self.experiencia} años de experiencia.")

# Clase Docente (hereda de Profesional)
class Docente(Profesional):
    def __init__(self, nombre, asignatura, institucion, experiencia):
        super().__init__(nombre, experiencia)
        self.asignatura = asignatura
        self.institucion = institucion

    def trabajar(self):
        print(f"El profesor {self.nombre} imparte la asignatura de {self.asignatura} en la institución {self.institucion} "
              f"y tiene {self.experiencia} años de experiencia.")

# Función que muestra el trabajo de cada profesional
def describir_trabajo(profesional):
    profesional.trabajar()

# Creación de objetos de cada clase
medico = Medico("Ana Pérez", "Cardiología", "Hospital Central", 10)
ingeniero = Ingeniero("Carlos López", "Ingeniería Civil", "Constructora ABC", 8)
docente = Docente("María Gómez", "Matemáticas", "Colegio Nacional", 5)

# Llamado al método trabajar() para cada objeto
describir_trabajo(medico)
describir_trabajo(ingeniero)
describir_trabajo(docente)
