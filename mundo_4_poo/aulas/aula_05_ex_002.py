
# Como melhorar a classe da aula anterior?
# Como documentar uma classe?
# Como descobrir a classe de um objeto?
# Como obter o estado de um objeto?
# Me mostre um exemplo mais útil?


# Declaração de Classe
class Gafanhoto:
    """
Gafanhoto é uma pessoa que tem nome e idade

para criar um gafanhoto use:
variável = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0):
        # Atributos de Instancia
        self.nome = nome
        self.idade = idade
    
    # Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado : nome = {self.nome}; idade = {self.idade}"

g1 = Gafanhoto(nome="Maria", idade=17)
g1.aniversario()
#print(g1.mensagem())
#print(g1.__doc__)
#print(g1)
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Método
print(g1.__class__)

'''
g2 = Gafanhoto(nome="Mauro", idade=53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto("vazio")
print(g3.mensagem())
'''
