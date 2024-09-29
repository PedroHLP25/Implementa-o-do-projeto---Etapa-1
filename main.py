from fastapi import FastAPI
from jogo import Jogo
from distribuicao_territorios_strategy import DistribuicaoAleatoria
from distribuicao_exercitos_strategy import DistribuicaoPadrao
from jogador import Jogador

app = FastAPI()

# Instanciando as estratégias
distribuicao_territorios_strategy = DistribuicaoAleatoria()
distribuicao_exercitos_strategy = DistribuicaoPadrao()

# Criando o jogo com as estratégias definidas
jogo = Jogo(distribuicao_territorios_strategy, distribuicao_exercitos_strategy)

@app.post("/jogadores/adicionar/")
def adicionar_jogador(nome: str, cor: str):
    jogador = Jogador(nome, cor)
    jogo.adicionar_jogador(jogador)
    return {"message": f"Jogador {nome} adicionado"}

@app.post("/preparacao/distribuir-territorios/")
def distribuir_territorios():
    jogo.distribuir_territorios()
    return {"message": "Territórios distribuídos"}

@app.post("/preparacao/distribuir-exercitos/")
def distribuir_exercitos(nome: str, quantidade: int):
    jogador = next(j for j in jogo.jogadores if j.nome == nome)
    jogo.distribuir_exercitos(jogador, quantidade)
    return {"message": f"Exércitos distribuídos para o jogador {nome}"}
