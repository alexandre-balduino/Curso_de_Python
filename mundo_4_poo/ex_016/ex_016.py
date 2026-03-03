'''
Desafio 016

Crie a classe Funcionario, 
onde podemos cadastrar nome, 
setor e cargo. 
Crie tambem um método que permita 
ao funcionário se apresentar.
'''

from rich import print

class Funcionario:
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    
    def apresentar(self):
        return f":wave: Olá, sou [blue] {self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {__class__.empresa}"


maria = Funcionario("Maria", "Administração", "Diretora")
pedro = Funcionario("Pedro", "TI", "Programador")
print(maria.apresentar())
print(pedro.apresentar())
