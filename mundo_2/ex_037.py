'''
Desafio 037

Escreva um programa em Python que 
leia um número inteiro qualquer e 
peça para o usuário escolher qual 
será a base de conversão: 
    1 para binário, 
    2 para octal e 
    3 para hexadecimal.
'''

num = int(input("Digite um número: "))
opcao = int(input("[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal \nEscolha uma opção: "))
if opcao == 1:
    print(f"O número {num} convertido para binário é {bin(num)[2:]}")
elif opcao == 2:
    print(f"O número {num} convertido para octal é {oct(num)[2:]}")
elif opcao == 3:
    print(f"O número {num} convertido para hexadecimal é {hex(num)[2:]}")
else:
    print("Opção inválida!")
    