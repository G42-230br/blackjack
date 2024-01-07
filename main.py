from lib.deck import Deck
from lib.erros import ExceptionQtdJogadores
from lib.jogador import Jogador
from lib.mao import Mao
import time
import os

def retorna_jogador(jogadores, msg):
  retornados = []
  if msg == "maior":
    for jogador in jogadores:
      if jogador.mao.soma > 21:
        retornados.append(jogador)

  if msg == "menor":
    for jogador in jogadores:
      if jogador.mao.soma < 21:
        retornados.append(jogador)

  if msg == "igual":
    for jogador in jogadores:
      if jogador.mao.soma == 21:
        retornados.append(jogador)

  return retornados

def tem_dealer(jogadores):
  return any(jogador.nome == "Dealer" for jogador in jogadores)

def retorna_dealer(jogadores):
  for index, jogador in enumerate(jogadores):
    if jogador.nome == "Dealer":
      return index


tipos = ["ouros", "copas", "espadas", "paus"]

ranks = [
    {
        "rank": "A",
        "valor": "11"
    },
    {
        "rank": "2",
        "valor": "2"
    },
    {
        "rank": "3",
        "valor": "3"
    },
    {
        "rank": "4",
        "valor": "4"
    },
    {
        "rank": "5",
        "valor": "5"
    },
    {
        "rank": "6",
        "valor": "6"
    },
    {
        "rank": "7",
        "valor": "7"
    },
    {
        "rank": "8",
        "valor": "8"
    },
    {
        "rank": "9",
        "valor": "9"
    },
    {
        "rank": "10",
        "valor": "10"
    },
    {
        "rank": "Q",
        "valor": "10"
    },
    {
        "rank": "J",
        "valor": "10"
    },
    {
        "rank": "K",
        "valor": "10"
    },
]


def ExibirMao(jogador, mao, vezes):
  print(f"======= Mao {jogador.nome} ======= ")
  for i in range(vezes):
    print(f'''
    Tipo: {mao.mao_cartas[i][0]}
    Rank: {mao.mao_cartas[i][1]['rank']}
    Valor: {mao.mao_cartas[i][1]['valor']}
      ''')


jogadores = []
ganhadores = []

jog_blackjack = []
blackjack = 0

dealer_ganhou = False
mao_padrao = Mao()
dealer = Jogador(1, "default", mao_padrao, 0)
ac_dealer = 0

print('''
Informe o modo de jogo?
(1) 1 jogador
(2) 2 jogadores
(3) 3 jogadores
(4) 4 jogadores
''')

try:
  qtd_jog = int(input())
  if qtd_jog > 4:
    raise ExceptionQtdJogadores()
except ExceptionQtdJogadores as e:
  print(e)
else:
  os.system('clear')
  print('''
Informe quantas rodadas pretendem jogar?
  ''')

  rodadas = int(input())
  os.system('clear')
  for rodada in range(rodadas):
    
    deck = Deck()
    deck.GerarDeck(tipos, ranks)
    deck.Embaralhar()

    mao_padrao = Mao()
    jogador_padrao = Jogador(1, "default", mao_padrao, 0)
    ganhadores.append(jogador_padrao)
    
    mao_dealer = Mao()
    mao_dealer.GerarMao(deck)
    dealer = Jogador(2, "Dealer", mao_dealer, 1)

    i = 0
    
    if rodada == 0:
      for i in range(qtd_jog):
        print(f"Informe o nome do jogador {i+1}:")
        nome = input()
        os.system('clear')
        mao_jogador = Mao()
        mao_jogador.GerarMao(deck)
        jogador = Jogador(i, nome, mao_jogador, 1)
        jogadores.append(jogador)
    else:
      for jogador in jogadores:
        mao_jogador = Mao()
        mao_jogador.GerarMao(deck)
        jogador.mao = mao_jogador

    i = 0
    
    for i in range(qtd_jog):
      jog_blackjack = []
      blackjack = 0
      
      print(f'''
========== Rodada {rodada + 1} ===========
              ''')

      ExibirMao(jogadores[i], jogadores[i].mao, 2)
      print(f"Soma {jogadores[i].mao.soma}")

      ExibirMao(dealer, mao_dealer, 1)

      print(f'''
Jogador {jogadores[i].nome}, você deseja cavar ou passar?
(1)Cavar
(2)Passar
        ''')
      decisao = input()
      os.system('clear')
      if decisao == "1":
        carta = deck.Cavar()
        jogadores[i].mao.AddCartas(carta)
        ExibirMao(jogadores[i], jogadores[i].mao, 3)
        print(f"Soma: {jogadores[i].mao.soma}")
      elif decisao == "2":
        ExibirMao(jogadores[i], jogadores[i].mao, 2)
        print(f"Soma: {jogadores[i].mao.soma}")

    for jogador in jogadores:
      if jogador.mao.soma == 21:
        blackjack = 1
        jog_blackjack.append(jogador)
        
    if blackjack == 0:
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
      
      jog_maior_21 = retorna_jogador(jogadores, "maior")
      jog_21 = retorna_jogador(jogadores, "igual")
      jog_menor_21 = retorna_jogador(jogadores, "menor")

      i = 0
      os.system('clear')
      if dealer_ganhou:
        if jog_21:
          print("Houve um empate entre o dealer e:")
          for jogador in jog_21:
            print(jogador.nome)
        else:
          print("A rodada é do dealer")
          ac_dealer += 1
      elif dealer.mao.soma > 21:
        if len(jog_maior_21) == qtd_jog:
          print("A rodada não é de ninguém")
        elif jog_21:
          print("A rodada é de: ")
          for jogador in jog_21:
            print(jogador.nome)
            jogador.rod_ganhas += 1
        else:
          menor = 21
          for jogador in jog_menor_21:
            dif = 21 - jogador.mao.soma
            if dif < menor:
              menor = dif
              ganhadores[0] = jogador
          print(f"A rodada é de:{ganhadores[0].nome}")
          ganhadores[0].rod_ganhas += 1
      elif dealer.mao.soma < 21:
        if len(jog_maior_21) == qtd_jog:
          print("A rodada é do dealer")
          ac_dealer += 1
        elif jog_21:
          print("A rodada é de: ")
          for jogador in jog_21:
            print(jogador.nome)
            jogador.rod_ganhas += 1
        else:
          menor = 21
          for jogador in jog_menor_21:
            dif = 21 - jogador.mao.soma
            if dif < menor:
              menor = dif
              ganhadores[0] = jogador

          if ganhadores[0].mao.soma > mao_dealer.soma:
            print(f"A rodada é de:{ganhadores[0].nome}")
            ganhadores[0].rod_ganhas += 1
          elif ganhadores[0].mao.soma == mao_dealer.soma:
            print(f"Houve um empate entre o dealer {ganhadores[0].nome}")
          else:
            print("A rodada é do Dealer")
            ac_dealer += 1
      
    else:
      os.system('clear')
      print("O(s) jogador(es)")
      for jogador in jog_blackjack:
        print(jogador.nome)
        jogador.rod_ganhas += 1
      print("venceram com um blackjack!")
      
  dealer.rod_ganhas = ac_dealer
  empatados = []
  jogadores.append(dealer)
  maior = 0

  os.system('clear')
  print("Histórico das rodadas")

  for jogador in jogadores:  
    print(f'''
Nome: {jogador.nome}
Rodadas ganhas: {jogador.rod_ganhas} 
      ''')
    
    if jogador.rod_ganhas > maior:
        maior = jogador.rod_ganhas
        ganhadores = [jogador]
    elif jogador.rod_ganhas == maior:
        empatados.append(jogador)
      
  if len(empatados) > 0:
      empatados.append(ganhadores[0])
      print("Houve um empate entre: ")
      for empate in empatados:
          print(empate.nome)
  else:
      print(f"O vencedor da mesa é {ganhadores[0].nome}")





