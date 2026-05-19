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

class Funcionario(ABC):
    def __init__(self, nome, sal_minimo=1612, inss=7.5):
        self.nome = nome
        self.sal_bruto = 0
        self.sal_liquido = 0
        self.sal_minimo = sal_minimo
        self.inss = inss
    
    @abstractmethod
    def calcular_sal(self):
        pass
    
    def analisar_sal(self):
        print(f"{self.nome} recebe {self.sal_liquido}")


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def calcular_sal(self):
        pass


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)
    
    def calcular_sal(self):
        desc = self.sal_bruto * (self.inss / 100)
        self.sal_liquido = self.sal_bruto - desc