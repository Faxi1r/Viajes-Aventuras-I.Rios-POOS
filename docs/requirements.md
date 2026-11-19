# Requerimientos v0 (borrador)

Completar y priorizar en equipo. Cada requerimiento necesita identificador, prioridad y criterio de aceptación comprobable.

| ID | Tipo | Requerimiento | Prioridad | Criterio de aceptación |
|----|------|---------------|-----------|------------------------|
| RF-01 | Funcional | La agencia puede registrar un destino. | Alta | El destino registrado aparece en el listado de destinos disponibles. |
| RF-02 | Funcional | El cliente puede reservar un paquete. | Alta | La reserva aparece en su historial con estado y precio total. |
| RF-03 | Funcional | Un paquete contiene al menos 2 destinos con costo asociado. | Alta | Guardar un paquete con 1 destino es rechazado; con 2 o más, se guarda. |
| RNF-01 | No funcional | Las contraseñas se almacenan como hashes. | Alta | El registro de prueba contiene un hash y la clave original no aparece almacenada. |

## Regla del negocio representada en la BD

Un paquete turístico contiene 2 o más destinos (clase asociativa `PackageDestination`
→ tabla `package_destinations` con claves foráneas a `tour_packages` y `destinations`).
