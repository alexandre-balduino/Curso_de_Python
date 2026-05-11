'''
Desafio 024

Simule uma cafeteira orientada a objetos
    |-----------------------------|
    |   BebidaQuente {abstract}   |
    |=============================|
    | + preparar()                |
    | + ferver_agua()             |
    | + misturar() {abstract}     |
    | + servir() {abstract}       |
    |-----------------------------|
                   ∆
                   |
       |-------------------------|
       |           |             |
|--------------|   |   |--------------|
| Cafe         |   |   |   Cha        |
|==============|   |   |==============|
| + misturar() |   |   | + misturar() |
| + servir()   |   |   | + servir()   |
|--------------|   |   |--------------|
                   |
            |--------------|
            |   Leite      |
            |==============|
            | + misturar() |
            | + servir()   |
            |--------------|
'''

from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("--- Iniciando o preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("Bebida pronta.")
    
    def ferver_agua(self):
        print("Fervendo água.")
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("Passando a água no pó do café.")
    
    def servir(self):
        print("Servindo em uma xícara pequena.")


class Cha(BebidaQuente):
    def misturar(self):
        print("Mergulhando o saquinho de chá na água.")
    
    def servir(self):
        print("Servindo na caneca de porcelanato.")


class Leite(BebidaQuente):
    def misturar(self):
        print("Misturando o leite em pó na água.")
    
    def servir(self):
        print("Servindo na xícara grande.")