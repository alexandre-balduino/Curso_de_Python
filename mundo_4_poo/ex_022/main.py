
from os import system
from rich import print
from rich.panel import Panel
from ex_022 import ControleRemoto

def main():
    controle = ControleRemoto()
    while True:
        system("clear")
        if not controle.ligado:
            visor = f"[red]A TV está desligada[/]"
        else:
            canais = [str(i) for i in range(1, 6)]
            canais[controle.canal - 1] = f"[blue]{controle.canal}[/]"
            canal = "CANAL = " + " ".join(canais)
            barra_vol = "■" * controle.volume
            espaco_vol = " " * (5 - controle.volume)
            volume = f"VOLUME = [[blue]{barra_vol}[/]{espaco_vol}]"
            visor = f"{canal}\n{volume}"
            tv = Panel(visor, title="[ TV ]")
        print(tv)
        opcao = input(f"[ @ ] ON/OFF \n<CH{controle.canal}> \n-VOL{controle.volume}+\n").strip()
        match opcao:
            case "@":
                controle.liga_desliga()
            case "<":
                controle.voltar_canal()
            case ">":
                controle.avancar_canal()
            case "-":
                controle.diminuir_volume()
            case "+":
                controle.aumentar_volume()


main()