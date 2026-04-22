'''
Desafio 023

Implemente o seguinte diagrama de classe:
    |--------------------------|
    |   Poligono {abstract}    |
    |==========================|
    | + qtd_lados              |
    |--------------------------|
    | + perimetro() {abstract} |
    | + area() {abstract}      |
    |--------------------------|
                  ∆
                  |
        |-------------------|
        |                   |
|---------------|    |---------------|
|   Quadrado    |    |   Circulo     |
|===============|    |===============|
| + lado        |    | + raio        |
|---------------|    |---------------|
| + perimetro() |    | + perimetro() |
| + area()      |    | + area()      |
|---------------|    |---------------|
'''

import math
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        """
            Este método deve ser implementado pelas subclasses
        """
        pass
    
    @abstractmethod
    def area(self):
        """
            Este método deve ser implementado pelas subclasses
        """
        pass


class Quadrado(Poligono):
    def __init__(self, lado, qtd_lados=4):
        super().__init__(qtd_lados)
        self.lado = lado
    
    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio, qtd_lados=0):
        super().__init__(qtd_lados)
        self.raio = raio
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def area(self):
        return math.pi * (self.raio ** 2)
