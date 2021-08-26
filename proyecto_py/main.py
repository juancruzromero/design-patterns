class Rectangulo():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def __str__(self):
        return f"Alto: {self.alto}\tAncho {self.ancho}"

class Presentacion():
    def mostrar(rectangulo):
        print(rectangulo)

if __name__ == '__main__':
    miRectangulo = Rectangulo(10,20)
    miPresentacion = Presentacion
    miPresentacion.mostrar(miRectangulo)