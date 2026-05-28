
from ex_027 import *

def main():
    p1 = Guerreiro("Bárbaro", 1500)
    p2 = Mago("Excomungado", 2000)
    
    p1.atacar(p2, 2000)
    p2.atacar(p1)
    p1.atacar(p2)
    p1.curar()
    p2.curar()
    p2.atacar(p1)

if __name__ == "__main__":
    main()