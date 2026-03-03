'''
Desafio 020

Crie a classe Gamer, 
onde podemos cadastrar nome, nick e 
os jogos favoritos de uma pessoa. 
Crie também um método que permita 
mostrar a ficha desse gamer.
'''

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    
    
    def cadastrar_jogos(self, *jogo):
        for j in jogo:
            self.jogos.append(j)
    
    
    def ficha(self):
        conteudo = f"Nome real: [white on blue]{self.nome}[/]\n"
        if len(self.jogos) > 0:
            conteudo += "Jogos favoritos:\n"
            for jogo in self.jogos:
                conteudo += f":video_game:  [blue]{jogo}[/]\n"
        ficha = Panel(conteudo, title=f"Jogador: <{self.nick}>")
        return ficha


ale = Gamer("Alexandre", "Campeão")
ale.cadastrar_jogos("Minecraft", "Clash Royale")
print(ale.ficha())
joao = Gamer("João", "Gigante")
print(joao.ficha())