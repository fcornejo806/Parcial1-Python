def suma(n1, n2, n3):
    result = n1 + n2 + n3
    print(result)


suma(2, 4, 6)

def sumaImpares():
    result = 0
    for numero in range(1, 1001, 2):
        print(numero)
        result = result + numero
    print(result)


sumaImpares()

def definicionEsfera(radio):
    from math import pi
    perimetro = 2 * pi * radio
    area = 4 * radio ** 2 * pi
    volumen = (4 / 3) * pi * radio ** 3
    result = "Radio",radio,"Perimetro",perimetro,", Area",area," Volumen ",volumen
    print(result)


definicionEsfera(12)

class Esfera:
    from math import pi

    def definicionEsfera(self, radio):
        self.radio = radio
        result = print(f"perimetro: {obtenerPerimetro()} area: {obtenerArea()} volumen: {obtenerVolumen()}")
        return result

    def obtenerPerimetro(self):
        result = float(2 * pi * 12)
        return result


    def obtenerArea(self):
        result = float(4 * pi * 12**2)
        return result


    def obtenerVolumen(self):
        result = float((4/3) * pi * 12**3)
        return result





    




