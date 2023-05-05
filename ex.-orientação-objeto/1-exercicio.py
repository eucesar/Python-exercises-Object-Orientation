#Crie uma classe "Pessoa" que possua os atributos "nome" e "idade". Em seguida, crie um objeto dessa classe e imprima seus atributos. 

class Pessoa:
    def __init__(self, nome, idade): #função + public
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 30)

print(f"Nome: {pessoa1.nome}") #uso 'f' no começo para acessar o 00 = e uso {} para aceesar no print
print(f"Idade: {pessoa1.idade}")