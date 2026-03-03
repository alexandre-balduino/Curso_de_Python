'''
Desafio 021

Crie a classe Caneta,
que simula o funcionamento de uma 
caneta colorida, podendo escrever 
frases na cor relativa.
'''

from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True
    
    
    def destampar(self):
        if self.tampada:
            self.tampada = False
            return f"Caneta {self.cor} destampada com sucesso"
        else:
            return f"Caneta {self.cor} já está destampada"
    
    
    def tampar(self):
        if not self.tampada:
            self.tampada = True
            return f"Caneta {self.cor} tampada com sucesso"
        else:
            return f"Caneta {self.cor} já está tampada"
    
    
    def escrever(self, conteudo):
        cores = {
            "azul": "blue",
            "verde": "green",
            "vermelha": "red",
            "preta": "black on gray"
        }
        cor = cores.get(self.cor.lower(), "default")
        if self.cor.lower() == "azul":
            cor = "blue"
        elif self.cor.lower() == "vermelha":
            cor = "red"
        elif self.cor.lower() == "verde":
            cor = "green"
        if not self.tampada:
            print(f"[{cor}]{conteudo}[/]", end="")
        else:
            print(f"A caneta [{cor}]{self.cor}[/] está tampada", end="")
    
    
    def pular_linha(self, quantidade=1):
        for q in range(quantidade):
            print()


preta = Caneta("preta")
azul = Caneta("azul")
vermelha = Caneta("vermelha")
verde = Caneta("verde")

vermelha.destampar()
azul.destampar()
verde.destampar()


azul.escrever("Caneta azul, azul caneta")
preta.pular_linha()
preta.escrever("Outra cor")
preta.pular_linha()
vermelha.escrever("O batom é dessa cor")
vermelha.pular_linha()
verde.escrever("Cuide da natureza")
verde.pular_linha(2)

