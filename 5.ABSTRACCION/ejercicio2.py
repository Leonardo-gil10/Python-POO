from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass
    
class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return"El Ingeniero está desarrollando un sistema."
    
class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "El Doctor está realizando una operacion."

ingeniero = Ingeniero()
print(ingeniero.realizar_tarea())

doctor = Doctor()
print(doctor.realizar_tarea())

    