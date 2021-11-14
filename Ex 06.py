"""
Classe TV: Faça um programa que simule um televisor criando-o como
um objeto. O usuário deve ser capaz de informar o número do canal
e aumentar ou diminuir o volume. Certifique-se de que o número do
canal e o nível do volume permanecem dentro de faixas válidas.
"""


class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def trocar_canal(self, canal):
        if canal < 1 or canal > 100:
            print('Canal inválido. Digite entre 1 e 100.')
            return

        if canal >= 1 or canal <= 100:
            print(f'Trocou para o canal {canal}.')
            self.canal = canal
            return

    def aumentar_volume(self, volume):
        self.volume += volume
        if self.volume > 10:
            print('Volume máximo atingido.')
            self.volume = 10
            return
        print(f'Volume nível: {self.volume}')

    def diminuir_volume(self, volume):
        self.volume -= volume
        if self.volume < 0:
            print('Volume MUDO.')
            self.volume = 0
            return
        print(f'Volume nível: {self.volume}')


# Testando
canal_tv = Tv(10, 3)
canal_tv.trocar_canal(50)
canal_tv.trocar_canal(150)
canal_tv.aumentar_volume(7)
canal_tv.aumentar_volume(1)
canal_tv.diminuir_volume(10)
canal_tv.diminuir_volume(2)
