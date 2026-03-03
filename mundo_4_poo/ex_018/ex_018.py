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
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
        self.consumo = 0.4
        self.preco_carne = 82.4
        
    
    def analisar(self):
        quantos_kg = self.consumo * self.pessoas
        valor_total = quantos_kg * self.preco_carne
        valor_pessoa = valor_total / self.pessoas
        analise = Panel(
            f'''
Analisando {self.titulo} com {self.pessoas} convidados
Cada participante comerá {self.consumo}kg e cada Kg custa R${self.preco_carne}
Recomendo comprar {quantos_kg:.2f}kg de carne
O custo total será de R${valor_total:.2f}
E cada pessoa pagará R${valor_pessoa:.2f} para participar.
            ''', 
            title=self.titulo
        )
        print(analise)

churramigo = Churrasco("Churrasco dos amigos", 11)
churramigo.analisar()
