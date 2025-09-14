class Raca:
    def __init__(self):
        self.tipo = None
        self.movimento = None
        self.infravisao = None
        self.alinhamento = None
        self.peso = None
        self.idades = None
    
    def escolhaRaca(self, raca):
        if raca == "Elfo":
            self.tipo = "Elfo"
        elif raca == "Anão":
            self.tipo = "Anão"
        elif raca == "Humano":
            self.tipo = "Humano"
        else:
            self.tipo = "Desconhecida"

    def atributosRaca(self, idade):
        if self.tipo == "Elfo":
            self.movimento = "9 metros"
            self.infravisao = "18 metros"
            self.alinhamento = "Neutro"
            self.peso = 60
            if idade < 120: self.idades = "Jovem"
            elif idade < 450: self.idades = "Adulto"
            elif idade < 900: self.idades = "Meia-Idade"
            else: self.idades = "Idoso"

        elif self.tipo == "Anão":
            self.movimento = "6 metros"
            self.infravisao = "18 metros"
            self.alinhamento = "Ordem"
            self.peso = 75
            if idade < 50: self.idades = "Jovem"
            elif idade < 120: self.idades = "Adulto"
            elif idade < 350: self.idades = "Meia-Idade"
            else: self.idades = "Idoso"

        elif self.tipo == "Humano":
            self.movimento = "9 metros"
            self.infravisao = "Não"
            self.alinhamento = "Qualquer"
            self.peso = 80
            if idade < 15: self.idades = "Jovem"
            elif idade < 45: self.idades = "Adulto"
            elif idade < 90: self.idades = "Meia-Idade"
            else: self.idades = "Idoso"