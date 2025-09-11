import tkinter as tk
from tkinter import messagebox

class AtenderPaciente(tk.Frame):
    def __init__(self, master, cola, regresar_callback):
        super().__init__(master, bg="#2C3E50")
        self.cola = cola
        self.regresar_callback = regresar_callback
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Turnos Medicos", bg="#4682B4", fg="white", font="Arial 18 bold").grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")
        self.lbl_turno = tk.Label(self, text="Turno de:", bg="#2C3E50", fg="white", font="Arial 14")
        self.lbl_turno.grid(row=1, column=0, padx=(40,10), pady=10, sticky="w")
        self.lbl_paciente = tk.Label(self, text="", bg="#2C3E50", fg="white", font="Arial 14")
        self.lbl_paciente.grid(row=1, column=1, padx=(10,40), pady=10, sticky="w")

        tk.Label(self, text="Tiempos", bg="#2C3E50", fg="white", font="Arial 14").grid(row=2, column=0, padx=(40,10), pady=10, sticky="w")
        self.lbl_tiempo = tk.Label(self, text="", bg="#2C3E50", fg="white", font="Arial 14")
        self.lbl_tiempo.grid(row=2, column=1, padx=(10,40), pady=10, sticky="w")

        tk.Button(self, text="Atender", font="Arial 12", command=self.atender).grid(row=3, column=0, sticky="w", padx=(40,10), pady=(30,10))
        tk.Button(self, text="Regresar", font="Arial 12", command=self.regresar_callback).grid(row=3, column=1, sticky="e", padx=(10,40), pady=(30,10))

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.actualizar_info()

    def actualizar_info(self):
        paciente = self.cola.primero
        if paciente:
            self.lbl_paciente.config(text=paciente.nombre)
            self.lbl_tiempo.config(text=f"Espera: {paciente.tiempo_espera} min | Atención: {paciente.tiempo_atencion} min")
        else:
            self.lbl_paciente.config(text="Ningún paciente")
            self.lbl_tiempo.config(text="0 minutos")

    def atender(self):
        paciente = self.cola.pop()
        if paciente:
            messagebox.showinfo("Atendido", f"Se atendió a: {paciente.nombre}")
        else:
            messagebox.showinfo("Info", "No hay pacientes en la cola")
        self.actualizar_info()