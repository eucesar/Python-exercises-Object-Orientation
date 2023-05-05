#Crie uma classe "Retangulo" que possua os atributos "largura" e "altura". Crie um método que calcule a área desse retângulo e outro método que calcule o perímetro. Em seguida, crie um objeto dessa classe e chame os métodos criados.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    #tenho q usar o 'self' para a função, pq eu quero q ela leia uma função __init__, e se eu for chamar ela futuramente, eu so digito o 1° nome e uso (), n preciso escrever valor na variavel, pq ela vai ser usada em baixo, eu uso o self na propria função
    def calcular_area(self): 
        return self.largura * self.altura #para fzer conta uso o return
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo1 = Retangulo(10, 5) #tem q declarar a variavel por ultimo - __unit__

print("Área:", retangulo1.calcular_area()) #variavel + função - qq coisa q eu for manipular os valores q eu coloquei na class eu uso essa variavel, já q coloquei defini valor apra a class ali
print("Perímetro:", retangulo1.calcular_perimetro())
#print(f"exemplo: {retangulo1.calcular_area()}")

        