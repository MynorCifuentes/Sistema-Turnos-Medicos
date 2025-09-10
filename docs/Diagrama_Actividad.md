### Diagrama de Actividad del método `atender()` (Mermaid)

```mermaid
---
title: Actividad del método atender()
---
start
    :Obtener paciente actual de la cola;
    decision ¿Hay paciente en la cola?
        yes
            :Remover paciente con pop();
            :Mostrar mensaje "Se atendió a: [nombre]";
        no
            :Mostrar mensaje "No hay pacientes en la cola";
    :Actualizar información de la ventana;
end
```
