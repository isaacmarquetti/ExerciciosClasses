class Bola:
    def __init__(self):
        self.cor = 'Azul'
        self.circuferencia = 4
        self.material = 'Metal'

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor

# Exemplo

bola = Bola()
bola.troca_cor('Amarelo')
print(bola.mostra_cor())