'''
Desafio 026

Crie a estrutura capaz de calcular 
salários de funciinários diferentes

    |--------------------------|
    |   Funcionario {abstract} |
    |==========================|
    | + nome                   |
    | + sal_bruto              |
    | + sal_liquido            |
    | + sal_minimo = 1612      |
    | + inss                   |
    |--------------------------|
    | + calc_sal() {abstract}  |
    | + analisar_sal()         |
    |--------------------------|
                   ∆
                   |
         |--------------------|
         |                    |
|----------------|    |---------------|
|   Horista      |    |   Mensalista  |
|================|    |===============|
| + valor_hora() |    | + calc_sal()  |
| + horas_trab() |    |---------------|
|----------------|
| + calc_sal()   |
|----------------|
'''

from abc import ABC, abstractmethod
from rich.panel import Panel

class Funcionario(ABC):
    sal_minimo = 1612
    desc_inss = 7.5
    
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.sal_liquido = 0
    
    @abstractmethod
    def calcular_sal(self):
        pass
    
    def analisar_sal(self):
        quant = self.sal_liquido / Funcionario.sal_minimo
        print(f"O salário de {self.nome} é R${self.sal_liquido:.2f} e corresponde a {quant:.1f} salários mínimos.")


class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.13, horas_trab=200):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab
    
    def calcular_sal(self):
        self.sal_liquido = self.sal_bruto - (self.sal_bruto * Funcionario.desc_inss / 100)


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
    
    def calcular_sal(self):
        self.sal_liquido = self.sal_bruto - (self.sal_bruto * Funcionario.desc_inss / 100)