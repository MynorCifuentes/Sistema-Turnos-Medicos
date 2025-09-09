from Estructuras.Paciente import Paciente
import os

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def cola_vacia(self):
        return self.primero == None and self.ultimo == None
    
    def push(self, nombre, edad, especialidad, tiempo):
        
        nuevo_paciente = Paciente(nombre, edad, especialidad, tiempo)
        
        if self.cola_vacia():
            self.primero = self.ultimo = nuevo_paciente
        else: 
            self.ultimo.siguiente = nuevo_paciente
            self.ultimo = nuevo_paciente
    
    def pop(self):
        if self.cola_vacia():
            return None  # O podrías lanzar una excepción

        paciente_atendido = self.primero
        self.primero = self.primero.siguiente

        # Si después de quitar el primero la cola queda vacía, actualiza self.ultimo
        if self.primero is None:
            self.ultimo = None

        paciente_atendido.siguiente = None  # Opcional: desconectar el nodo
        return paciente_atendido
    
    
    def graficar(self, name):
        temp = self.primero
        contador = 0
        dot_path = f"{name}.dot"
        png_path = f"{name}.png"
        cadena = "digraph G {\n"
        cadena += "rankdir=LR;\n"
        cadena += 'node[ shape = record, style="filled", color="black", fillcolor="yellow"];\n'
    
        while temp is not None:
            cadena += f'Paciente{contador}[label="{temp.nombre} | {temp.edad} | {temp.especialidad} | {temp.tiempo}"];\n'
            if contador > 0:
                cadena += f"Paciente{contador-1} -> Paciente{contador};\n"
            temp = temp.siguiente
            contador += 1

        cadena += "}\n"

        with open(dot_path, "w") as file:
            file.write(cadena)

        os.system(f"dot -Tpng {dot_path} -o {png_path}")
        return png_path  # Útil si luego quieres usarlo en la GUI