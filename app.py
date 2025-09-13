import tkinter as tk
from Estructuras.Cola import ColaPacientes
from Ventanas.Registro import RegistroPaciente
from Ventanas.Visualizar import VisualizarPacientes
from Ventanas.Atender import AtenderPaciente

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mynor Cifuentes_Practica2")
        self.geometry("800x200")
        self.cola = ColaPacientes()
        self.mostrar_menu()

    def limpiar(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_menu(self):
        self.limpiar()
        frame = tk.Frame(self, bg="#2C3E50")
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="Turnos Médicos", bg="#4682B4", fg="white", font=("Kokila", 22, "bold")).pack(pady=20)
        tk.Button(frame, text="Registrar", font="Kokila 20", command=self.mostrar_registro).pack(side="left", padx=40, expand=True)
        tk.Button(frame, text="Visualizar", font="Kokila 20", command=self.mostrar_visualizar).pack(side="left", padx=40, expand=True)
        tk.Button(frame, text="Atender", font="Kokila 20", command=self.mostrar_atender).pack(side="left", padx=40, expand=True)

    def mostrar_registro(self):
        self.limpiar()
        self.geometry("700x350")
        frame = RegistroPaciente(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)

    def mostrar_visualizar(self):
        self.limpiar()
        self.geometry("600x600")
        frame = VisualizarPacientes(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)
        frame.actualizar_lista()

    def mostrar_atender(self):
        self.limpiar()
        self.geometry("600x300")
        frame = AtenderPaciente(self, self.cola, self.mostrar_menu)
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()