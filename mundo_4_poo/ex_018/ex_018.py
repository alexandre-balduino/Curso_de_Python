'''
Desafio 018

Crie uma classe Churrasco,
onde seja possível informar quantas 
pesssoas vão participar e mostre
quanto de carne deve ser comprado,
o custo total do churrasco e o 
preço por pessoa.

Considere:
consumo padrão: 400g por pessoa
preço. R$82,40/Kg
'''

from rich import print
from rich.panel import Panel

class Churrasco:
    consumo: float = 0.400
    preco_kg: float = 82.40
        
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
    
    
    def __str__(self):
        return f"Esse é {self.titulo} com {self.pessoas} pessoas participando."
    
    
    def calcular_quant_carne(self) -> float:
        return self.pessoas * Churrasco.consumo # ou __class__.consumo
    
    
    def calcular_preco_total(self) -> float:
        return self.calcular_quant_carne() * __class__.preco_kg # ou Churrasco.preco
    
    
    def calcular_preco_individual(self) -> float:
        return self.calcular_preco_total() / self.pessoas
        
    
    def analisar(self):
        conteudo = f"Analisando [blue]{self.titulo}[/] com [green]{self.pessoas} convidados[/] \n"
        conteudo += f"Cada participante comerá {Churrasco.consumo}kg e cada Kg custa R${Churrasco.preco_kg:.2f} \n"
        conteudo += f"Recomendo comprar {self.calcular_quant_carne()}kg de carne \n"
        conteudo += f"O custo total será de R${self.calcular_preco_total():.2f} \n"
        conteudo += f"E cada pessoa pagará R${self.calcular_preco_individual():.2f} para participar."
        analise = Panel(
            conteudo, 
            title=self.titulo
        )
        print(analise)

churramigo = Churrasco("Churrasco dos amigos", 11)
churramigo.analisar()
