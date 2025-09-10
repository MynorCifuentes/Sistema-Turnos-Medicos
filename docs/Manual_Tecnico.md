## Manual Técnico

### Estructura de Carpetas

```
Sistema-Turnos-Medicos/
│
├── app.py
├── Estructuras/
│     ├── __init__.py
│     ├── Cola.py
│     └── Paciente.py
├── Ventanas/
│     ├── __init__.py
│     ├── Registro.py
│     ├── Visualizar.py
│     └── Atender.py
```

### Dependencias

- **Tkinter** (incluido en la mayoría de instalaciones de Python)
- **Pillow** (`pip install pillow`)
- **graphviz** (`pip install graphviz`)
- **Graphviz** ejecutable en el sistema

### Ejecución

Asegúrate de ejecutar `python app.py` desde la raíz del proyecto.

### Descripción General de la Arquitectura

- **`Paciente`**: Clase nodo para la lista enlazada.
- **`ColaPacientes`**: Implementa la lista enlazada personalizada con métodos `push`, `pop`, `listar` y `graficar`.
- **Ventanas (`RegistroPaciente`, `VisualizarPacientes`, `AtenderPaciente`)**:  
  Heredan de `tk.Frame`, son la interfaz gráfica para cada función principal.
- **`App`**: Controla la navegación entre pantallas y mantiene la única instancia de `ColaPacientes`.



---

## Notas

- Si tienes problemas al graficar la cola, asegúrate de que el ejecutable `dot` de Graphviz está en tu PATH.
- Cualquier error de importación suele resolverse asegurando que ejecutas el script desde la raíz del proyecto y tienes los archivos `__init__.py` en cada carpeta.

---
