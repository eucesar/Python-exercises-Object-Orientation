#Crie uma classe "Carro" que possua os atributos "marca", "modelo", "ano" e "velocidade". Crie métodos para acelerar e frear o carro, e também para imprimir os dados do carro (marca, modelo, ano e velocidade). Em seguida, crie um objeto dessa classe e teste os métodos criados.

class Carro:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        
    def acelerar(self, valor):
        self.velocidade += valor
        
    def frear(self, valor):
        if self.velocidade - valor < 0:
            self.velocidade = 0 #se for menor que 0 eu vou zerar a velocidade vai ser 0, n tem como ter velociadade negativa
        else:
            self.velocidade -= valor
            
    #atualizar dados
    def imprimir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Velocidade: {self.velocidade}")
        
meu_carro = Carro("Fiat", "Uno", 2010)

meu_carro.acelerar(20)
meu_carro.imprimir_dados()

meu_carro.frear(10)
meu_carro.imprimir_dados()
