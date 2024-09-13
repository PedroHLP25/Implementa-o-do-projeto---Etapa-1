from fastapi import FastAPI, HTTPException, Query
from jogo import Jogo
from jogador import Jogador
import json
app = FastAPI()

jogo = Jogo()
jogador1 = Jogador("Edson", "Vermelho")
jogador2 = Jogador("Marcelo", "Azul")
jogador3 = Jogador("Pedro", "Verde")

jogo.adicionar_jogador(jogador1)
jogo.adicionar_jogador(jogador2)
jogo.adicionar_jogador(jogador3)

jogo.definir_ordem_jogadores()
jogo.distribuir_territorios()
jogo.distribuir_objetivos()
jogo.iniciar_rodada()


jogo.distribuir_cartas()


with open('dados.json', 'w') as f:
    f.write(jogo.gerar_json())

# # Função para salvar o estado atual do jogo em um arquivo JSON
# @app.get("/salvar_jogo/")
# def salvar_jogo():
#     with open('dados.json', 'w') as f:
#         f.write(jogo.gerar_json())
#     return {"message": "Dados do jogo salvos com sucesso"}

# # Função para carregar o estado do jogo do arquivo JSON
# @app.get("/carregar_jogo/")
# def carregar_jogo():
#     with open('dados.json', 'r') as f:
#         dados = f.read()
#     return {"message": "Dados do jogo carregados com sucesso", "dados": dados}


# # Escolher cor para o jogador
# @app.post("/jogador/escolher_cor/")
# def escolher_cor(nome: str = Query(...), cor: str = Query(...)):
#     jogador = next((j for j in jogo.jogadores if j.nome == nome), None)
#     if not jogador:
#         raise HTTPException(status_code=404, detail="Jogador não encontrado")
    
#     jogador.cor = cor
#     return {"message": f"O jogador {nome} escolheu a cor {cor}"}

# # Receber objetivo
# @app.post("/jogador/receber_objetivo/")
# def receber_objetivo(nome: str):
#     jogador = next((j for j in jogo.jogadores if j.nome == nome), None)
#     if not jogador:
#         raise HTTPException(status_code=404, detail="Jogador não encontrado")
    
#     if not jogo.objetivos:
#         raise HTTPException(status_code=400, detail="Não há mais objetivos disponíveis")
    
#     objetivo = jogo.objetivos.pop(0)  # Retira um objetivo da lista
#     jogador.receber_objetivo(objetivo)
    
#     return {"message": f"O jogador {nome} recebeu o objetivo: {objetivo}"}