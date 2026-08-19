# ============================================================
# AULA: LISTAS, TUPLAS E DICIONÁRIOS
# ============================================================


# ------------------------------------------------------------
# 1. LISTAS
# ------------------------------------------------------------

# Listas são utilizadas para armazenar vários valores
# dentro de uma única variável.

nomes = ["Ana", "Carlos", "João", "Maria"]

print(nomes)


# ------------------------------------------------------------
# 2. ACESSANDO ELEMENTOS DA LISTA
# ------------------------------------------------------------

# Os elementos possuem posições, chamadas de índices.
# O primeiro elemento começa no índice 0.

print(nomes[0])
print(nomes[1])
print(nomes[2])


# Podemos acessar o último elemento usando -1.

print(nomes[-1])


# ------------------------------------------------------------
# 3. ALTERANDO ELEMENTOS
# ------------------------------------------------------------

# As listas são mutáveis, ou seja, seus elementos
# podem ser alterados.

nomes[0] = "Pedro"

print(nomes)


# ------------------------------------------------------------
# 4. ADICIONANDO ELEMENTOS
# ------------------------------------------------------------

# append() adiciona um elemento no final da lista.

nomes.append("Lucas")

print(nomes)


# insert() adiciona um elemento em uma posição específica.

nomes.insert(1, "Mariana")

print(nomes)


# ------------------------------------------------------------
# 5. REMOVENDO ELEMENTOS
# ------------------------------------------------------------

# remove() remove um elemento pelo seu valor.

nomes.remove("Lucas")

print(nomes)


# pop() remove um elemento pelo índice.

nomes.pop(0)

print(nomes)


# ------------------------------------------------------------
# 6. TAMANHO DA LISTA
# ------------------------------------------------------------

# len() informa a quantidade de elementos.

print(len(nomes))


# ------------------------------------------------------------
# 7. PERCORRENDO UMA LISTA
# ------------------------------------------------------------

for nome in nomes:
    print(nome)


# ------------------------------------------------------------
# 8. VERIFICANDO SE UM ELEMENTO EXISTE
# ------------------------------------------------------------

if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")


# ------------------------------------------------------------
# 9. LISTA COM DIFERENTES TIPOS DE DADOS
# ------------------------------------------------------------

dados = ["João", 18, 1.75, True]

print(dados)


# ------------------------------------------------------------
# 10. LISTA DE NÚMEROS
# ------------------------------------------------------------

notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"Média: {media:.1f}")


# ------------------------------------------------------------
# 11. TUPLAS
# ------------------------------------------------------------

# Tuplas são semelhantes às listas.
# A principal diferença é que tuplas não podem
# ser alteradas depois de criadas.

coordenadas = (10, 20)

print(coordenadas)


# Acessando elementos.

print(coordenadas[0])
print(coordenadas[1])


# ------------------------------------------------------------
# 12. TUPLA COM VÁRIOS VALORES
# ------------------------------------------------------------

dias = ("segunda", "terça", "quarta", "quinta", "sexta")

print(dias)

for dia in dias:
    print(dia)


# ------------------------------------------------------------
# 13. DIFERENÇA ENTRE LISTA E TUPLA
# ------------------------------------------------------------

# Lista → pode ser alterada.

frutas = ["maçã", "banana", "laranja"]

frutas[0] = "uva"

print(frutas)


# Tupla → não pode ser alterada.

frutas = ("maçã", "banana", "laranja")

# A linha abaixo causaria um erro:
# frutas[0] = "uva"


# ------------------------------------------------------------
# 14. QUANDO USAR TUPLAS
# ------------------------------------------------------------

# Podemos utilizar tuplas para informações que
# não devem ser alteradas.

data_nascimento = (15, 8, 2008)

print(data_nascimento)


# ------------------------------------------------------------
# 15. DICIONÁRIOS
# ------------------------------------------------------------

# Dicionários armazenam informações no formato:
#
# chave: valor

aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)


# ------------------------------------------------------------
# 16. ACESSANDO VALORES DO DICIONÁRIO
# ------------------------------------------------------------

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])


# ------------------------------------------------------------
# 17. ALTERANDO VALORES
# ------------------------------------------------------------

aluno["nota"] = 9.0

print(aluno)


# ------------------------------------------------------------
# 18. ADICIONANDO NOVOS DADOS
# ------------------------------------------------------------

aluno["curso"] = "Informática"

print(aluno)


# ------------------------------------------------------------
# 19. REMOVENDO DADOS
# ------------------------------------------------------------

del aluno["curso"]

print(aluno)


# ------------------------------------------------------------
# 20. PERCORRENDO UM DICIONÁRIO
# ------------------------------------------------------------

for chave in aluno:
    print(chave)


# Podemos acessar chave e valor ao mesmo tempo.

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


# ------------------------------------------------------------
# 21. VERIFICANDO UMA CHAVE
# ------------------------------------------------------------

if "nome" in aluno:
    print("A chave nome existe.")


# ------------------------------------------------------------
# 22. DICIONÁRIO COM LISTA
# ------------------------------------------------------------

aluno = {
    "nome": "Maria",
    "notas": [8.0, 7.5, 9.0]
}

print(aluno["nome"])
print(aluno["notas"])


# Podemos acessar um elemento da lista dentro do dicionário.

print(aluno["notas"][0])


# ------------------------------------------------------------
# 23. LISTA DE DICIONÁRIOS
# ------------------------------------------------------------

# Essa estrutura é muito utilizada em aplicações
# para representar vários registros.

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

for aluno in alunos:
    print(aluno["nome"], aluno["nota"])


# ------------------------------------------------------------
# 24. EXEMPLO PRÁTICO
# ------------------------------------------------------------

# Cadastro de produtos utilizando uma lista
# de dicionários.

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


# ------------------------------------------------------------
# 25. RESUMO
# ------------------------------------------------------------

# LISTA
# - Utiliza []
# - Pode ser alterada
# - Possui índices
#
# TUPLA
# - Utiliza ()
# - Não pode ser alterada
# - Possui índices
#
# DICIONÁRIO
# - Utiliza {}
# - Trabalha com chave e valor
# - Pode ser alterado
# - Muito utilizado para representar registros