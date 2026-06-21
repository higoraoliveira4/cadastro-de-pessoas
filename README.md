# Cadastro de Pessoas com Validação em Python

Projeto de estudo desenvolvido em Python que permite cadastrar várias pessoas, coletando dados como idade e sexo, com validação das entradas informadas pelo usuário.

## Objetivo do projeto

Praticar conceitos fundamentais da linguagem Python, como:

- Entrada de dados pelo terminal
- Estruturas de repetição (`while`)
- Estruturas condicionais (`if` e `elif`)
- Tratamento de erros com `try/except`
- Validação de dados do usuário
- Uso de contadores
- Controle de fluxo com `break`
- Manipulação de strings com `.upper()`

## Funcionalidades

- Solicita a idade da pessoa com validação numérica
- Solicita o sexo da pessoa com validação para `M` ou `F`
- Permite continuar ou encerrar o cadastro
- Exibe ao final:
  - Total de pessoas com mais de 18 anos
  - Total de homens cadastrados
  - Total de mulheres com menos de 20 anos
- Impede entradas inválidas, como letras no campo de idade ou opções diferentes de `S/N`

## Tecnologias utilizadas

- Python 3
- Execução via terminal ou IDE (PyCharm, VS Code, etc.)

## Exemplo de uso

```text
------------------------------ CADASTRE UMA PESSOA ------------------------------

Digite sua idade: 25
Digite seu sexo (M/F): M
Quer continuar? [S/N] S

------------------------------ CADASTRE UMA PESSOA ------------------------------

Digite sua idade: 17
Digite seu sexo (M/F): F
Quer continuar? [S/N] N

O total de pessoas com mais de 18 anos: 1
O total de homens cadastrados é 1
E temos 1 mulher com menos de 20 anos
