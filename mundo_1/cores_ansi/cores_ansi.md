# 🎨 ANSI Escape Codes (Guia Completo)

## 🧠 O que são?

ANSI é um padrão que permite controlar o terminal usando **sequências de escape**.

Tudo começa com:

```
\033[
```

ou
```
\x1b[
```
E termina com:
```
m
```
---

## 📊 Tabela ANSI
| ESTILO | COR_TEXTO | COR_FUNDO |
|--------|----------|-----------|
| 0 (reset) | 30 (preto) | 40 (preto) |
| 1 (negrito) | 31 (vermelho) | 41 (vermelho) |
| 2 (fraco) | 32 (verde) | 42 (verde) |
| 4 (sublinhado) | 33 (amarelo) | 43 (amarelo) |
| 5 (piscando) | 34 (azul) | 44 (azul) |
| 7 (invertido) | 35 (magenta) | 45 (magenta) |
| — | 36 (ciano) | 46 (ciano) |
| — | 37 (branco) | 47 (branco) |
---

## 🧠 Sintaxe
\033[ESTILO;COR_TEXTO;COR_FUNDOm

### 🔍 Exemplo
```python
print("\033[1;31;43mTexto estilizado\033[m")
```

1 → negrito
31 → vermelho
43 → fundo amarelo

📍 Posicionar texto na tela

Sintaxe
```
\033[LINHA;COLUNAH
```
ou
```
\033[LINHA;COLUNAf
```
Exemplo
```Python
print("\033[10;20HOlá mundo")
```
👉 Linha 10, coluna 20
🧹 Limpar tela
```
\033[2J
```
```Python
print("\033[2J")
```
🔝 Ir para o topo
```
\033[H
```
🔄 Limpar linha atual
```
\033[K
```
🧭 Movimentação do cursor
Código
Ação
```
\033[nA
```
sobe n linhas
```
\033[nB
```
desce n linhas
```
\033[nC
```
direita n colunas
```
\033[nD
```
esquerda n colunas

💾 Salvar/restaurar cursor
```
\033[s   # salvar posição
\033[u   # restaurar posição
```
👀 Mostrar / esconder cursor
```
\033[?25l   # esconder cursor
\033[?25h   # mostrar cursor
```
🎨 Cores avançadas (256 cores)
Texto
```
\033[38;5;NUMm
```
Fundo
```
\033[48;5;NUMm
```
Exemplo
```Python
print("\033[38;5;202mTexto colorido avançado\033[m")
```
🚀 Exemplo prático (barra de progresso)
```Python
import time

print("\033[2J")  # limpa tela

for i in range(101):
    print(f"\033[5;10HCarregando: {i}%")
    time.sleep(0.05)
```
⚠️ Observações
Funciona perfeitamente no Termux
Pode não funcionar no IDLE
Sempre use:
```
\033[m
```
para resetar o terminal
🧠 Resumo
Com ANSI você controla:
🎨 Cores
📍 Posição
🧭 Movimento
💅 Estilo
⚙️ Comportamento do terminal
🔥 Ideal para:
Menus CLI
Dashboards
Sistemas interativos
Projetos estilo terminal