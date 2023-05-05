#Crie uma classe "Funcionario" que possua os atributos "nome", "salario" e "cargo". Crie métodos para calcular o aumento de salário e para imprimir os dados do funcionário (nome, cargo e salário atual). Em seguida, crie um objeto dessa classe e teste os métodos criados.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        
    def calcular_aumento_salario(self, percentual_aumento):
        aumento = self.salario * percentual_aumento / 100
        self.salario += aumento
        
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário atual: R$ {self.salario:.2f}")


meu_funcionario = Funcionario("João", 3000, "Analista de Sistemas")

meu_funcionario.imprimir_dados()

meu_funcionario.calcular_aumento_salario(10)

meu_funcionario.imprimir_dados()
