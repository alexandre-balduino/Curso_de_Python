'''
Desafio 019

Crie a classe Livro,
que vai simular a passagem de páginas
de um livro, considerando também se o 
usuário chegou ao fim da leitura.
'''

from rich import print
from time import sleep

class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = 1
    
    
    def __str__(self):
        return f"Você está na {self.pagina_atual}ª página do livro {self.nome}"
    
    
    def mudar_pagina(self, paginas):
        for pagina in range(paginas):
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                print(f"[black]{self.pagina_atual}[black]", end=" > ")
                sleep(0.2)
            else:
                print("Não é possível mudar de página, você chegou no final do livro")
                break


livro = Livro("Aprendendo a programar com python", 232)
print(livro)
livro.mudar_pagina(30)
print(livro)