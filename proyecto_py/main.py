class Rectangulo():
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def mostrar(self):
        print(self.__str__)

if __name__ == '__main__':
    miRectangulo = Rectangulo(10,20)
    miRectangulo.mostrar()