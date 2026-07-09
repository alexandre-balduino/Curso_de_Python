# Desafio 003

Sua missão neste desafio é pegar a nossa mesma tabela de informática e resolver 3 problemas práticos de alteração e resumo de dados.

---

### Suas Tarefas:

​- **Correção de Dados** (O "UPDATE" do Pandas): O estagiário cadastrou a categoria da Impressora HP como 'Printers' (em inglês). Modifique esse valor específico para ficar em português: 'Periféricos'.
​
- **A Inflação Chegou** (Operação em Massa): Devido às taxas de importação, todos os produtos da loja sofreram um aumento de 10% no preço. Atualize a coluna 'Preço' refletindo esse novo valor para todos os produtos de uma só vez (sem usar for!).
​
- **Resumo por Categoria** (O "GROUP BY" do Pandas): O gerente quer saber quantos produtos a loja tem no estoque total somando por cada Categoria. Agrupe os dados e mostre essa soma.
​
---

### O Código Inicial:

```python
dados_informatica = {
    'Produto': ['Notebook Dell', 'Teclado Mecânico', 'Monitor LG 29"', 'Mouse Gamer', 'Impressora HP', 'SSD 1TB'],
    'Categoria': ['Notebooks', 'Periféricos', 'Monitores', 'Periféricos', 'Printers', 'Armazenamento'],
    'Preço': [4200.00, 250.00, 1350.00, 180.00, 890.00, 410.00],
    'Estoque': [5, 15, 4, 22, 3, 18]
}
```
