class ExceptionQtdJogadores(Exception):
  def __init__(self, mensagem = "O máximo são 4 jogadores"):
    self.mensagem = mensagem
    super().__init__(self.mensagem)