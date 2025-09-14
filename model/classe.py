class Classe:
    def __init__(self):
        self.tipo = None
        self.habilidades = []

    def escolhaClasse(self, escolha):
        classes_habilidades = {
            "Guerreiro": ["Combate com armas", "Uso de armaduras pesadas", "Táticas de batalha"],
            "Mago": ["Conjuração de magias", "Estudo de arcanos", "Identificação de itens mágicos"],
            "Ladrão": ["Ações furtivas", "Arrombamento de fechaduras", "Furtar objetos"]
        }

        if escolha == "Guerreiro":
            self.tipo = "Guerreiro"
        elif escolha == "Mago":
            self.tipo = "Mago"
        elif escolha == "Ladrão":
            self.tipo = "Ladrão"
        else:
            self.tipo = "Desconhecida"
        
        self.habilidades = classes_habilidades.get(self.tipo, [])