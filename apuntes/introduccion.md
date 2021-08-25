# 💬 Introduccion
Luego de haber entendido el paradigma de la **Programación Orientada a Objetos (POO)**, y cómo implementarlo en el código, el próximo paso es aprender **Patrones de Diseño**. Estos patrones busca resolver los problemas más comunes que tuvieron los programadores a lo largo de la historia de la manera más optima posible, respetando las bases del paradigma.

Entender estos patrones nos permitirá aplicar las mejores prácticas para tener aplicaciones robustas, legibles y mantenibles. 
## 🤔 ¿Qué son los Patrones de Diseño?
Como dijimos en la introducción, son soluciones a diferentes problemas que tenemos los programadores, con patrones ya definidos por los cuatro autores del libro **"Design Patterns: Elements of Reusable Object-Oriented"**, denominados por la comunidad como **"The Gang of Four"**. Estos patrones son independientes del lenguaje, librería y sistema operativo. Es por esto que se irán explicando con ejemplos en **Python** y **C#**.

Si bien, estos patrones fueron diseñados en los años 90', a pesar de este mundo cambiante, aún son vigentes y es muy importantes entenderlos.

## 📜 Listado de Patrones de Diseño

Los patrones han sido clasificados en tres grupos.
- Patrones creacionales.
- Patrones estructurales.
- Patrones de comportamiento.

## 🧠 Patrones Creacionales
- **Abstract Factory** Provee una interfaz para la creación de familias de objetos sin especificar una clase en concreta.
- **Factory Method** Define una interfaz para la creación de un objeto, pero deja que la subclase decida qué clase instanciar.
- **Builder** Separa la construcción de objetos complejos.
- **Prototype** Especifica que tipo de objetos crear usando una instancia prototipo y crea nuevos objetos copiando este prototipo.
- **Singleton** Nos asegura que una clase solo puede ser instanciada una vez, además de proveer un punto de acceso a esta.

## 🔧 Patrones Estructurales
- **Adapter** Convierte la interfaz de una clase en otro interfaz que el cliente espera.
- **Bridge** Nos permite desacoplar una abstracción de su implementación, de manera que ambas puedan ser modificadas independientemente sin necesidad de alterar por ello la otra.
- **Composite** Sirve para construir objetos complejos a partir de otros más simples y similares entre sí, gracias a la composición recursiva y a una estructura en forma de árbol.
- **Decorator** Agrega responsabilidades adicionales a un objeto de forma dinámica.
- **Facade** Nos permite utilizar módulos complejos de una forma sencilla y con bajos costos para el cliente.
- **Flyweight** Nos permite eliminar o reducir redundancia cuando trabajamos con una gran cantidad de objetos.
- **Proxy** Permite controlar el acceso a diferentes áreas de módulos.

## 🦾 Patrones de Comportamiento
- **Chain of Responsibility** Evita acoplar el emisor de una petición a su receptor dando a más de un objeto la posibilidad de responder a una petición. Para ello, se encadenan los receptores y pasa la petición a través de la cadena hasta que es procesada por algún objeto.
- **Command** Permite solicitar una operación a un objeto sin conocer realmente el contenido de esta operación, ni el receptor real de la misma. Para ello se encapsula la petición como un objeto, con lo que además facilita la parametrización de los métodos.
- **Interpreter** Dado un idioma, define una representación para su gramática junto con un intérprete que use la representación para interpretar oraciones en el lenguaje.
- **Iterator** Define una interfaz que declara los métodos necesarios para acceder secuencialmente a un grupo de objetos de una colección.
- **Mediator** Define un objeto que encapsula como un conjunto de objetos interactúan.
- **Memento** Permite almacenar el estado de un objeto (o del sistema completo) en un momento dado de manera que se pueda restaurar en ese punto de manera sencilla. Para ello se mantiene almacenado el estado del objeto para un instante de tiempo en una clase independiente de aquella a la que pertenece el objeto (pero sin romper la encapsulación), de forma que ese recuerdo permita que el objeto sea modificado y pueda volver a su estado anterior.
- **Observer** Define una dependencia del tipo uno a muchos entre objetos, de manera que cuando uno de los objetos cambia su estado, notifica este cambio a todos los dependientes.
- **State** Se utiliza cuando el comportamiento de un objeto cambia dependiendo del estado del mismo.
- **Template** Method Define el esqueleto de programa de un algoritmo en un método, llamado método de plantilla, el cual difiere algunos pasos a las subclases.
- **Visitor** Representa una operación que se realiza sobre los elementos que conforman la estructura de un objeto.