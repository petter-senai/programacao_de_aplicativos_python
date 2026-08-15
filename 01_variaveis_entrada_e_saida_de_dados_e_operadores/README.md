# Variáveis, Entrada e Saída de Dados e Operadores

Este material apresenta os conceitos fundamentais para iniciar a programação em Python. Serão abordadas variáveis, tipos de dados, entrada e saída de informações e os principais operadores utilizados na linguagem.

## Índice

1. [Introdução](#1-introdução)
2. [Variáveis e Tipos de Dados](#2-variáveis-e-tipos-de-dados)

   * 2.1. String
   * 2.2. Inteiro
   * 2.3. Decimal
   * 2.4. Booleano
   * 2.5. Verificando o Tipo de uma Variável
3. [Entrada de Dados](#3-entrada-de-dados)

   * 3.1. Entrada de Texto
   * 3.2. Entrada de Números Inteiros
   * 3.3. Entrada de Números Decimais
4. [Saída de Dados](#4-saída-de-dados)

   * 4.1. Utilizando `print()`
   * 4.2. Utilizando F-strings
5. [Operadores Aritméticos](#5-operadores-aritméticos)

   * 5.1. Adição
   * 5.2. Subtração
   * 5.3. Multiplicação
   * 5.4. Divisão
   * 5.5. Resto da Divisão
   * 5.6. Potenciação
   * 5.7. Divisão Inteira
6. [Operadores Relacionais](#6-operadores-relacionais)
7. [Operadores Lógicos](#7-operadores-lógicos)

   * 7.1. Operador `and`
   * 7.2. Operador `or`
   * 7.3. Operador `not`
8. [Exemplos Práticos](#8-exemplos-práticos)

   * 8.1. Cálculo de uma Compra
   * 8.2. Cálculo de Média
9. [Atividade](#9-atividade)

   * 9.1. Cálculo de Salário com Aumento

---

## 1. Introdução

As variáveis, a entrada e saída de dados e os operadores são conceitos fundamentais para a construção de programas em Python.

Com esses recursos, é possível criar programas capazes de:

* Armazenar informações.
* Receber dados do usuário.
* Realizar cálculos.
* Comparar valores.
* Trabalhar com decisões lógicas.
* Exibir resultados na tela.

Esses conceitos formam uma das primeiras etapas no aprendizado da lógica de programação.

---

## 2. Variáveis e Tipos de Dados

Uma variável é utilizada para armazenar uma informação durante a execução do programa.

Em Python, não é necessário declarar previamente o tipo da variável. A própria linguagem identifica o tipo de dado armazenado.

```python
nome = "João"
idade = 18
altura = 1.75
aprovado = True
```

Nesse exemplo, foram criadas quatro variáveis com diferentes tipos de dados.

### 2.1. String

O tipo `str` é utilizado para armazenar textos.

```python
nome = "João"
```

Textos são normalmente escritos entre aspas simples ou duplas.

```python
nome1 = "João"
nome2 = 'Maria'
```

### 2.2. Inteiro

O tipo `int` representa números inteiros, positivos ou negativos.

```python
idade = 18
quantidade = 10
temperatura = -5
```

### 2.3. Decimal

O tipo `float` representa números que possuem casas decimais.

```python
altura = 1.75
preco = 29.90
```

Em Python, o separador decimal utilizado é o ponto.

```text
29.90
```

e não:

```text
29,90
```

### 2.4. Booleano

O tipo `bool` representa valores lógicos.

Existem apenas dois valores:

```python
True
False
```

Exemplo:

```python
aprovado = True
```

### 2.5. Verificando o Tipo de uma Variável

Podemos utilizar a função `type()` para verificar o tipo armazenado em uma variável.

```python
nome = "João"
idade = 18
altura = 1.75
aprovado = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(aprovado))
```

---

## 3. Entrada de Dados

A entrada de dados permite que o programa receba informações fornecidas pelo usuário.

Em Python, utilizamos a função `input()`.

### 3.1. Entrada de Texto

```python
nome = input("Digite seu nome: ")

print("Olá,", nome)
```

O usuário digita uma informação e ela é armazenada na variável `nome`.

Um ponto importante é que o `input()` sempre retorna uma informação do tipo `str`.

### 3.2. Entrada de Números Inteiros

Quando precisamos receber um número inteiro, utilizamos `int()`.

```python
idade = int(input("Digite sua idade: "))

print("Sua idade é:", idade)
```

O `int()` converte o texto recebido pelo `input()` para um número inteiro.

### 3.3. Entrada de Números Decimais

Para receber números com casas decimais, utilizamos `float()`.

```python
altura = float(input("Digite sua altura: "))

print("Sua altura é:", altura)
```

Nesse caso, o valor informado pelo usuário é convertido para `float`.

---

## 4. Saída de Dados

A saída de dados é utilizada para apresentar informações ao usuário.

Em Python, utilizamos principalmente a função `print()`.

### 4.1. Utilizando `print()`

```python
print("Olá, mundo!")

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
```

Podemos utilizar o `print()` para apresentar textos, valores armazenados em variáveis e resultados de operações.

### 4.2. Utilizando F-strings

As f-strings permitem inserir variáveis diretamente dentro de um texto.

```python
nome = "João"
idade = 18

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Também podemos formatar números.

```python
preco = 29.9

print(f"Preço: R$ {preco:.2f}")
```

O `.2f` indica que o número deverá ser apresentado com duas casas decimais.

---

## 5. Operadores Aritméticos

Os operadores aritméticos são utilizados para realizar cálculos matemáticos.

| Operador | Operação         | Exemplo   |
| -------- | ---------------- | --------- |
| `+`      | Adição           | `10 + 3`  |
| `-`      | Subtração        | `10 - 3`  |
| `*`      | Multiplicação    | `10 * 3`  |
| `/`      | Divisão          | `10 / 3`  |
| `%`      | Resto da divisão | `10 % 3`  |
| `**`     | Potenciação      | `10 ** 3` |
| `//`     | Divisão inteira  | `10 // 3` |

### 5.1. Adição

```python
numero1 = 10
numero2 = 3

soma = numero1 + numero2

print(soma)
```

### 5.2. Subtração

```python
subtracao = numero1 - numero2

print(subtracao)
```

### 5.3. Multiplicação

```python
multiplicacao = numero1 * numero2

print(multiplicacao)
```

### 5.4. Divisão

```python
divisao = numero1 / numero2

print(divisao)
```

A divisão `/` pode gerar um resultado com casas decimais.

### 5.5. Resto da Divisão

O operador `%` retorna o resto de uma divisão.

```python
resto = numero1 % numero2

print(resto)
```

Esse operador é bastante utilizado para verificar, por exemplo, se um número é par ou ímpar.

### 5.6. Potenciação

O operador `**` realiza uma potência.

```python
potencia = numero1 ** numero2

print(potencia)
```

Nesse exemplo, o programa calcula:

```text
10³
```

### 5.7. Divisão Inteira

O operador `//` realiza uma divisão inteira.

```python
divisao_inteira = numero1 // numero2

print(divisao_inteira)
```

Diferentemente do `/`, o resultado considera apenas a parte inteira da divisão.

---

## 6. Operadores Relacionais

Os operadores relacionais são utilizados para comparar valores.

O resultado de uma comparação será sempre `True` ou `False`.

| Operador | Significado    | Exemplo       |
| -------- | -------------- | ------------- |
| `==`     | Igual          | `idade == 18` |
| `!=`     | Diferente      | `idade != 18` |
| `>`      | Maior          | `idade > 18`  |
| `<`      | Menor          | `idade < 18`  |
| `>=`     | Maior ou igual | `idade >= 18` |
| `<=`     | Menor ou igual | `idade <= 18` |

Exemplo:

```python
idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)
```

Esses operadores serão importantes posteriormente para trabalhar com estruturas condicionais.

---

## 7. Operadores Lógicos

Os operadores lógicos permitem combinar ou inverter condições.

Os principais operadores são:

* `and` → E
* `or` → OU
* `not` → NÃO

### 7.1. Operador `and`

Todas as condições precisam ser verdadeiras.

```python
idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira

print(resultado)
```

### 7.2. Operador `or`

Pelo menos uma condição precisa ser verdadeira.

```python
resultado = idade >= 18 or possui_carteira

print(resultado)
```

### 7.3. Operador `not`

Inverte o resultado de uma condição.

```python
resultado = not possui_carteira

print(resultado)
```

---

## 8. Exemplos Práticos

### 8.1. Cálculo de uma Compra

Podemos utilizar variáveis, entrada de dados, conversão de tipos, operadores aritméticos e saída de dados para criar um pequeno sistema de compra.

```python
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço do produto: "))

total = quantidade * preco

print("\n===== RESUMO DA COMPRA =====")

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço: R$ {preco:.2f}")
print(f"Total: R$ {total:.2f}")
```

O programa:

1. Recebe o nome do produto.
2. Recebe a quantidade.
3. Recebe o preço.
4. Calcula o valor total.
5. Apresenta um resumo da compra.

### 8.2. Cálculo de Média

Também podemos utilizar esses conceitos para calcular a média de um aluno.

```python
nome = input("Nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("\n===== RESULTADO =====")

print(f"Aluno: {nome}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")
```

Nesse exemplo, o programa recebe duas notas, calcula a média e apresenta o resultado.

---

## 9. Atividade

### 9.1. Cálculo de Salário com Aumento

Crie um programa que receba as seguintes informações:

* Nome do funcionário.
* Salário atual.
* Percentual de aumento.

Depois, o programa deverá calcular:

* Valor do aumento.
* Novo salário.

Utilize variáveis, `input()`, conversão de tipos, operadores aritméticos e `print()`.

Exemplo:

```text
Nome: Carlos
Salário: 2500
Aumento: 10%
```

Resultado esperado:

```text
Aumento: R$ 250,00
Novo salário: R$ 2.750,00
```

O objetivo da atividade é utilizar, em um único programa, os principais conceitos apresentados neste material.
