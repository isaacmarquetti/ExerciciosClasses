"""
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado=1):
        self.lado = lado

    def mudar_valor(self, lado):
        self.lado = lado

    def retorna_valor(self):
        return self.lado

    def calcula_area(self):
        return self.lado ** 2


# Testando

quadrado = Quadrado(4)
print(quadrado.lado)
print(quadrado.calcula_area())
