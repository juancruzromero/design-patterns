# Programación orientada a objetos #

## ¿Qué es la programación orientada a objetos (POO)? ##
...

## Clases y Objetos ##

### Conceptos ###
- Estado
- Propiedades
- Comportamientos

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