from distribuicao_territorios_strategy import DistribuicaoTerritoriosStrategy
from distribuicao_exercitos_strategy import DistribuicaoExercitosStrategy
from jogador import Jogador
import random

class Jogo:
    def __init__(self, distribuicao_territorios_strategy: DistribuicaoTerritoriosStrategy,
                 distribuicao_exercitos_strategy: DistribuicaoExercitosStrategy):
        self.jogadores = []
        self.territorios = ["Território1", "Território2", "Território3", "Território4", "Território5", "Território6"]
        self.ordem_jogadores = []
        self.distribuicao_territorios_strategy = distribuicao_territorios_strategy
        self.distribuicao_exercitos_strategy = distribuicao_exercitos_strategy

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def definir_ordem_jogadores(self):
        self.ordem_jogadores = random.sample(self.jogadores, len(self.jogadores))

    def distribuir_territorios(self):
        self.distribuicao_territorios_strategy.distribuir_territorios(self.jogadores, self.territorios)

    def distribuir_exercitos(self, jogador: Jogador, quantidade: int):
        self.distribuicao_exercitos_strategy.distribuir_exercitos(jogador, quantidade)
