'''
Desafio 027

Simule o sistema de batalha entre 
personagens de um RPG

    |-------------------------|
    |   Personagem {abstract} |
    |=========================|
    | + nome                  |
    | + vida                  |
    | + golpes                |
    |-------------------------|
    | + atacar(alvo, forca)   |
    | + receber_dano(dano)    |
    | + curar() {abstract}    |
    |-------------------------|
                ∆
                |
        |--------------|
        |              |
|-------------|   |-----------|
|   Guerreiro |   |   Mago    |
|=============|   |===========|
| + curar()   |   | + curar() |
|-------------|   |-----------|
'''
