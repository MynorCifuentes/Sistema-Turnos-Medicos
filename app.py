from tkinter import Tk, Frame, Label, Button, Entry, StringVar
from tkinter.ttk import Combobox

def mostrar_registro():
    frame_botones.pack_forget()
    frame_registro.pack(expand=True)

def regresar_menu():
    frame_registro.pack_forget()
    frame_botones.pack(expand=True)

ventana = Tk()
ventana.title("Practica2")

ancho_ventana = 600
alto_ventana = 400

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Panel superior
panel_superior = Frame(ventana, bg="#4682B4", height=80)
panel_superior.pack(fill="x")
lbl_sup = Label(panel_superior, text="Turnos Médicos", bg="#4682B4", fg="white", font="Arial 18 bold")
lbl_sup.pack(pady=20, anchor="center")

# Panel inferior
panel_inferior = Frame(ventana, bg="#2C3E50")
panel_inferior.pack(fill="both", expand=True)

# Frame de botones menú principal
frame_botones = Frame(panel_inferior, bg="#2C3E50")
frame_botones.pack(expand=True)

btn_registrar = Button(frame_botones, text="Registrar Paciente", font="Arial 12", command=mostrar_registro)
btn_registrar.pack(side="left", padx=10)

btn_visualizar = Button(frame_botones, text="Visualizar Pacientes", font="Arial 12")
btn_visualizar.pack(side="left", padx=10)

btn_atender = Button(frame_botones, text="Atender Paciente", font="Arial 12")
btn_atender.pack(side="left", padx=10)

# Frame de registro de paciente (oculto por defecto)
frame_registro = Frame(panel_inferior, bg="#2C3E50")

lbl_registro = Label(frame_registro, text= "Registro de Pacientes", bg = "#2C3E50", fg="white", font= "Arial 16")
lbl_registro.grid(column=0, row=0, sticky="e", padx=(40,10), pady=(30,10))

# Etiqueta y campo Nombre
lbl_nombre = Label(frame_registro, text="Nombre:", bg="#2C3E50", fg="white", font="Arial 14")
lbl_nombre.grid(column=0, row=1, sticky="e", padx=(40,10), pady=(30,10))
entry_nombre = Entry(frame_registro, font="Arial 14", width=25)
entry_nombre.grid(column=1, row=1, padx=(0,40), pady=(30,10), sticky="w")

# Etiqueta y campo Edad
lbl_edad = Label(frame_registro, text="Edad:", bg="#2C3E50", fg="white", font="Arial 14")
lbl_edad.grid(column=0, row=2, sticky="e", padx=(40,10), pady=10)
entry_edad = Entry(frame_registro, font="Arial 14", width=8)
entry_edad.grid(column=1, row=2, padx=(0,40), pady=10, sticky="w")

# Combobox de especialidad médica
lbl_especialidad = Label(frame_registro, text="", bg="#2C3E50")
lbl_especialidad.grid(column=0, row=3)  # Espacio
especialidades = ["General", "Pediatría", "Cardiología", "Ginecología", "Traumatología"]
var_especialidad = StringVar()
combo_especialidad = Combobox(frame_registro, textvariable=var_especialidad, values=especialidades, font="Arial 14", width=22, state="readonly")
combo_especialidad.set("Especialidad Médica")
combo_especialidad.grid(column=0, row=3, columnspan=2, pady=10, padx=40, sticky="ew")

# Botón Agendar (izquierda) y Regresar (derecha)
btn_agendar = Button(frame_registro, text="Agendar", font="Arial 12")
btn_agendar.grid(column=0, row=4, sticky="w", padx=(40,10), pady=(50,10))

btn_regresar = Button(frame_registro, text="Regresar", font="Arial 12", command=regresar_menu)
btn_regresar.grid(column=1, row=4, sticky="e", padx=(10,40), pady=(50,10))

# Configura el grid para expandir el espacio entre los controles
frame_registro.columnconfigure(0, weight=1)
frame_registro.columnconfigure(1, weight=1)

ventana.mainloop()