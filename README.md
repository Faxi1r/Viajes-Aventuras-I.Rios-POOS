# Viajes Aventura

Sistema de gestión de destinos, paquetes turísticos y reservas (TI3021 · Unidad 4 · Sprint 1).

## Estructura por capas

```
src/viajes_aventura/
├── presentation/   # Interfaz de usuario (menús / GUI)
├── business/       # Reglas de negocio: modelos, autenticación, validaciones
└── persistence/    # Conexión a la BD y esquema SQL
docs/               # Requerimientos, modelo físico v1, UML y diagramas
tests/              # Pruebas repetibles
```

Las clases salen del diagrama UML (`docs/uml_classes_v1.drawio`):
`User`, `Destination`, `TourPackage`, `PackageDestination`, `Reservation`,
`AuthService` y `DataValidator`.

## Preparar el entorno

Requiere Python 3.10 o superior. No necesita dependencias externas (SQLite viene incluido).

```bash
git clone <url-del-repositorio>
cd viajes-aventura
cp .env.example .env        # en Windows: copy .env.example .env
```

## Ejecutar la prueba de conexión a SQLite

```bash
python -m unittest tests.test_connection -v
```

Resultado esperado: 3 pruebas en estado `OK`.

Para crear la base de datos local:

```bash
PYTHONPATH=src python -m viajes_aventura.presentation.main
```

## Flujo de trabajo (Git)

- Ramas: `feature/`, `fix/` o `docs/` + clave Jira + descripción, p. ej. `docs/va-12-requirements`.
- Todo cambio a `main` pasa por un pull request aprobado por el compañero. **Prohibido el push directo.**
- Enlazar el PR en la tarjeta de Jira.

## Convenciones

- Código Python y SQL en inglés; mensajes al usuario en español.
- El archivo `.env` real queda local; solo se versiona `.env.example`.

## Pendiente (Hito 2)

MySQL, lógica de reservas, autenticación con hash de contraseñas, BPMN y UML de casos de uso.
