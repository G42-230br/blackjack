from lib.deck import Deck
from lib.jogador import Jogador
from lib.mao import Mao

tipos = [
  "ouros",
  "copas",
  "espadas",
  "paus"
]

ranks = [
  {"rank":"A", "valor":"11"},
  {"rank":"2", "valor":"2"},
  {"rank":"3", "valor":"3"},
  {"rank":"4", "valor":"4"},
  {"rank":"5", "valor":"5"},
  {"rank":"6", "valor":"6"},
  {"rank":"7", "valor":"7"},
  {"rank":"8", "valor":"8"},
  {"rank":"9", "valor":"9"},
  {"rank":"10", "valor":"10"},
  {"rank":"Q", "valor":"10"},
  {"rank":"J", "valor":"10"},
  {"rank":"K", "valor":"10"},
]

def ExibirMao(jogador, mao, vezes):
  print(f"======= Mao {jogador.nome} ======= ")
  for i in range(vezes):
    print(f'''
    Tipo: {mao.mao_cartas[i][0]}
    Rank: {mao.mao_cartas[i][1]['rank']}
    Valor: {mao.mao_cartas[i][1]['valor']}
      ''')
  
deck = Deck()
deck.GerarDeck(tipos, ranks)
deck.Embaralhar()
  
mao_jogador = Mao()
mao_jogador.GerarMao(deck)
mao_dealer = Mao()
mao_dealer.GerarMao(deck)
  
jogador = Jogador(1, "Amanda", mao_jogador, 0)
dealer = Jogador(2, "Dealer", mao_dealer, 1)

fim_jogo = 0

if jogador.mao.soma == 21:
  print(f"Blackjack! Que sorte, o jogador {jogador.id} ganhou na primeira rodada")

contador_j = len(mao_jogador.mao_cartas)
contador_d = len(mao_dealer.mao_cartas)

ExibirMao(jogador, mao_jogador, 2)
print(f"Soma {mao_jogador.soma}")

ExibirMao(dealer, mao_dealer, 1)

print(f'''
Jogador {jogador.nome}, você deseja cavar ou passar?
(1)Cavar
(2)Passar
''')
decisao = input()

if decisao == "1":
  carta = deck.Cavar()
  mao_jogador.AddCartas(carta)  
  ExibirMao(jogador, mao_jogador, 3)
  print(f"Soma: {jogador.mao.soma}")
elif decisao == "2":
  ExibirMao(jogador, mao_jogador, 2)
  print(f"Soma: {jogador.mao.soma}")

ExibirMao(dealer, mao_dealer, 2)
print(f"Soma: {dealer.mao.soma}")

vezes = 2

if dealer.mao.soma < 17:
  print("Dealer precisa cavar...")
  while dealer.mao.soma < 17:
    carta = deck.Cavar()
    mao_dealer.AddCartas(carta)
    vezes += 1
    
ExibirMao(dealer, mao_dealer, vezes)
print(f"Soma: {dealer.mao.soma}")

dealer_ganhou = mao_dealer.soma == 21
jogador_ganhou = mao_jogador.soma == 21
jogador_perdeu = mao_jogador.soma > 21
dealer_perdeu = mao_dealer.soma > 21

if jogador_perdeu and dealer_perdeu:
    print("Ambos perderam")
elif jogador_perdeu:
    print("Jogador perdeu")
elif dealer_perdeu:
    print("Dealer perdeu")
elif jogador_ganhou and dealer_ganhou:
    print("Empate")
elif jogador_ganhou:
    print("Jogador ganhou")
elif dealer_ganhou:
    print("Dealer ganhou")
elif mao_jogador.soma < 21:
    if mao_jogador.soma > mao_dealer.soma:
        print("Jogador ganhou")
    elif mao_jogador.soma < mao_dealer.soma:
        print("Dealer ganhou")


