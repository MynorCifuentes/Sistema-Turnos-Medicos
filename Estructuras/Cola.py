import os
from Estructuras.Paciente import Paciente
class ColaPacientes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    # Agrega al final (como push)
    def push(self, nombre, edad, especialidad):
        nuevo = Paciente(nombre, edad, especialidad)
        if self.ultimo:
            self.ultimo.siguiente = nuevo
        else:
            self.primero = nuevo
        self.ultimo = nuevo
        self.tamanio += 1

    # Quita del frente (como pop)
    def pop(self):
        if self.primero:
            paciente = self.primero
            self.primero = self.primero.siguiente
            if not self.primero:
                self.ultimo = None
            self.tamanio -= 1
            return paciente
        return None

    def listar(self):
        actual = self.primero
        pacientes = []
        while actual:
            pacientes.append(actual)
            actual = actual.siguiente
        return pacientes

    def esta_vacia(self):
        return self.primero is None

    def contar(self):
        return self.tamanio

    def graficar(self, filename='cola_pacientes'):
        dot_filename = f"{filename}.dot"
        img_filename = f"{filename}.png"
        with open(dot_filename, 'w', encoding='utf-8') as f:
            f.write('digraph ColaPacientes {\n')
            f.write('rankdir=LR;\n')
            actual = self.primero
            count = 0
            while actual:
                node_name = f'Paciente{count}'
                label = f"{actual.nombre}\\nEdad: {actual.edad}\\n{actual.especialidad}"
                f.write(f'{node_name} [label="{label}"];\n')
                if actual.siguiente:
                    f.write(f'{node_name} -> Paciente{count+1};\n')
                actual = actual.siguiente
                count += 1
            f.write('}\n')
        os.system(f'dot -Tpng {dot_filename} -o {img_filename}')
        return img_filename