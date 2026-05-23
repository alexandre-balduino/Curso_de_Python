'''
Desafio 027

Simule o sistema de batalha entre 
personagens de um RPG

    |-------------------------|
    |   Personagem {abstract} |
    |=========================|
    | + nome                  |
    | + vida                  |
    | + golpes                |
    |-------------------------|
    | + atacar(alvo, forca)   |
    | + receber_dano(dano)    |
    | + curar() {abstract}    |
    |-------------------------|
                ∆
                |
        |--------------|
        |              |
|-------------|   |-----------|
|   Guerreiro |   |   Mago    |
|=============|   |===========|
| + curar()   |   | + curar() |
|-------------|   |-----------|
'''

from abs import ABS, abstractmethod

class Personagem(ABS):
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.golpes = []
    
    def atacar(self):
        pass
    
    def receber_dano(self):
        pass
    
    @abstractmethod
    def curar(self):
        pass,