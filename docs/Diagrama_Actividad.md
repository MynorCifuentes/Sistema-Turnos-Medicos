### Diagrama de Actividad del método `atender()` (Mermaid)

```mermaid
flowchart TD
    A[Inicio] --> B[Obtener paciente actual]
    B --> C{Hay paciente en la cola}
    C -- Si --> D[Remover paciente]
    D --> E[Mostrar mensaje atendido]
    E --> G[Actualizar ventana]
    C -- No --> F[Mostrar mensaje sin pacientes]
    F --> G
    G --> H[Fin]
```
