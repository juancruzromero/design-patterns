# Programación orientada a objetos #

## ¿Qué es la Programación Orientada a Objetos (POO)? ##
Uno de los primeros paradigmas fue la **"Programación Estructurada"** en donde se escribe el código de forma secuencial, como por ejemplo, con el lenguaje de programación **C**.

Con el tiempo este nuevo paradigma, la **Programación Orientada a Objetos** vino a solucionar algunos problemas que tenía el anterior, como por ejemplo las largas líneas de código o lo dificil que puede ser mantenerlo.

Es aquí cuando **POO** viene a ayudarnos a resolver problemas que tenemos los programadores. A la hora de programar, pensar nuestros problemas en **forma de objeto**. 

## Entonces... ¿Qué es un objeto? ##
### Desde una perspectiva humana... ###
- Algo tangible y/o visible.
- Algo que puede comprenderse intelectualmente.
- Algo como un pensamiento o acción.

**Ejemplo: Un automóvil. (Literal)**
<p align="center"> 
    <img src="https://static.wikia.nocookie.net/lossimpson/images/2/28/THomer2.jpg/revision/latest/scale-to-width-down/309?cb=20090330180213&path-prefix=es">
</p>

### Desde la teoría del Paradigma Orientado a Objetos: ###

- Es una instancia de una clase.
- Es cualquier cosa real o abstracta que posee una estructura  que lo define y acciones que lo controlan.
- Tiene estado, exhibe un comportamiento bien definido y tiene una identidad única.
- Las buenas prácticas indican tener una clase por archivo.

**Ejemplo de un objeto en código:**

**En Python**
```python
class Coche():
    def __init__(self):
        self.largo = 250
        self.ancho = 100
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self):        
        self.enMarcha = True
    
    def estado(self):
        if self.enMarcha:
            return "Prendido"
        else:
            return "Apagado"
```
**En C#**
```csharp
class Coche():
    public Coche(int largo, int ancho)
    {
        this.largo = largo;
        this.ancho = ancho;
        int ruedas = 4;
        bool enMarcha = False;
    }

    public void Arrancar()
    {
        enMarcha = True;
    }

    public string Estado()
    {
        enMarcha = True;
        if (enMarcha)
        {
            return "Prendido";
        }
        else:
        {
            return "Apagado";
        }
    }
```
#### Repasando: ####
Entonces, **las clases** son templetes, plantillas o modelos que representan entidades o conceptos y **los objetos** vienen a ser instancias de las clases, que poseen un estado y de un comportamiento. En otras palabras, es el “template con datos”.

## Características de un Objeto ##
Un objeto tiene las siguientes carecterísticas:

- **Propiedades:** También pueden llamarse atributos y estos también serán sustantivos. Algunos atributos o propiedades son nombre, tamaño, forma, estado, etc. Son todas las características del objeto. Ejemplo: nombre, color, etc. 
- **Comportamiento:** Es cómo actúa y reacciona un objeto, en términos de cambios de estado y paso de mensajes. Es todo aquello que el objeto  puede hacer. Ejemplo: correr, trabajar o algún tipo de acción.
- **Estado:** Es el conjunto de todas las  propiedades estáticas y los  valores dinámicos que adoptan en un momento dado. Ejemplo: Encendido, apagado.
- **Identidad:** Es la característica o conjunto de características que permiten diferenciar a un  objeto de los demás.

## Principios del modelo de objetos ##

Elementos Fundamentales:

- **Clase:** Es el modelo por el cual nuestros objetos se van a construir y nos van a permitir generar más objetos. Analizamos Objetos para crear Clases. Las Clases son los modelos sobres los cuales construiremos nuestros objetos. **"Hay que analizar Objetos para crear Clases"** y este análisis que hacemos se llama **Abstracción**.
- **Abstracción:** Es cuando separamos los datos de un objeto para generar un molde. Denota las características claves de un objeto que lo distinguen de todos los demás.
- **Modularidad:** Un sistema complejo es más fácil de resolver si se divide en un conjunto de elementos. Es importante considerar **un bajo acoplamiento y una alta cohesión en su funcionamiento**. Dividir un sistema en partes pequeñas y estas serán nuestros módulos pudiendo funcionar de manera independiente. La modularidad de nuestro código nos va a dar varias ventajas como:

    - Reutilizar código.
    - Evitar colapsos.
    - Hacer nuestro código más mantenible.
    - Legibilidad.
    - Resolución rápida de problemas.
    - Una buena práctica es separando las clases en archivos diferentes.

- **Encapsulado:** Encapsular es esconder detalles de la implementación de un objeto. Se separan los aspectos externos (accesibles por otros objetos) de los detalles internos (accesibles solo dentro de la clase). Algunos lenguajes tienen varios niveles de encapsulamiento, como Público, Privado, Paquetes, etc.
  
- **Jerarquía:** Es una clasificación u ordenación de abstracciones. Consiste en agrupar clases que se obtuvieron de abstracciones realizadas y se agrupan de acuerdo a las funciones que realizan. Estó se ve más adelante al aplicar **Herencia** y **Polimorfismo**.

Otros elementos a tener en cuenta:

- **Tipos:** Un tipo es una caracterización de propiedades estructurales o de comportamiento que comparten un grupo de entidades.

- **Concurrencia:** Es la ocurrencia de dos o más lugares de ejecución durante el mismo intervalo de tiempo. Un sistema que tiene concurrencia debe poder manejar varios hilos en tiempo de ejecución como si fuera múltiple en un solo CPU.

- **Presistencia**: Es la propiedad de un objeto por lo que su existencia trasciende el tiempo y/o espacio.

Bibliografía: POO - Grady Booch

### Clase ###
```python
class Coche():
    largo = 250
    ancho = 100
    ruedas = 4
    enMarcha = False

    def arrancar(self):        
        self.enMarcha = True
    
    def estado(self):
        if self.enMarcha:
            return "Prendido"
        else:
            return "Apagado"
```
### Constructor ###

```python
class Coche():
    def __init__(self):
        self.largo = 250
        self.ancho = 100
        self.ruedas = 4
        self.enMarcha = False

    def arrancar(self, arrancamos):        
        self.enMarcha = arrancamos

        if self.enMarcha:
            return "Prendido"
        else:
            return "Apagado"
```