## Perguntas
- O que significa **encapsulamento**?
- Quais são as **vantagens** de **proteger** os objetos?
- É verdade que o **Python não protege** nada?
- Como implementar **visibilidade** de **atributos**?
- O que é **name mangling** (mutilação de nome)?


Pilares da POO

## Encapsulando objetos e protegendo tudo

Parte 1

## Encapsulamento

Visa manter a **integridade** do sistema, **protegendo** o **estado interno** do objeto contra **interferência** externa não regulamentada.

Ex: Controle remoto
O que fazemos para **proteger** os **circuitos** e **componentes** internos?
Envolvemos ele em uma **"cápsula"** que deixa **exposto** apenas o que é **acessível**.

Ex: Comprimido
Qual é o **objetivo** em usar uma **cápsula** gelatinosa nos **remédios**?
* **Isola** a **dose exata** dos compostos?
* **Impede** a ação de fatores **externos** (umidade, luz, ...)
* **Protege** o paciente do gosto **amargo** e da **toxicidade** direta

## Principais **vantagens**:
- Segurança e controle
- Facilidade de manutenção
- Flexibilidade e reutilização
- Redução de efeitos colaterais


## Para realizar essa **proteção**, precisamos entender:
- Visibilidade dos atributos
- Acesso aos dados protegidos

### Visibilidade
Existem **três tipos** de **visibilidade** para atributos em linguagens **POO**:
- public +
- projected #
- private -

## Consenting Adults
Liberdade com Responsabilidade

---

A:
atrib1 public*
_atrib2 *protejected*
__atrib3 *private*