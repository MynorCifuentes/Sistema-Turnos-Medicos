import tkinter as tk
from tkinter import messagebox

class RegistroPaciente(tk.Frame):
    def __init__(self, master, cola, regresar_callback):
        super().__init__(master, bg="#2C3E50")
        self.cola = cola
        self.regresar_callback = regresar_callback
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Turnos Medicos", bg="#4682B4", fg="white", font="Arial 18 bold").grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")
        tk.Label(self, text="Nombre:", bg="#2C3E50", fg="white", font="Arial 14").grid(row=1, column=0, sticky="e", padx=(40,10), pady=(10,10))
        self.entry_nombre = tk.Entry(self, font="Arial 14", width=25)
        self.entry_nombre.grid(row=1, column=1, padx=(0,40), pady=(10,10), sticky="w")

        tk.Label(self, text="Edad:", bg="#2C3E50", fg="white", font="Arial 14").grid(row=2, column=0, sticky="e", padx=(40,10), pady=10)
        self.entry_edad = tk.Entry(self, font="Arial 14", width=8)
        self.entry_edad.grid(row=2, column=1, padx=(0,40), pady=10, sticky="w")

        especialidades = ["Medicina General", "Pediatría", "Ginecología", "Dermatología"]
        self.especialidad_var = tk.StringVar()
        self.especialidad_var.set("Especialidad Medica")
        self.combo_especialidad = tk.OptionMenu(self, self.especialidad_var, *especialidades, command=self.actualizar_tiempo_espera)
        self.combo_especialidad.config(font="Arial 14")
        self.combo_especialidad.grid(row=3, column=0, columnspan=2, pady=10, padx=40, sticky="ew")

        tk.Label(self, text="Tiempo de espera estimado:", bg="#2C3E50", fg="white", font="Arial 14").grid(row=4, column=0, sticky="e", padx=(40,10), pady=(10,10))
        self.lbl_tiempo_espera = tk.Label(self, text="0 minutos", bg="#2C3E50", fg="white", font="Arial 14")
        self.lbl_tiempo_espera.grid(row=4, column=1, padx=(0,40), pady=(10,10), sticky="w")

        tk.Button(self, text="Agendar", font="Arial 12", command=self.agendar).grid(row=5, column=0, sticky="w", padx=(40,10), pady=(30,10))
        tk.Button(self, text="Regresar", font="Arial 12", command=self.regresar_callback).grid(row=5, column=1, sticky="e", padx=(10,40), pady=(30,10))

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.actualizar_tiempo_espera()

    def actualizar_tiempo_espera(self, *args):
        especialidad = self.especialidad_var.get()
        if especialidad != "Especialidad Medica":
            # El tiempo de espera es la suma de todos los tiempos de atención en la cola
            tiempo_espera = 0
            actual = self.cola.primero
            while actual:
                tiempo_espera += actual.tiempo_atencion
                actual = actual.siguiente
            tiempo_atencion = self.cola.tiempo_base_especialidad(especialidad)
            self.lbl_tiempo_espera.config(
                text=f"Espera: {tiempo_espera} minutos | Atención: {tiempo_atencion} minutos"
            )
        else:
            self.lbl_tiempo_espera.config(text="0 minutos")

    def agendar(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.entry_edad.get().strip()
        especialidad = self.especialidad_var.get()
        if nombre and edad.isdigit() and especialidad != "Especialidad Medica":
            self.cola.push(nombre, int(edad), especialidad)
            self.entry_nombre.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)
            self.especialidad_var.set("Especialidad Medica")
            self.lbl_tiempo_espera.config(text="0 minutos")
            messagebox.showinfo("Éxito", "Paciente agendado en la cola")
            self.actualizar_tiempo_espera()
        else:
            messagebox.showerror("Error", "Complete todos los campos correctamente.")