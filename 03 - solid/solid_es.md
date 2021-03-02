# SOLID #

## Introducción a principios SOLID ##

Robert C. Martín Coautor del manifiesto ágil escribió el libro: Agile Software Development: Principles, Patterns, and Practices. Ahí menciona los principios SOLID. Al aplicar estos principios en conjunto podemos crear aplicaciones modulables reutilizables y mantenibles, las cuales podremos ampliar con el paso del tiempo.

- S -> Responsabilidad única (Single Responsability)
- O -> Abierto/Cerrado (Open/Closed)
- L -> Sustitución de Liskov (Liskov Substitution)
- I -> Segregación de Interfaces (Interface Segregation)
- D -> Inversión de dependencia (Dependency Inversion)

## Responsabilidad Simple ##

Primero debo entender cohesión. Es una medida de cuánto una unidad tiene relación consigo misma. Una clase que realiza una tarea en concreto, tiene una cohesión alta.

Entonces, una clase debe tener una sola razón para cambiar. Una clase realiza una sola tarea.

Por ejemplo, esto funciona:

```python
class Prueba():

```
