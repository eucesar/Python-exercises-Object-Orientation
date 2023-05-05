#Crie uma classe "ContaBancaria" que possua os atributos "titular", "saldo" e "numero". Crie métodos para depositar e sacar dinheiro da conta, e também para consultar o saldo. Em seguida, crie um objeto dessa classe e teste os métodos criados.

class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero

    def depositar(self, valor): #função python em 00 sempre vai usar self como variavel 
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    
    def sacar(self, valor):
        if (self.saldo >= valor): #n pode ser um valor maior 
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
            
        else: #apenas self.saldo < valor
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Criando uma conta bancária e testando os métodos
conta = ContaBancaria("João", 1000.00, "123456")

conta.consultar_saldo() # Saldo atual: R$1000.00 #variavel + função

conta.depositar(500.00) # Depósito de R$500.00 realizado com sucesso! #eu vou usar a variavel 'conta' para td, para poder usar os valores colocados da 'ContaBancaria' e manipular de acordo com a função que eu criei
conta.consultar_saldo() # Saldo atual: R$1500.00

conta.sacar(200.00) # Saque de R$200.00 realizado com sucesso!
conta.consultar_saldo() # Saldo atual: R$1300.00

conta.sacar(1500.00) # Saldo insuficiente.
conta.consultar_saldo() # Saldo atual: R$1300.00


