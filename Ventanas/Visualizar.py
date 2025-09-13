import tkinter as tk
from PIL import Image, ImageTk

class VisualizarPacientes(tk.Frame):
    def __init__(self, master, cola, regresar_callback):
        super().__init__(master, bg="#2C3E50")
        self.cola = cola
        self.regresar_callback = regresar_callback
        self.imagen_graphviz = None
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Turnos Medicos", bg="#4682B4", fg="white", font="Arial 18 bold").grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")
        tk.Label(self, text="Cola pacientes", bg="#2C3E50", fg="white", font="Arial 14").grid(row=1, column=0, pady=10)
        tk.Label(self, text="Tiempo de espera", bg="#2C3E50", fg="white", font="Arial 14").grid(row=1, column=1, pady=10)

        self.lista_pacientes = tk.Listbox(self, font="Arial 12", width=25)
        self.lista_pacientes.grid(row=2, column=0, padx=(40,10), pady=10, sticky="n")
        self.lista_tiempos = tk.Listbox(self, font="Arial 12", width=30)
        self.lista_tiempos.grid(row=2, column=1, padx=(10,40), pady=10, sticky="n")

        self.lbl_imagen = tk.Label(self, bg="#2C3E50")
        self.lbl_imagen.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(self, text="Mostrar Cola con Graphviz", font="Arial 12", command=self.mostrar_graphviz).grid(row=4, column=0, pady=10)
        tk.Button(self, text="Regresar", font="Arial 12", command=self.regresar_callback).grid(row=4, column=1, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.actualizar_lista()

    def mostrar_graphviz(self):
        path_img = self.cola.graficar('cola_pacientes')
        img = Image.open(path_img)
        img = img.resize((400, 150))  # Ajusta el tamaño si es necesario
        self.imagen_graphviz = ImageTk.PhotoImage(img)
        self.lbl_imagen.config(image=self.imagen_graphviz)

    def actualizar_lista(self):
        self.lista_pacientes.delete(0, tk.END)
        self.lista_tiempos.delete(0, tk.END)
        actual = self.cola.primero
        while actual:
            self.lista_pacientes.insert(tk.END, f"{actual.nombre}")
            self.lista_tiempos.insert(
                tk.END,
                f"Espera: {actual.tiempo_espera} min | Atención: {actual.tiempo_atencion} min"
            )
            actual = actual.siguiente