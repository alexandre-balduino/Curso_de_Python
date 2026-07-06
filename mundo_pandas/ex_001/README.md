# Desafio 001

---

Imagine que você recebeu um relatório bruto de vendas de uma pequena loja de eletrônicos em formato de dicionário Python. O seu chefe quer que você use o **Pandas** para organizar esses dados e extrair algumas informações cruciais.
​
Escreva um programa em Python que pegue o dicionário abaixo, transforme-o em um **DataFrame** do Pandas e faça as seguintes tarefas:

1.​ Mostre a tabela completa na tela de forma organizada.
​
2. Exiba apenas as 2 primeiras linhas do DataFrame para uma checagem rápida.
​
3. Mostre a estrutura dos dados (quantas linhas, colunas e os tipos de dados que estão ali dentro).
​
4. Adicione uma nova linha no final com o produto "Gabinete Gamer" que custa 450.00 e tem 8 unidades no estoque.
​
5. Calcule e mostre na tela o valor total do estoque da loja (Dica: você precisará multiplicar a coluna de preço pela de estoque e somar tudo).
​
---

 Dados Iniciais para colocar no seu código:

```python
dados_loja = {
    'Produto': ['Teclado Mecânico', 'Mouse Wireless', 'Monitor 24"', 'Headset RGB'],
    'Preço': [250.00, 120.00, 899.90, 310.00],
    'Estoque': [15, 30, 7, 12]
}
```
