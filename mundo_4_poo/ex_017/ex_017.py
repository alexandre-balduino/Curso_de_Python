'''
Desafio 017

Crie a classe Produto, 
onde podemos cadastrar nome e o preço.
Crie também um método que mostre uma
etiqueta de preço do produto.
'''

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
    
    
    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"
    
    
    def etiqueta(self) -> Panel:
        larg = 28
        conteudo = f"{self.nome.center(larg, '-')}\n"
        conteudo += f"{'-' * larg}\n"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(larg, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=32)
        return etiqueta


terco = Produto("Terço", 25)
mouse = Produto("Mouse", 100)
iphone = Produto("Iphone 17 Pro Max", 25_000.85)
print(terco.etiqueta())
print(mouse.etiqueta())
print(iphone.etiqueta())
