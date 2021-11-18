"""
Classe Bomba de Combustível: Faça um programa completo utilizando
classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses
    atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel

    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser
        abastecido e mostra a quantidade de litros que foi colocada
        no veículo

        abastecerPorLitro( ) – método onde é informado a quantidade
        em litros de combustível e mostra o valor a ser pago pelo
        cliente.

        alterarValor( ) – altera o valor do litro do combustível.

        alterarCombustivel( ) – altera o tipo do combustível.

        alterarQuantidadeCombustivel( ) – altera a quantidade de
        combustível restante na bomba.

    OBS: Sempre que acontecer um abastecimento é necessário atualizar
    a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        quantidade_carro = valor / self.valor_litro

        if quantidade_carro > self.quantidade_combustivel:
            print(f"A bomba não suporta a quantidade informada. (Max: {self.quantidade_combustivel} litros)")
            return

        self.quantidade_combustivel -= valor / self.valor_litro
        print(f'Colocou R${valor:.2f} de {self.tipo_combustivel} e adicionou {quantidade_carro}l. '
              f'(Bomba: {self.quantidade_combustivel} litros)')

    def abastecer_por_litro(self, litro):
        valor = litro * self.valor_litro

        if litro > self.quantidade_combustivel:
            print(f"A bomba não suporta a quantidade informada. (Max: {self.quantidade_combustivel} litros)")
            return

        self.quantidade_combustivel -= litro
        print(f'Adicionou {litro}l de {self.tipo_combustivel} no valor total de R${valor:.2f}. '
              f'(Bomba: {self.quantidade_combustivel} litros)')

    def alterar_valor(self, valor):
        self.valor_litro = valor

    def alterar_combustivel(self, combustivel):
        self.tipo_combustivel = combustivel

    def alterar_quantidade_combustivel(self, combustivel):
        self.quantidade_combustivel += combustivel
        print(f'Adicionado {combustivel}l na bomba de combustível. (Bomba: {self.quantidade_combustivel} litros)')

# Testando


bomba = BombaCombustivel('gasolina', 5, 100)
bomba.abastecer_por_valor(90)
bomba.abastecer_por_litro(30)
bomba.alterar_quantidade_combustivel(40)


