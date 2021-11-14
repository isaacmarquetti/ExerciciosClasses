"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.
    Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, idade):
        if idade < 21:
            self.altura = self.altura + ((idade - self.idade) + 0.5)
            self.idade += idade

    def engordar(self, peso):
        self.peso += peso

    def emagrece(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Testando


pessoa = Pessoa('Luis', 2, 48, 80)
print(pessoa.__dict__)
pessoa.envelhecer(10)
print(pessoa.__dict__)