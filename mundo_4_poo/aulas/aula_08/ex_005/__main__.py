
from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main(inspecionar=False):
    a1 = Aluno("Jose", 17, "Informática", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    
    p1 = Professor("Samuel", 37, "Biologia", "Mestre")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    
    f1 = Funcionario("Claudia", 27, "Secretária", "Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    
    if inspecionar:
        inspect(a1, methods=True)
        inspect(p1, methods=True)
        inspect(f1, methods=True)

if __name__ == "__main__":
    main()