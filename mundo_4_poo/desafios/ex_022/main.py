
import readchar
from os import system
from rich import print
from ex_022 import ControleRemoto

def main():
    controle = ControleRemoto()
    
    while True:
        print(
            controle.mostrar_tv(), 
            f"< CH{controle.canal_atual} >   - VOL{controle.canal_atual} + "
        )
        comando = readchar.readkey()
        match comando:
            case "0":
                break
            case "@":
                controle.liga_desliga()
            case ">":
                controle.canal_mais()
            case "<":
                controle.canal_menos()
            case "+":
                controle.volume_mais()
            case "-":
                controle.volume_menos()
        system("clear")
        
main()
 