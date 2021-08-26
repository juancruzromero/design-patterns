# 📚 Principios SOLID

## 👨🏽‍🏫 Introducción a principios SOLID

Robert C. Martín co-autor del manifiesto ágil desarrolló estos **Principios SOLID**. Son las bases principales para diseñar software utilizando el paradigma orientado a objetos. Busca evitar malos diseños, tener que refactorizar el código fuente y que el mismo sea bien legible y extensible.

Se llaman **Principios SOLID** por su acrónimo en inglés:
- S -> Responsabilidad única (Single Responsability)
- O -> Abierto/Cerrado (Open/Closed)
- L -> Sustitución de Liskov (Liskov Substitution)
- I -> Segregación de Interfaces (Interface Segregation)
- D -> Inversión de dependencia (Dependency Inversion)

## 👩🏽‍🏭 Responsabilidad Simple

Primero debo entender a qué llamamos cohesión en **POO**. En principio, no es fácil de explicarlo con palabras, pero estoy seguro que con un ejemplo se entenderá perfecto. Teorícamente, es una medida de cuánto una unidad tiene relación consigo misma. La cohesión mide la fuerza de relación entre funcionalidades dentro de un programa.

Si vamos a un ejemplo, una clase que realiza una tarea en concreto, tiene una **cohesión alta**. Una clase que realiza diversas funcionalidades, tiene una **cohesión baja y esto no es muy deseable**.

Haciendo una analogía con una navaja suiza, una buena práctica es hacer una clase por cada una de sus funcionalidades, una para cortar, otra para destapar vinos, etc. Una mala práctica es hacer una clase con todas estas necesidades, y entonces **no cumpliriamos con el principio de Responsabilidad Simple**.

Entonces, como conclusión, **una clase debe tener una sola razón para existir**. Una clase debe realiza una sola tarea.

Por ejemplo, creamos una clase con las caracteristicas de un **rectangulo**:

**En Python**
```python
class Rectangulo():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def mostrar(self):
        print(self.to_string()) 

```
**En C#**
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
