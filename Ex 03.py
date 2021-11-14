"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e
    Altura, a escolher)

    Métodos: Mudar valor dos lados, Retornar valor dos lados,
    calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao
    usuário que informe as medidades de um local. Depois,
    deve criar um objeto com as medidas e calcular a quantidade
    de pisos e de rodapés necessárias para o local.
"""


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def set_comprimento(self, comprimento):
        self.comprimento = comprimento

    def set_largura(self, largura):
        self.largura = largura

    def get_comprimento(self):
        return self.comprimento

    def get_largura(self):
        return self.largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def perimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)


m1 = float(input("Digite o comprimento (m): "))
m2 = float(input("Digite a largura (m): "))

medida = Retangulo(m1, m2)
print(f'Área total: {medida.calcular_area()}m')
print(f'Perímetro: {medida.perimetro()}m')
