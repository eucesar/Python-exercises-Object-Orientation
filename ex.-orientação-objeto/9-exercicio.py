#Crie uma classe "Triangulo" que possua os atributos "lado1", "lado2" e "lado3". Crie um método que verifique se esses lados formam um triângulo e outro método que calcule a área desse triângulo. Em seguida, crie um objeto dessa classe e teste os métodos criados.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def verificar_triangulo(self):
        if self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1:
            return True #cada lado do tringulo tem q ser menor q a soma dos dois lados
        else:
            return False
    
    def calcular_area(self):
        p = (self.lado1 + self.lado2 + self.lado3) / 2
        area = (p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3)) ** 0.5
        return area

meu_triangulo = Triangulo(3, 4, 5)

if meu_triangulo.verificar_triangulo():
    area = meu_triangulo.calcular_area()
    print(f"A área do triângulo é {area}")
    print("É um triângulo")
else:
    print("Os lados não formam um triângulo")
