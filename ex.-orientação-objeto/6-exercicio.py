#Crie uma classe "Animal" que possua os atributos "nome" e "especie". Crie métodos para alimentar o animal e para emitir um som característico da espécie. Em seguida, crie um objeto dessa classe e teste os métodos criados.

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def alimentar(self):
        print(f"{self.nome} está se alimentando!")
        
    def emitir_som(self):
        if self.especie == "cachorro":
            print("Au au!")
        elif self.especie == "gato":
            print("Miau!")
        else:
            print("Esse animal não emite som.")

meu_animal = Animal("Rex", "cachorro")

meu_animal.alimentar()
meu_animal.emitir_som()
