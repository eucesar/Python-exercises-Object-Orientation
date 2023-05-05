#Crie uma classe "Cachorro" que possua os atributos "nome" e "idade". Crie um método que calcule a idade do cachorro em anos humanos (considere que 1 ano para o cachorro equivale a 7 anos humanos). Em seguida, crie um objeto dessa classe e teste o método criado.

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def calcular_idade_humana(self):
        idade_humana = self.idade * 7
        return idade_humana

meu_cachorro = Cachorro("Rex", 3)

idade_humana = meu_cachorro.calcular_idade_humana()

print(f"{meu_cachorro.nome} tem {idade_humana} anos humanos")
