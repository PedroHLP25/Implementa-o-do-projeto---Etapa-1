from abc import ABC, abstractmethod
from typing import List
from jogador import Jogador

class DistribuicaoTerritoriosStrategy(ABC):
    @abstractmethod
    def distribuir_territorios(self, jogadores: List[Jogador], territorios: List[str]):
        pass


class DistribuicaoEquilibrada(DistribuicaoTerritoriosStrategy):
    def distribuir_territorios(self, jogadores: List[Jogador], territorios: List[str]):
        territorios.sort()  # Apenas um exemplo de ordenação antes de distribuir
        for i, jogador in enumerate(jogadores):
            jogador.receber_territorios(territorios[i::len(jogadores)])


class DistribuicaoAleatoria(DistribuicaoTerritoriosStrategy):
    def distribuir_territorios(self, jogadores: List[Jogador], territorios: List[str]):
        import random
        random.shuffle(territorios)
        for i, jogador in enumerate(jogadores):
            jogador.receber_territorios(territorios[i::len(jogadores)])
