class Mao:

  def __init__(self):
    self.mao_cartas = []
    self.soma = 0

  def GerarMao(self, deck):
    for _ in range(2):
      carta = deck.Cavar()
      self.mao_cartas.append(carta)
      self.soma = self.soma + int(carta[1]['valor'])

  def AddCartas(self, carta):
    self.mao_cartas.append(carta)
    self.soma += int(carta[1]['valor'])

  def MostrarMao(self):
    print(self.mao_cartas)