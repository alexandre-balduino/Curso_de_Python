'''
Desafio 024

Simule uma cafeteira orientada a objetos
    |-----------------------------|
    |   BebidaQuente {abstract}   |
    |=============================|
    | + preparar()                |
    | + ferver_agua()             |
    | + misturar() {abstract}     |
    | + servir() {abstract}       |
    |-----------------------------|
                   ∆
                   |
       |-------------------------|
       |           |             |
|--------------|   |   |--------------|
| Cafe         |   |   |   Cha        |
|==============|   |   |==============|
| + misturar() |   |   | + misturar() |
| + servir()   |   |   | + servir()   |
|--------------|   |   |--------------|
                   |
            |--------------|
            |   Leite      |
            |==============|
            | + misturar() |
            | + servir()   |
            |--------------|
'''
