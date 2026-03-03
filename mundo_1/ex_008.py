'''
Desafio 008

Desenvolva um programa que leia um 
valor em metros e o exiba 
convertido em milímetros, 
centímetros, decímetros, decâmetros, 
hectômetros e quilômetros.
'''

metro = int(input("Digite um valor em metros: "))

milim = metro * 1000
centi = metro * 100
decim = metro * 10
decam = metro / 10
hecto = metro / 100
quilo = metro / 1000

print(f"A medida de {metro} em metros corresponde a: \n{milim} milímetros \n{centi} centímetros \n{decim} decímetros \n{decam} decâmetros \n{hecto} hectômetros \n{quilo} quilômetros")
