# Estruturas Condicionais, Estruturas de Repetição e Controle de Repetições

Este material apresenta estruturas fundamentais para o desenvolvimento de programas em Python. Serão estudadas as estruturas condicionais, responsáveis pela tomada de decisões, as estruturas de repetição, utilizadas para executar comandos várias vezes, e os comandos de controle de repetição `break`, `continue` e `pass`.

## Índice

1. [Introdução](#1-introdução)
2. [Estruturas Condicionais](#2-estruturas-condicionais)

   * 2.1. `if`
   * 2.2. `if / else`
   * 2.3. `if / elif / else`
3. [Estruturas de Repetição](#3-estruturas-de-repetição)

   * 3.1. `while`
   * 3.2. `for`
   * 3.3. `range()`
4. [Controle de Repetições](#4-controle-de-repetições)

   * 4.1. `break`
   * 4.2. `continue`
   * 4.3. `pass`
5. [Combinando Condições e Repetições](#5-combinando-condições-e-repetições)
6. [Exemplos Práticos](#6-exemplos-práticos)

   * 6.1. Menu com `while` e `break`
   * 6.2. Verificação de Notas
7. [Atividade](#7-atividade)

   * 7.1. Sistema de Menu

---

## 1. Introdução

Um programa precisa ser capaz de tomar decisões e executar determinadas tarefas várias vezes.

Por exemplo, um sistema pode:

* Verificar se um usuário possui permissão.
* Identificar se um aluno foi aprovado.
* Repetir uma operação enquanto uma condição for verdadeira.
* Percorrer uma sequência de números.
* Exibir um menu até que o usuário escolha sair.
* Interromper uma repetição quando determinada condição acontecer.
* Ignorar uma etapa específica de uma repetição.

Em Python, essas funcionalidades podem ser desenvolvidas utilizando estruturas condicionais e estruturas de repetição.

---

## 2. Estruturas Condicionais

As estruturas condicionais permitem que o programa escolha diferentes caminhos de execução de acordo com uma condição.

As principais estruturas são:

* `if`
* `else`
* `elif`

### 2.1. `if`

O `if` executa um bloco de código quando uma condição é verdadeira.

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

Nesse exemplo, a mensagem será exibida somente se a idade for maior ou igual a 18.

---

### 2.2. `if / else`

O `else` define o que deverá acontecer quando a condição do `if` for falsa.

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

O programa possui dois possíveis caminhos:

```text
Condição verdadeira → if
Condição falsa      → else
```

---

### 2.3. `if / elif / else`

O `elif` permite verificar várias condições.

```python
nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

Nesse exemplo:

* Nota maior ou igual a 7 → Aprovado.
* Nota maior ou igual a 5 → Recuperação.
* Nota menor que 5 → Reprovado.

---

## 3. Estruturas de Repetição

As estruturas de repetição permitem executar um determinado bloco de código várias vezes.

Em Python, as principais estruturas são:

* `while`
* `for`

A escolha da estrutura depende da situação que queremos resolver.

---

### 3.1. `while`

O `while` executa um bloco de código enquanto uma condição for verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

O resultado será:

```text
1
2
3
4
5
```

O programa continua executando o bloco enquanto:

```text
contador <= 5
```

for verdadeiro.

É importante alterar a variável utilizada na condição para evitar uma repetição infinita.

---

### 3.2. `for`

O `for` é utilizado para percorrer uma sequência ou repetir uma determinada quantidade de vezes.

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```text
1
2
3
4
5
```

O `for` é muito utilizado quando sabemos previamente quantas vezes uma determinada operação deverá ser executada.

---

### 3.3. `range()`

A função `range()` é frequentemente utilizada junto com o `for`.

Sua forma básica é:

```python
range(inicio, fim)
```

Por exemplo:

```python
for numero in range(1, 6):
    print(numero)
```

O valor inicial é incluído, mas o valor final não é.

Portanto:

```text
range(1, 6)
```

gera:

```text
1, 2, 3, 4, 5
```

Também podemos utilizar `range()` com apenas um valor:

```python
for numero in range(5):
    print(numero)
```

Nesse caso, a contagem começa em `0`:

```text
0
1
2
3
4
```

---

## 4. Controle de Repetições

Python possui comandos que permitem controlar o comportamento das estruturas de repetição.

Os principais são:

* `break`
* `continue`
* `pass`

---

### 4.1. `break`

O `break` interrompe imediatamente a repetição.

Exemplo:

```python
contador = 1

while contador <= 10:

    print(contador)

    if contador == 5:
        break

    contador += 1
```

Nesse caso, a repetição será interrompida quando o contador chegar a `5`.

Resultado:

```text
1
2
3
4
5
```

O `break` é muito utilizado em menus, sistemas de busca e situações em que precisamos encerrar uma repetição antes do seu final normal.

---

### 4.2. `continue`

O `continue` interrompe apenas a execução atual da repetição e passa para a próxima.

Exemplo:

```python
for numero in range(1, 6):

    if numero == 3:
        continue

    print(numero)
```

Resultado:

```text
1
2
4
5
```

Quando o número é `3`, o `continue` faz com que o restante daquela repetição seja ignorado.

---

### 4.3. `pass`

O `pass` não executa nenhuma ação.

Ele é utilizado quando precisamos criar uma estrutura que ainda não possui uma implementação.

Exemplo:

```python
idade = 20

if idade >= 18:
    pass
```

Nesse caso, o `pass` funciona como um espaço reservado para um código que poderá ser desenvolvido posteriormente.

---

## 5. Combinando Condições e Repetições

As estruturas condicionais e de repetição podem ser utilizadas juntas.

Por exemplo, podemos percorrer vários números e verificar uma condição para cada um deles.

```python
for numero in range(1, 11):

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
```

Nesse programa:

1. O `for` percorre os números de 1 a 10.
2. O `if` verifica cada número.
3. O operador `%` verifica o resto da divisão por 2.
4. O programa informa se o número é par ou ímpar.

Esse tipo de combinação é muito comum no desenvolvimento de sistemas.

---

## 6. Exemplos Práticos

### 6.1. Menu com `while` e `break`

Um menu pode permanecer em execução até que o usuário escolha a opção de sair.

```python
while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastro selecionado.")

    elif opcao == "2":
        print("Consulta selecionada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
```

Nesse exemplo, `while True` cria uma repetição contínua.

A repetição somente será encerrada quando o usuário escolher a opção `0`.

O comando responsável por encerrar o `while` é:

```python
break
```

Esse padrão é bastante utilizado em sistemas que possuem menus interativos.

---

### 6.2. Verificação de Notas

Podemos utilizar `for` para receber cinco notas e verificar a situação de cada aluno.

```python
for numero in range(1, 6):

    nota = float(input(f"Digite a nota do aluno {numero}: "))

    if nota >= 7:
        print("Aprovado")

    elif nota >= 5:
        print("Recuperação")

    else:
        print("Reprovado")
```

Nesse exemplo, o `for` executa o código cinco vezes.

A cada repetição:

1. Uma nota é solicitada.
2. A nota é analisada.
3. O programa informa a situação do aluno.

---

## 7. Atividade

### 7.1. Sistema de Menu

Crie um programa de menu que permaneça em execução até que o usuário escolha a opção `0`.

O menu deverá possuir as seguintes opções:

```text
1 - Verificar número
2 - Tabuada
3 - Contagem
0 - Sair
```

### Opção 1: Verificar número

Solicite um número ao usuário e informe se ele é:

* Positivo.
* Negativo.
* Zero.

Utilize:

```python
if
elif
else
```

### Opção 2: Tabuada

Solicite um número e mostre sua tabuada de 1 a 10.

Exemplo:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

Utilize:

```python
for
range()
```

### Opção 3: Contagem

Mostre os números de 1 a 10.

Utilize uma estrutura de repetição.

### Opção 0: Sair

Encerre o programa e apresente uma mensagem informando que o programa foi encerrado.

Utilize:

```python
break
```

### Desafio

Utilize também o comando `continue` para tratar alguma situação específica do programa.

O objetivo da atividade é utilizar, em um único programa:

```text
if
elif
else
while
for
break
continue
```

Essa atividade reúne os principais conceitos estudados neste material e prepara o aluno para desenvolver programas mais interativos e estruturados.
