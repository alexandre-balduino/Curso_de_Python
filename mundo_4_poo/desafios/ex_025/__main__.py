
from ex_025 import *
from rich import print, inspect
from rich.table import Table

def main():
    dist = 50
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")
    
    for item in viagem:
        tabela.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calcular_frete()}")
    
    print(tabela)

if __name__ == "__main__":
    main()
