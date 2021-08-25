# SOLID

## Introducción a principios SOLID ##

Robert C. Martín co-autor del manifiesto ágil escribió el libro: Agile Software Development: Principles, Patterns, and Practices. Ahí menciona los **principios SOLID**. Al aplicar estos principios en conjunto podemos crear aplicaciones modulables reutilizables y mantenibles, las cuales podremos ampliar con el paso del tiempo.

- S -> Responsabilidad única (Single Responsability)
- O -> Abierto/Cerrado (Open/Closed)
- L -> Sustitución de Liskov (Liskov Substitution)
- I -> Segregación de Interfaces (Interface Segregation)
- D -> Inversión de dependencia (Dependency Inversion)

## Responsabilidad Simple ##

Primero debo entender cohesión. Es una medida de cuánto una unidad tiene relación consigo misma. Una clase que realiza una tarea en concreto, tiene una cohesión alta.

Entonces, una clase debe tener una sola razón para cambiar. Una clase realiza una sola tarea.

Por ejemplo, vemos este ejemplo de código:

```python
class Rectangulo():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def mostrar(self):
        print(self.to_string()) 

```
```csharp
class Prueba():
    def __init__():

```
Sin embargo, el método Mostrar() debe ser propio de una hipotética capa de **presentación**. El Rectángulo, debe encargarse de qué datos mostrar y nó como mostrarlos.

Para mejorar esto y aplicar este principio, podemos crear una clase llamada **Presentación**.

```python
class Presentacion():
    def mostrar(self, objeto):
        print(objeto) 

```


## Abierto/Cerrado ##

Este principio dice que la entidad, ya sea módulo, clase o función, debe estar **abierta a la extensión**, pero **cerrada a la modificación**. Por ejemplo, si queremos extender la aplicación, podemos lograrlo sin modificar el código existente, por ejemplo si queremos agregar el módulo de autenticación a nuestro sistema, no deberíamos por qué modificar o reconstruir el módulo de alta de usuarios. Esto lo podemos resolver mediante la herencia.
