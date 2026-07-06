# Desafio 002

Você recebeu uma tabela maior com o estoque de uma loja de informática. Seu objetivo é criar um programa em Python que carregue esses dados em um DataFrame e resolva 4 problemas de negócio usando filtros, ordenação e o acesso a linhas específicas que acabamos de aprender.
​
---

### Dados Iniciais para o seu código:

```python
dados_informatica = {
    'Produto': ['Notebook Dell', 'Teclado Mecânico', 'Monitor LG 29"', 'Mouse Gamer', 'Impressora HP', 'SSD 1TB'],
    'Categoria': ['Notebooks', 'Periféricos', 'Monitores', 'Periféricos', 'Printers', 'Armazenamento'],
    'Preço': [4200.00, 250.00, 1350.00, 180.00, 890.00, 410.00],
    'Estoque': [5, 15, 4, 22, 3, 18]
}
```

### Suas Tarefas:

​- **Filtro de Categoria**: Exiba na tela apenas os produtos que pertencem à categoria 'Periféricos'.
​
- **Alerta de Estoque Baixo**: O gerente precisa saber quais produtos estão com menos de 5 unidades no estoque. Filtre e mostre apenas essas linhas.
​
- **Ordenação de Preços**: Mostre a tabela completa, mas ordenada do produto mais caro para o mais barato (Preço decrescente).
​
- **Consulta VIP** (Acesso Específico): Descubra e mostre na tela apenas o nome do produto e o preço que estão exatamente na linha de índice de posição 4 (.iloc).
