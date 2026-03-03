'''
Desafio 022

Crie a classe ControleRemoto, 
onde vamos simular o funcionamento 
de um controle simples (canal, 
volume e liga/desliga)
'''

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.volume = 3
        self.canal = 1
    
    
    def liga_desliga(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True
    
    
    def aumentar_volume(self):
        if self.volume < 5:
            self.volume += 1
    
    
    def diminuir_volume(self):
        if self.volume > 1:
            self.volume -= 1
    
    
    def avancar_canal(self):
        if self.canal < 5:
            self.canal += 1
        elif self.canal == 5:
            self.canal = 1
    
    
    def voltar_canal(self):
        if self.canal > 1:
            self.canal -= 1
        elif self.canal == 1:
            self.canal = 5
