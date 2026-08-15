# Operadores Lógicos e Estruturas Condicionais

Este material apresenta os principais conceitos relacionados à tomada de decisões em Python. Serão estudados os operadores de comparação, os operadores lógicos e as estruturas condicionais `if`, `elif` e `else`.

## Índice

1. [Introdução](#1-introdução)
2. [Operadores de Comparação](#2-operadores-de-comparação)
3. [Operadores Lógicos](#3-operadores-lógicos)

   * 3.1. Operador `and`
   * 3.2. Operador `or`
   * 3.3. Operador `not`
4. [Estrutura Condicional `if`](#4-estrutura-condicional-if)
5. [Estrutura `if / else`](#5-estrutura-if--else)
6. [Estrutura `if / elif / else`](#6-estrutura-if--elif--else)
7. [Uso de Várias Condições](#7-uso-de-várias-condições)
8. [Condições Dentro de Condições](#8-condições-dentro-de-condições)
9. [Exemplos Práticos](#9-exemplos-práticos)

   * 9.1. Sistema de Login
   * 9.2. Média do Aluno
   * 9.3. Sistema de Desconto
10. [Atividades](#10-atividades)

    * 10.1. Classificação por Idade
    * 10.2. Sistema de Login
    * 10.3. Situação do Aluno

---

## 1. Introdução

Os operadores lógicos e as estruturas condicionais permitem que um programa tome decisões de acordo com determinadas condições.

Por exemplo, um sistema pode verificar:

* Se um usuário informou a senha correta.
* Se um aluno atingiu a média necessária.
* Se uma pessoa possui idade suficiente para acessar determinado serviço.
* Se um cliente possui direito a um desconto.
* Se um usuário está autorizado a acessar um sistema.

Esses recursos são fundamentais para criar programas capazes de analisar situações e executar diferentes ações.

---

## 2. Operadores de Comparação

Os operadores de comparação são utilizados para comparar valores. O resultado de uma comparação será sempre `True` ou `False`.

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

---

## 3. Operadores Lógicos

Os operadores lógicos permitem combinar duas ou mais condições.

Em Python, os principais operadores lógicos são:

* `and`
* `or`
* `not`

### 3.1. Operador `and`

O operador `and` significa **E**.

Todas as condições precisam ser verdadeiras para que o resultado seja `True`.

```python
idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira

print(resultado)
```

Nesse exemplo, a pessoa precisa:

1. Ter 18 anos ou mais.
2. Possuir carteira.

As duas condições precisam ser verdadeiras.

---

### 3.2. Operador `or`

O operador `or` significa **OU**.

Pelo menos uma das condições precisa ser verdadeira.

```python
idade = 16
acompanhado = True

resultado = idade >= 18 or acompanhado

print(resultado)
```

Nesse caso, o acesso será permitido se a pessoa tiver 18 anos ou mais **ou** estiver acompanhada.

---

### 3.3. Operador `not`

O operador `not` significa **NÃO** e inverte o resultado de uma condição.

```python
aluno_matriculado = True

print(not aluno_matriculado)
```

Como a variável possui o valor `True`, o operador `not` transforma o resultado em `False`.

---

## 4. Estrutura Condicional `if`

A estrutura `if` permite executar um bloco de código quando determinada condição for verdadeira.

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
```

Nesse exemplo, a mensagem será exibida somente se `idade >= 18` for verdadeira.

A indentação é importante em Python, pois define quais instruções pertencem ao `if`.

---

## 5. Estrutura `if / else`

O `else` permite definir o que deve acontecer quando a condição do `if` for falsa.

```python
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

O programa possui dois possíveis caminhos:

* Condição verdadeira → `if`
* Condição falsa → `else`

---

## 6. Estrutura `if / elif / else`

Quando existem várias possibilidades, podemos utilizar o `elif`.

O `elif` permite testar uma nova condição caso a condição anterior seja falsa.

```python
nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

Nesse exemplo:

* Nota maior ou igual a 7 → Aprovado.
* Nota entre 5 e 6.9 → Recuperação.
* Nota menor que 5 → Reprovado.

---

## 7. Uso de Várias Condições

Os operadores lógicos podem ser utilizados dentro das estruturas condicionais.

### Utilizando `and`

```python
nota = 8
frequencia = 80

if nota >= 7 and frequencia >= 75:
    print("Aluno aprovado")
else:
    print("Aluno não aprovado")
```

O aluno precisa atender às duas condições:

* Nota maior ou igual a 7.
* Frequência maior ou igual a 75%.

### Utilizando `or`

```python
administrador = False
professor = True

if administrador or professor:
    print("Acesso permitido")
else:
    print("Acesso negado")
```

Nesse caso, basta uma das condições ser verdadeira.

---

## 8. Condições Dentro de Condições

É possível colocar uma estrutura condicional dentro de outra.

```python
idade = 20
documento = True

if idade >= 18:

    if documento:
        print("Entrada permitida")
    else:
        print("Apresente seu documento")

else:
    print("Entrada não permitida")
```

Esse recurso é chamado de **condicional aninhada**.

O programa primeiro verifica a idade. Caso a pessoa seja maior de idade, verifica se possui documento.

---

## 9. Exemplos Práticos

### 9.1. Sistema de Login

Um sistema de login pode utilizar `and` para verificar se o usuário e a senha estão corretos.

```python
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso")
else:
    print("Usuário ou senha incorretos")
```

As duas informações precisam estar corretas para permitir o acesso.

---

### 9.2. Média do Aluno

Podemos utilizar estruturas condicionais para determinar a situação de um aluno.

```python
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Aluno: {nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
```

O programa calcula a média e utiliza `if`, `elif` e `else` para definir a situação.

---

### 9.3. Sistema de Desconto

Estruturas condicionais também podem ser utilizadas em sistemas comerciais.

```python
valor = float(input("Digite o valor da compra: "))

if valor >= 500:
    desconto = valor * 0.10
elif valor >= 200:
    desconto = valor * 0.05
else:
    desconto = 0

valor_final = valor - desconto

print(f"Valor da compra: R$ {valor:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
```

Nesse exemplo:

* Compras a partir de R$ 500 recebem 10% de desconto.
* Compras a partir de R$ 200 recebem 5% de desconto.
* Compras abaixo de R$ 200 não recebem desconto.

---

## 10. Atividades

### 10.1. Classificação por Idade

Crie um programa que receba a idade de uma pessoa e classifique sua faixa etária.

Regras:

* Menor que 12 → Criança.
* De 12 até 17 → Adolescente.
* De 18 até 59 → Adulto.
* 60 ou mais → Idoso.

Utilize `if`, `elif` e `else`.

---

### 10.2. Sistema de Login

Crie um programa de login que solicite:

* Usuário.
* Senha.

O acesso deverá ser permitido somente quando:

```text
Usuário: admin
Senha: 1234
```

Caso contrário, o programa deverá apresentar:

```text
Acesso negado
```

Utilize o operador lógico `and`.

---

### 10.3. Situação do Aluno

Crie um programa para verificar se um aluno foi aprovado.

Solicite:

* Nota.
* Frequência.

Utilize as seguintes regras:

```text
Nota >= 7 e frequência >= 75 → Aprovado

Nota >= 5 e frequência >= 75 → Recuperação

Caso contrário → Reprovado
```

Utilize operadores lógicos e estruturas condicionais para resolver o problema.
