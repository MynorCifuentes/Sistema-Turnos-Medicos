### Diagrama de Actividad del método `atender()` (Mermaid)

```mermaid
flowchart TD
    A[Obtener paciente actual de la cola] --> B{¿Hay paciente en la cola?}
    B -- Sí --> C[Remover paciente con pop()]
    C --> D[Mostrar mensaje "Se atendió a: [nombre]"]
    D --> F[Actualizar información de la ventana]
    B -- No --> E[Mostrar mensaje "No hay pacientes en la cola"]
    E --> F
```
