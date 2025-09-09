
class Paciente: 
    def __init__(self, nombre, edad, especialidad, tiempo):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.tiempo = tiempo
        
        self.siguiente = None