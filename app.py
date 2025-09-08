from tkinter import Tk, Frame, Label, Button

ventana = Tk()
ventana.title("Practica2")

# Tamaño de la ventana
ancho_ventana = 800
alto_ventana = 400

# Obtener el tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular coordenadas x e y para centrar la ventana
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Asignar geometría centrada
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Panel superior (Frame)
panel_superior = Frame(ventana, bg="#4682B4", height=80)
panel_superior.pack(fill="x")

lbl_sup = Label(panel_superior, text="Turnos Médicos", bg="#4682B4", fg="white", font="Arial 14 bold")
lbl_sup.pack(pady=20, anchor="center")

# Panel inferior (Frame)
panel_inferior = Frame(ventana, bg="#2C3E50")
panel_inferior.pack(fill="both", expand=True)

# Frame para los botones, centrado vertical y horizontalmente
frame_botones = Frame(panel_inferior, bg="#2C3E50")
frame_botones.pack(expand=True)

btn_registrar = Button(frame_botones, text="Registrar Paciente")
btn_registrar.pack(side="left", padx=10)

btn_visualizar = Button(frame_botones, text="Visualizar Pacientes")
btn_visualizar.pack(side="left", padx=10)

btn_atender = Button(frame_botones, text="Atender Paciente")
btn_atender.pack(side="left", padx=10)

ventana.mainloop()