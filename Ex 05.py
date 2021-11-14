"""
Classe Conta Corrente: Crie uma classe para implementar uma
conta corrente. A classe deve possuir os seguintes atributos:
número da conta, nome do correntista e saldo. Os métodos
são os seguintes: alterarNome, depósito e saque; No construtor,
saldo é opcional, com valor default zero e os demais atributos
são obrigatórios.
"""


class ContaCorrente:
    def __init__(self, numero_da_conta, nome_correntista, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def set_nome(self, nome):
        self.nome_correntista = nome

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito no valor de R${valor:.2f}')

    def saque(self, valor):
        if self.saldo == 0:
            print('Não há valores para o saque.')
            return

        if self.saldo >= valor:
            print(f'Saque de R${valor:.2f}')
            valor_atual = self.saldo - valor
            print(f'Valor atual: R${valor_atual:.2f}')
            self.saldo = valor_atual
            return
        if self.saldo < valor:
            print(f'Saque indisponível nesse valor.')
            return


conta = ContaCorrente(1242, 'Fulano de Tal')

while True:
    print()
    print("## BANCO ##")
    print(f'Títular: {conta.nome_correntista}')
    print(f'Número da conta: {conta.numero_da_conta}')
    print(f'Saldo atual: R${conta.saldo:.2f}')
    print()
    print("O que deseja fazer? [1]Depositar [2]Saque [3]Sair")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite as opções 1, 2 ou 3.")

    if opcao == 1:
        valor_deposito = float(input("Digite o valor para depósito: "))
        conta.deposito(valor_deposito)

    if opcao == 2:
        valor_saque = float(input("Digite o valor para saque: "))
        conta.saque(valor_saque)

    if opcao == 3:
        break

    if opcao > 3:
        print("Digite as opções 1, 2 ou 3.")


