'''
Desafio 105

Faça um programa que tenha uma 
função chamada notas(), que pode 
receber várias notas de alunos e 
vai retornar um dicionário com as 
seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
'''

def notas(*notas, situacao=False):
    """
    -> Função para analisar nota e situação de vários alunos.
    :param notas: uma ou mais notas dos alunos
    :param situacao: (opcional) indica se deve mostrar a situação dos alunos
    :return: dicionário com informações sobre as notas
    """
    if len(notas) == 0:
        return {}
    dados = {
        "quant": len(notas),
        "maior": max(notas),
        "menor": min(notas),
        "media": sum(notas) / len(notas)
    }
    if situacao:
        if dados["media"] >= 7:
            dados["situacao"] = "APROVADO"
        elif dados["media"] >= 5:
            dados["situacao"] = "RECUPERAÇÃO"
        else:
            dados["situacao"] = "REPROVADO"
    return dados


print(notas(6, 7))
print(notas(7, 6, 8, 7, situacao=True))
print(notas())