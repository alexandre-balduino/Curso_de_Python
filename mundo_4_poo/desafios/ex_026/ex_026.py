'''
Desafio 026

Crie a estrutura capaz de calcular 
salários de funciinários diferentes

    |--------------------------|
    |   Funciinario {abstract} |
    |==========================|
    | + nome                   |
    | + sal_bruto              |
    | + salario                |
    | + sal_minimo = 1612      |
    | + inss                   |
    |--------------------------|
    | + calc_sal() {abstract}  |
    | + analisar_sal()         |
    |--------------------------|
                   ∆
                   |
         |--------------------|
|----------------|    |---------------|
|   Horista      |    |   Mensalista  |
|================|    |===============|
| + valor_hora() |    | + calc_sal()  |
| + horas_trab() |    |---------------|
|----------------|
| + calc_sal()   |
|----------------|
'''
