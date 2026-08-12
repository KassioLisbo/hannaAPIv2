import requests

def Pesquisar(tag):

    Player = PesquisarPlayer(tag)
    Batalhas = PesquisarBatalhas(tag)

    return {
        "player": Player,
        "batalhas": Batalhas
    }

def PesquisarPlayer(tag):
    url =  f"https://api.clashroyale.com/v1/players/%23{tag}"
    headers = {'Authorization': 'Bearer'}

    r = requests.get(url, headers=headers)

    dados = r.json()

    player = {
        "nome": dados["name"],
        "trofeus": dados["trophies"],
        "tag": dados["tag"]
    }

    return player

def PesquisarBatalhas(tag):

    url = f"https://api.clashroyale.com/v1/players/%23{tag}/battlelog"
    headers = {'Authorization': 'Bearer'}

    r = requests.get(url, headers=headers)

    dados = r.json()

    batalhas = []

    for batalha in dados:

        minhas_coroas = batalha["team"][0]["crowns"]
        coroas_adversario = batalha["opponent"][0]["crowns"]

        if minhas_coroas > coroas_adversario:
            resultado = "Vitoria"

        elif minhas_coroas < coroas_adversario:
            resultado = "Derrota"

        else:
            resultado = "Empate"

        batalhas.append({
            "tipo": batalha["type"],
            "resultado": resultado
        })

    return batalhas