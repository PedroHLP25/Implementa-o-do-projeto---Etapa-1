from abc import ABC, abstractmethod
from jogador import Jogador

class DistribuicaoExercitosStrategy(ABC):
    @abstractmethod
    def distribuir_exercitos(self, jogador: Jogador, quantidade: int):
        pass


class DistribuicaoPadrao(DistribuicaoExercitosStrategy):
    def distribuir_exercitos(self, jogador: Jogador, quantidade: int):
        jogador.exercitos += quantidade


class DistribuicaoBonus(DistribuicaoExercitosStrategy):
    def distribuir_exercitos(self, jogador: Jogador, quantidade: int):
        jogador.exercitos += quantidade + 2  
