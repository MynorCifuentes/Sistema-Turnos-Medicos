# Sistema de Turnos Médicos

## Manual de Usuario

### Requisitos Previos

- **Python 3.8+**  
- **Graphviz** instalado en tu sistema ([descargar aquí](https://graphviz.gitlab.io/download/))
- **Dependencias Python:**  
  - Pillow  
  - graphviz  

Instala las dependencias necesarias con:
```bash
pip install pillow graphviz
```

### Instalación de Graphviz

- **Windows:**  
  Descarga el instalador de [Graphviz](https://graphviz.gitlab.io/download/) y agrégalo al PATH del sistema.
- **Linux:**  
  ```bash
  sudo apt-get install graphviz
  ```

### ¿Cómo ejecutar el sistema?

1. Descarga o clona el repositorio.
2. Ejecuta desde la raíz del proyecto:
   ```bash
   python app.py
   ```

### Uso del Sistema

1. **Pantalla principal:**  
   Verás botones para “Registrar”, “Visualizar” y “Atender”.
2. **Registrar paciente:**  
   - Haz clic en "Registrar".
   - Ingresa nombre, edad y especialidad.
   - Haz clic en "Agendar" para agregar el paciente a la cola.
3. **Visualizar pacientes:**  
   - Haz clic en "Visualizar".
   - Observa la lista de pacientes en espera, el tiempo estimado y pulsa "Mostrar Cola (Graphviz)" para ver el estado gráfico.
4. **Atender paciente:**  
   - Haz clic en "Atender".
   - Presiona "Atender" para retirar al primer paciente de la cola y mostrar su información.

---

