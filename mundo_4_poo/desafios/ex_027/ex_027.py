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

from random import randint, choice
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def esta_vivo(self):
        return self.vida >= 0
    
    def atacar(self, alvo, forca=100):
        if alvo.esta_vivo():
            print(f"{self.nome} atacou {alvo.nome} com {choice(self.golpes)} de força {forca}")
            alvo.receber_dano(forca)
        else:
            print(f"{alvo.nome} já morreu")
    
    def receber_dano(self, dano):
        dano_recebido = randint(dano//2, dano)
        self.vida -= dano_recebido
        print(f"{self.nome} recebeu {dano_recebido} pontos de dano")
    
    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes.extend(["golpe de machado", "voadora", "direto"])
    
    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes.extend(["bola de fogo", "feitiço de dor crônica"])
    
    def curar(self):
        pass