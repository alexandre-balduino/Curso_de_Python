
from rich import print
from ex_008 import ContaBancaria

def main():
    c1 = ContaBancaria(id=112, nome="Gustavo", saldo=3000)
    c1.depositar(1_000)
    c1._titular = "Pedro"
    c1._ContaBancaria__saldo = 0
    print(c1)

if __name__ == "__main__":
    main()
