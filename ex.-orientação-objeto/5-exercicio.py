#Crie uma classe "Ponto" que possua os atributos "x" e "y". Crie um método que calcule a distância entre dois pontos. Em seguida, crie dois objetos dessa classe e calcule a distância entre eles.

import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calcular_distancia(self, outro_ponto):
        return math.sqrt((outro_ponto.x - self.x) ** 2 + (outro_ponto.y - self.y) ** 2)

ponto1 = Ponto(1, 2)
ponto2 = Ponto(4, 6)

distancia_entre_pontos = ponto1.calcular_distancia(ponto2)

print(f"A distância entre os pontos ({ponto1.x}, {ponto1.y}) e ({ponto2.x}, {ponto2.y}) é {distancia_entre_pontos}")
