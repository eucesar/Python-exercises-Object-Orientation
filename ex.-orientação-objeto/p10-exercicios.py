#Crie uma classe "Livro" que possua os atributos "titulo", "autor" e "ano". Crie um método para imprimir os dados do livro em forma de string (ex: "O livro 'Dom Casmurro', de Machado de Assis, foi publicado em 1899"). Em seguida, crie um objeto dessa classe e teste o método criado.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def dados_do_livro(self): #aqui q vai ter a saida => dados sobre o livro
        return print(f"O livro '{self.titulo}', de {self.autor}, foi publicado em {self.ano}")

# Cria um objeto da classe Livro e testa o método dados_do_livro()
meu_livro = Livro("1984", "George Orwell", 1949)
meu_livro.dados_do_livro()
