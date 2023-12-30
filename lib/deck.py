import random


class Deck:
  def __init__(self):
    self.cartas = []

  def GerarDeck(self, tipos, ranks):
    for tipo in tipos:
      for rank in ranks:
        self.cartas.append([tipo, rank])

  def Embaralhar(self):
    random.shuffle(self.cartas)

  def Cavar(self):
    return self.cartas.pop()

  def Devolver(self, carta):
    self.cartas.append(carta)