# Abstração

## Perguntas

- O que é **abstração**?
- O que é **interface pública**?
- O que é uma **classe abstrata**?
- O que é um **método concreto**?
- Você conhece as siglas **ABC** e **DRY**?

---

### Os **4 pilares** da **P**rogramação **O**rientada a **O**bjetos

- Abstração
- Encapsulamento
- Herança
- Polimorfismo

 ---

## Abstração

É a prática de **ignorar** o **irrelevante** e se **focar** estritamente no **essencial**

### Principais vantagens:
- Maior legibilidade
- Padronização
- Simplificação
- Segurança

---

Existe a **abstração de dados**, que acontece quando **ignoramos** *informações desnecessárias* para o escopo do projeto.

Existe a **abstração de processos**, quando não precisamos saber *como um método faz* seu trabalho, apenas sabe que **ele existe** pela *interface*.

---

## Exemplo

### Classe Abstrata:

Controle Genérico

### Métodos Abstratos:

- ligar()
- desligar()
- aumentar_volume()
- diminuir_volume()
- avançar_canal()
- retroceder_canal()

---

### Classe Abstrata:

`Pessoa`
- `nome`
- `idade`
- `fazer_aniversario()`
- `estudar() {abstract}`

### Classes Especializadas

| **`Aluno`** | **`Professor`** | **`Funcionario`** |
| :--- | :--- | :--- |
| `curso` | `especialidade` | `cargo` |
| `turma` | `nível` | `setor` |
| `fazer_natrícula()` | `dar_aula()` | `bater_ponto()` |
| `estudar()` | `estudar()` | `estudar()` |

---

Uma **classe abstrata** *nunca será instanciada*, já que ela é usada apenas como base para as **subclasses**.

Ao definir um conjunto de **métodos abstratos**, dizemos que estamos criando a **interface pública** da **classe**

Uma **classe abstrata** pode ter **métodos abstratos** que deverão ser *obrigatóriamente*  implementados nas **subclasses**.

Mas uma **classe abstrata** pode ter **métodos concretos** se eles funcionarem da mesma maneira para todas as **subclasses** (**DRY**).
