import random

class JogarDado:
    def valorDado(self):
        return [random.randint(1, 6) for _ in range(4)]

    def jogarTresDadosESomar(self):
        return sum(random.randint(1, 6) for _ in range(3))