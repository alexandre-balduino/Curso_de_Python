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
    def __init__(self):
        pass
    
    def preparar(self):
        print("preparando")
    
    def ferver_agua(self):
        print("fervendo água")
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print()
    
    def servir(self):
        print()


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print()
    
    def servir(self):
        print()


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print()
    
    def servir(self):
        print()