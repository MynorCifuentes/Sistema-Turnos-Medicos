import tkinter as tk
from Estructuras.Cola import ColaPacientes
from Ventanas.Registro import RegistroPaciente
from Ventanas.Visualizar import VisualizarPacientes
from Ventanas.Atender import AtenderPaciente

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Practica2")
        self.geometry("800x500")
        self.cola = ColaPacientes()
        self.mostrar_menu()

    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_menu(self):
        self.limpiar()
        frame = tk.Frame(self, bg="#2C3E50")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Turnos Medicos", bg="#4682B4", fg="white", font="Arial 18 bold").pack(pady=40)
        tk.Button(frame, text="Registrar", font="Arial 12", command=self.mostrar_registro).pack(side="left", padx=40, expand=True)
        tk.Button(frame, text="Visualizar", font="Arial 12", command=self.mostrar_visualizar).pack(side="left", padx=40, expand=True)
        tk.Button(frame, text="Atender", font="Arial 12", command=self.mostrar_atender).pack(side="left", padx=40, expand=True)

    def mostrar_registro(self):
        self.limpiar()
        frame = RegistroPaciente(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)

    def mostrar_visualizar(self):
        self.limpiar()
        frame = VisualizarPacientes(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)
        frame.actualizar_lista()

    def mostrar_atender(self):
        self.limpiar()
        frame = AtenderPaciente(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()