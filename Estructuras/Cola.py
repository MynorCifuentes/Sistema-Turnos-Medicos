import os
from Estructuras.Paciente import Paciente

class ColaPacientes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
        
    def _actualizar_tiempos(self):
        actual = self.primero
        tiempo_acumulado = 0
        while actual:
            actual.tiempo_espera = tiempo_acumulado
            actual.tiempo_atencion = self.tiempo_base_especialidad(actual.especialidad)
            tiempo_acumulado += actual.tiempo_atencion
            actual = actual.siguiente


    def tiempo_base_especialidad(self, especialidad):
        if especialidad == "Medicina General":
            return 10
        elif especialidad == "Pediatría":
            return 15
        elif especialidad == "Ginecología":
            return 20
        elif especialidad == "Dermatología":
            return 25
        return 10  # valor por defecto

    def obtener_tiempo_espera_actual(self, especialidad):
        actual = self.primero
        tiempo_total = 0
        while actual:
            if actual.especialidad == especialidad:
                tiempo_total += self.tiempo_base_especialidad(especialidad)
            actual = actual.siguiente
        return tiempo_total

    def push(self, nombre, edad, especialidad):
        #tiempo_espera = self.obtener_tiempo_espera_actual(especialidad)
        nuevo = Paciente(nombre, edad, especialidad)
        if self.ultimo:
            self.ultimo.siguiente = nuevo
        else:
            self.primero = nuevo
        self.ultimo = nuevo
        self.tamanio += 1
        self._actualizar_tiempos()

    def pop(self):
        if self.primero:
            paciente = self.primero
            self.primero = self.primero.siguiente
            if not self.primero:
                self.ultimo = None
            self.tamanio -= 1
            self._actualizar_tiempos()
            return paciente
        
        return None

    def esta_vacia(self):
        return self.primero is None

    def contar(self):
        return self.tamanio

    # Método graficar que recibe de parametro un archivo con nombre cola_pacientes
    def graficar(self, nombre_archivo='cola_pacientes'):
        archivo_dot = f"{nombre_archivo}.dot"
        archivo_img= f"{nombre_archivo}.png"
        with open(archivo_dot, 'w', encoding='utf-8') as archivo:
            archivo.write('digraph ColaPacientes {\n') 
            archivo.write('rankdir=LR;\n')
            actual = self.primero
            contador = 0 
            while actual:
                nombre_nodo = f'Paciente{contador}'
                lbl_paciente = (
                    f"{actual.nombre}\\n"
                    f"Edad: {actual.edad}\\n"
                    f"{actual.especialidad}\\n"
                    f"Espera: {actual.tiempo_espera} min\\n"
                    f"Atención: {actual.tiempo_atencion} min"
                )
                archivo.write(f'{nombre_nodo} [label="{lbl_paciente}"];\n')
                if actual.siguiente:
                    archivo.write(f'{nombre_nodo} -> Paciente{contador+1};\n')
                actual = actual.siguiente
                contador += 1
            archivo.write('}\n')
        os.system(f'dot -Tpng {archivo_dot} -o {archivo_img}')
        return archivo_img