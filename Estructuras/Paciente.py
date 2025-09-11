
class Paciente:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.tiempo_espera = 0
        self.tiempo_atencion = 0
        self.siguiente = None