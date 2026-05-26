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

from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = None
        self.vida = None
        self.golpes = None
    
    def atacar(self, alvo, forca):
        pass
    
    def receber_dano(self, dano):
        pass
    
    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def curar(self):
        pass


class Mago(Personagem):
    def curar(self):
        pass