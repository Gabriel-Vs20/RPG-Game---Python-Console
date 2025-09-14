from .atributos import Atributos

class Personagem:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.raca = None
        self.classe = None
        self.atributos = Atributos()