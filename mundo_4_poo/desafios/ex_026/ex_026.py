'''
Desafio 026

Crie a estrutura capaz de calcular 
salários de funciinários diferentes

    |--------------------------|
    |   Funcionario {abstract} |
    |==========================|
    | + nome                   |
    | + sal_bruto              |
    | + salario                |
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

class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, sal_liquido, sal_minimo, inss):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_liquido = sal_liquido
        self.sal_minimo = sal_minimo
        self.inss = inss
    
    @abstractmethod
    def calcular_sal(self):
        pass
    
    def analisar_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self, valor_hora, horas_trab):
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def analisar_sal(self):
        pass


class Mensalista(Funcionario):
    def analisar_sal(self):
        pass