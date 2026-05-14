'''
Desafio 025

Crie classes capazes de calcular 
fretes de veículos diferentes.

    |---------------------------|
    |   Transporte              |
    |===========================|
    | + distancia               |
    | + frete                   |
    |---------------------------|
    | + calc_frete() {abstract} |
    |---------------------------|
                    ∆
                    |
         |----------|-----------|
         |          |           |
|----------------|  |  |----------------|
|   Moto         |  |  |   Caminhao     |
|================|  |  |================|
| + fator = 0.50 |  |  | + fator = 1.20 |
|----------------|  |  |----------------|
| + calc_frete() |  |  | + calc_frete() |
|----------------|  |  |----------------|
                    |
            |----------------|
            |   Drone        |
            |================|
            | + fator = 0.50 |
            |----------------|
            | + calc_frete() |
            |----------------|
'''

from abc import ABC, abstractmethod

class Trabsporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete
    
    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Trabsporte):
    def __init__(self, fator=0.50):
        self.fator = fator
    
    def calc_frete(self):
        pass


class Caminhao(Transporte):
    def __init__(self, fator=1.20):
        self.fator = fator
    
    def calc_frete(self, dist):
        pass


class Drone(Transporte):
    def __init__(self, fator):
        self.fator = fator
    
    def calc_frete(self, dist):
        pass