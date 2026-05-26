# Estrategia de Branching

## Convención propuesta

Se adopta un flujo basado en ramas de tipo `feature/` para cambios aislados por capacidad o componente.

## Por qué `feature/infrastructure`

- Agrupa el trabajo de infraestructura sin mezclarlo con cambios funcionales de la API
- Facilita revisión, pruebas y rollback
- Mantiene el historial enfocado en un objetivo concreto del proyecto

## Modelo de trabajo

- `main` se reserva para versiones estables y listas para entrega.
- `feature/*` se usa para implementar partes aisladas del sistema.
- Las integraciones se hacen por pull request, con validación automática en CI.

## Criterio operativo

Este enfoque reduce el acoplamiento entre cambios de negocio y cambios de infraestructura, y permite auditar con claridad qué se incorporó en cada release.