# Listas, Tuplas e Dicionários

Este material apresenta três estruturas de dados fundamentais da linguagem Python: **listas, tuplas e dicionários**.

Essas estruturas permitem armazenar e organizar várias informações dentro de um programa. Elas são utilizadas em situações como cadastro de alunos, produtos, clientes, notas, informações de usuários e registros de sistemas.

## Índice

1. [Introdução](#1-introdução)
2. [Listas](#2-listas)

   * 2.1. Criando uma Lista
   * 2.2. Índices
   * 2.3. Alterando Elementos
   * 2.4. Adicionando Elementos
   * 2.5. Removendo Elementos
   * 2.6. Tamanho da Lista
   * 2.7. Percorrendo uma Lista
   * 2.8. Verificando se um Elemento Existe
   * 2.9. Listas com Diferentes Tipos de Dados
   * 2.10. Listas de Números
3. [Tuplas](#3-tuplas)

   * 3.1. Criando uma Tupla
   * 3.2. Acessando Elementos
   * 3.3. Percorrendo uma Tupla
   * 3.4. Diferença entre Lista e Tupla
   * 3.5. Quando Utilizar Tuplas
4. [Dicionários](#4-dicionários)

   * 4.1. Criando um Dicionário
   * 4.2. Acessando Valores
   * 4.3. Alterando Valores
   * 4.4. Adicionando Dados
   * 4.5. Removendo Dados
   * 4.6. Percorrendo um Dicionário
   * 4.7. Verificando uma Chave
5. [Estruturas Combinadas](#5-estruturas-combinadas)

   * 5.1. Dicionário com Lista
   * 5.2. Lista de Dicionários
6. [Exemplo Prático](#6-exemplo-prático)
7. [Resumo das Estruturas](#7-resumo-das-estruturas)

---

## 1. Introdução

Durante o desenvolvimento de programas, frequentemente precisamos armazenar várias informações relacionadas.

Imagine, por exemplo, um sistema escolar que precisa armazenar:

```text
Ana
Carlos
João
Maria
```

Criar uma variável diferente para cada nome não seria uma boa solução.

Em vez disso, podemos utilizar uma **lista**:

```python id="v9y8tg"
nomes = ["Ana", "Carlos", "João", "Maria"]
```

Da mesma forma, podemos utilizar outras estruturas para organizar diferentes tipos de informações.

As principais estruturas estudadas neste material são:

| Estrutura  | Característica principal                        |
| ---------- | ----------------------------------------------- |
| Lista      | Armazena vários valores e pode ser alterada     |
| Tupla      | Armazena vários valores e não pode ser alterada |
| Dicionário | Armazena informações no formato chave e valor   |

---

# 2. Listas

As listas são utilizadas para armazenar vários valores dentro de uma única variável.

Uma lista é criada utilizando colchetes `[]`.

### 2.1. Criando uma Lista

```python id="g9h7i4"
nomes = ["Ana", "Carlos", "João", "Maria"]

print(nomes)
```

Resultado:

```text id="2fby3a"
['Ana', 'Carlos', 'João', 'Maria']
```

Uma lista pode armazenar vários elementos.

---

## 2.2. Índices

Cada elemento de uma lista possui uma posição chamada de **índice**.

Em Python, o primeiro índice é `0`.

Considerando:

```python id="7b2q1d"
nomes = ["Ana", "Carlos", "João", "Maria"]
```

Temos:

| Índice | Valor  |
| -----: | ------ |
|      0 | Ana    |
|      1 | Carlos |
|      2 | João   |
|      3 | Maria  |

Podemos acessar cada elemento utilizando seu índice:

```python id="y7qk9e"
print(nomes[0])
print(nomes[1])
print(nomes[2])
```

Também podemos utilizar índices negativos.

O índice `-1` representa o último elemento:

```python id="9omw8e"
print(nomes[-1])
```

---

## 2.3. Alterando Elementos

As listas são **mutáveis**.

Isso significa que seus elementos podem ser alterados depois que a lista foi criada.

```python id="8ddx5j"
nomes = ["Ana", "Carlos", "João", "Maria"]

nomes[0] = "Pedro"

print(nomes)
```

A lista passa a ser:

```text id="8sh2jb"
['Pedro', 'Carlos', 'João', 'Maria']
```

---

## 2.4. Adicionando Elementos

O método `append()` adiciona um elemento ao final da lista.

```python id="iq0a7g"
nomes.append("Lucas")

print(nomes)
```

Também podemos utilizar `insert()` para adicionar um elemento em uma posição específica.

```python id="w7c5c3"
nomes.insert(1, "Mariana")

print(nomes)
```

Nesse exemplo, `"Mariana"` será adicionada na posição `1`.

---

## 2.5. Removendo Elementos

Podemos remover elementos de uma lista de diferentes maneiras.

O método `remove()` remove um elemento pelo seu valor.

```python id="xq0j5u"
nomes.remove("Lucas")

print(nomes)
```

O método `pop()` remove um elemento utilizando seu índice.

```python id="kjw3gi"
nomes.pop(0)

print(nomes)
```

---

## 2.6. Tamanho da Lista

A função `len()` informa a quantidade de elementos existentes na lista.

```python id="6x8p8n"
nomes = ["Ana", "Carlos", "João", "Maria"]

print(len(nomes))
```

Resultado:

```text id="2efzqx"
4
```

---

## 2.7. Percorrendo uma Lista

Podemos utilizar o `for` para percorrer todos os elementos de uma lista.

```python id="j0h48t"
nomes = ["Ana", "Carlos", "João", "Maria"]

for nome in nomes:
    print(nome)
```

O programa executará o `print()` para cada elemento da lista.

---

## 2.8. Verificando se um Elemento Existe

O operador `in` permite verificar se determinado elemento está presente na lista.

```python id="2u6b7z"
nomes = ["Ana", "Carlos", "João", "Maria"]

if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")
```

Esse recurso é bastante útil para realizar pesquisas.

---

## 2.9. Listas com Diferentes Tipos de Dados

Uma lista pode armazenar diferentes tipos de dados.

```python id="a1h1om"
dados = ["João", 18, 1.75, True]

print(dados)
```

Nesse exemplo temos:

* `str` → `"João"`
* `int` → `18`
* `float` → `1.75`
* `bool` → `True`

Apesar de ser possível misturar tipos, em aplicações reais é importante organizar os dados de maneira adequada à finalidade do programa.

---

## 2.10. Listas de Números

As listas também são muito utilizadas para armazenar valores numéricos.

```python id="y6f3m2"
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"Média: {media:.1f}")
```

Nesse exemplo, o programa percorre todas as notas, calcula a soma e depois divide pela quantidade de notas.

---

# 3. Tuplas

As tuplas são semelhantes às listas, porém possuem uma diferença importante:

**Tuplas não podem ser alteradas depois de criadas.**

Uma tupla é criada utilizando parênteses `()`.

---

## 3.1. Criando uma Tupla

```python id="c2g5mb"
coordenadas = (10, 20)

print(coordenadas)
```

A tupla possui dois valores:

```text id="6xwqj3"
10
20
```

---

## 3.2. Acessando Elementos

Assim como nas listas, os elementos de uma tupla possuem índices.

```python id="u8gqv2"
coordenadas = (10, 20)

print(coordenadas[0])
print(coordenadas[1])
```

O primeiro elemento está no índice `0`.

---

## 3.3. Percorrendo uma Tupla

Podemos utilizar o `for` para percorrer os elementos.

```python id="7yphm2"
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

for dia in dias:
    print(dia)
```

---

## 3.4. Diferença entre Lista e Tupla

A principal diferença está na possibilidade de alteração.

### Lista

Pode ser alterada:

```python id="gjxgdu"
frutas = ["maçã", "banana", "laranja"]

frutas[0] = "uva"

print(frutas)
```

### Tupla

Não pode ser alterada:

```python id="5v8qk4"
frutas = ("maçã", "banana", "laranja")
```

A tentativa de executar:

```python id="iy4e1c"
frutas[0] = "uva"
```

causaria um erro.

---

## 3.5. Quando Utilizar Tuplas

As tuplas são úteis quando temos informações que não devem ser alteradas durante a execução do programa.

Por exemplo, uma data de nascimento:

```python id="7q3w2h"
data_nascimento = (15, 8, 2008)

print(data_nascimento)
```

Outro exemplo poderia ser uma coordenada:

```python id="f08m26"
coordenada = (10, 20)
```

---

# 4. Dicionários

Os dicionários armazenam informações utilizando o formato:

```text id="k7u0q5"
chave: valor
```

Um dicionário é criado utilizando chaves `{}`.

Os dicionários são muito utilizados para representar registros.

---

## 4.1. Criando um Dicionário

```python id="sl9gcm"
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)
```

Nesse exemplo:

| Chave   | Valor  |
| ------- | ------ |
| `nome`  | Carlos |
| `idade` | 17     |
| `nota`  | 8.5    |

---

## 4.2. Acessando Valores

Podemos acessar um valor utilizando sua chave.

```python id="2tdr4r"
print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])
```

Diferentemente das listas, o acesso é realizado pela **chave**, e não pelo índice.

---

## 4.3. Alterando Valores

Os valores de um dicionário podem ser alterados.

```python id="e2o7cd"
aluno["nota"] = 9.0

print(aluno)
```

A nota que anteriormente era `8.5` passa a ser `9.0`.

---

## 4.4. Adicionando Dados

Podemos adicionar uma nova informação simplesmente atribuindo um valor a uma nova chave.

```python id="xg4t8n"
aluno["curso"] = "Informática"

print(aluno)
```

Agora o dicionário também possui a informação `"curso"`.

---

## 4.5. Removendo Dados

Podemos utilizar `del` para remover uma chave e seu respectivo valor.

```python id="f9x4l8"
del aluno["curso"]

print(aluno)
```

---

## 4.6. Percorrendo um Dicionário

Podemos percorrer as chaves de um dicionário utilizando o `for`.

```python id="w8b5po"
for chave in aluno:
    print(chave)
```

Também podemos acessar a chave e o valor ao mesmo tempo utilizando `items()`.

```python id="3xw5na"
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
```

---

## 4.7. Verificando uma Chave

Podemos verificar se determinada chave existe utilizando `in`.

```python id="v7c5s6"
if "nome" in aluno:
    print("A chave nome existe.")
```

Esse recurso pode ser utilizado antes de tentar acessar uma informação.

---

# 5. Estruturas Combinadas

Na programação, é muito comum combinar listas, tuplas e dicionários.

Essas combinações permitem representar estruturas de dados mais complexas.

---

## 5.1. Dicionário com Lista

Um dicionário pode armazenar uma lista como valor.

```python id="3hzl3a"
aluno = {
    "nome": "Maria",
    "notas": [8.0, 7.5, 9.0]
}

print(aluno["nome"])
print(aluno["notas"])
```

Também podemos acessar um elemento específico da lista dentro do dicionário.

```python id="2c3kwc"
print(aluno["notas"][0])
```

Nesse caso:

```text id="e3xjv7"
aluno
   ↓
"notas"
   ↓
[8.0, 7.5, 9.0]
   ↓
índice 0
   ↓
8.0
```

---

## 5.2. Lista de Dicionários

Uma estrutura muito utilizada em aplicações é uma lista contendo vários dicionários.

Por exemplo, podemos representar vários alunos:

```python id="8m5b7h"
alunos = [
    {
        "nome": "Ana",
        "idade": 17,
        "nota": 8.5
    },
    {
        "nome": "Carlos",
        "idade": 18,
        "nota": 7.0
    },
    {
        "nome": "João",
        "idade": 16,
        "nota": 9.0
    }
]
```

Podemos percorrer todos os alunos:

```python id="7q1t7k"
for aluno in alunos:
    print(aluno["nome"], aluno["nota"])
```

Essa estrutura é muito utilizada para representar vários registros em aplicações.

---

# 6. Exemplo Prático

Podemos utilizar uma lista de dicionários para representar um pequeno cadastro de produtos.

```python id="5tq3rf"
produtos = [
    {
        "nome": "Teclado",
        "preco": 89.90,
        "estoque": 10
    },
    {
        "nome": "Mouse",
        "preco": 49.90,
        "estoque": 15
    },
    {
        "nome": "Monitor",
        "preco": 899.90,
        "estoque": 5
    }
]

for produto in produtos:
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']}")
    print()
```

Nesse exemplo temos:

```text id="8e7x1p"
Lista
   ↓
Vários produtos
   ↓
Cada produto é um dicionário
   ↓
Cada dicionário possui:
nome
preço
estoque
```

Essa organização é muito próxima da maneira como informações são estruturadas em sistemas reais.

---

# 7. Resumo das Estruturas

## Lista

```python id="m2d7s4"
nomes = ["Ana", "Carlos", "João"]
```

Características:

* Utiliza `[]`.
* Possui índices.
* Pode ser alterada.
* Pode armazenar vários valores.
* Pode ser percorrida com `for`.

---

## Tupla

```python id="6g5j5a"
coordenadas = (10, 20)
```

Características:

* Utiliza `()`.
* Possui índices.
* Não pode ser alterada depois de criada.
* Pode armazenar vários valores.
* Pode ser percorrida com `for`.

---

## Dicionário

```python id="z2m7j7"
aluno = {
    "nome": "Carlos",
    "idade": 17
}
```

Características:

* Utiliza `{}`.
* Trabalha com chave e valor.
* Pode ser alterado.
* Permite representar registros.
* Pode ser percorrido com `for`.
* Pode conter listas e outras estruturas.

---

## Comparação Final

| Estrutura  | Símbolo | Índice                         | Pode alterar | Organização          |
| ---------- | ------- | ------------------------------ | ------------ | -------------------- |
| Lista      | `[]`    | Sim                            | Sim          | Sequência de valores |
| Tupla      | `()`    | Sim                            | Não          | Sequência de valores |
| Dicionário | `{}`    | Não utiliza índice tradicional | Sim          | Chave e valor        |

As listas, tuplas e dicionários são estruturas fundamentais para trabalhar com coleções de dados em Python. O domínio dessas estruturas será importante para desenvolver programas mais completos e, posteriormente, trabalhar com conceitos como funções, arquivos, APIs, bancos de dados e programação orientada a objetos.
