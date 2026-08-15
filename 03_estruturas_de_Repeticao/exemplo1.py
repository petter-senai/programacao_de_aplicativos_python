# ============================================================
# AULA: ESTRUTURAS CONDICIONAIS E DE REPETIÇÃO
# ============================================================


# ------------------------------------------------------------
# 1. ESTRUTURAS CONDICIONAIS
# ------------------------------------------------------------

# O if executa um bloco de código quando uma condição
# é verdadeira.

idade = 18

if idade >= 18:
    print("Maior de idade")


# O else é executado quando a condição do if é falsa.

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# O elif permite verificar várias condições.

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


# ------------------------------------------------------------
# 2. CONDIÇÕES COM OPERADORES LÓGICOS
# ------------------------------------------------------------

# Podemos combinar condições utilizando:
# and -> todas as condições devem ser verdadeiras
# or  -> pelo menos uma condição deve ser verdadeira
# not -> inverte o resultado

idade = 20
possui_ingresso = True

if idade >= 18 and possui_ingresso:
    print("Entrada permitida")
else:
    print("Entrada não permitida")


# ------------------------------------------------------------
# 3. ESTRUTURA DE REPETIÇÃO while
# ------------------------------------------------------------

# O while repete um bloco enquanto a condição
# for verdadeira.

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# ------------------------------------------------------------
# 4. ESTRUTURA DE REPETIÇÃO for
# ------------------------------------------------------------

# O for é utilizado para percorrer uma sequência
# ou repetir uma ação uma quantidade determinada de vezes.

for numero in range(1, 6):
    print(numero)


# ------------------------------------------------------------
# 5. PERCORRENDO UMA LISTA
# ------------------------------------------------------------

nomes = ["Ana", "Carlos", "João", "Maria"]

for nome in nomes:
    print(nome)


# ------------------------------------------------------------
# 6. BREAK
# ------------------------------------------------------------

# O break interrompe completamente a repetição.

for numero in range(1, 11):

    if numero == 6:
        break

    print(numero)


# ------------------------------------------------------------
# 7. CONTINUE
# ------------------------------------------------------------

# O continue interrompe apenas a repetição atual
# e passa para a próxima.

for numero in range(1, 11):

    if numero == 5:
        continue

    print(numero)


# ------------------------------------------------------------
# 8. PASS
# ------------------------------------------------------------

# O pass não executa nenhuma ação.
# Pode ser utilizado como espaço reservado
# para um código que será desenvolvido depois.

for numero in range(1, 6):

    if numero == 3:
        pass

    print(numero)


# ------------------------------------------------------------
# 9. CONDIÇÃO DENTRO DE REPETIÇÃO
# ------------------------------------------------------------

# Podemos utilizar estruturas condicionais
# dentro de estruturas de repetição.

for numero in range(1, 11):

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")


# ------------------------------------------------------------
# 10. REPETIÇÃO COM VALIDAÇÃO
# ------------------------------------------------------------

# O programa continua solicitando uma nota
# enquanto o valor informado for inválido.

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"Nota informada: {nota}")


# ------------------------------------------------------------
# 11. MENU COM while E break
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# 12. EXEMPLO PRÁTICO
# ------------------------------------------------------------

# O programa recebe 5 notas e informa a situação
# de cada aluno.

for numero in range(1, 6):

    nota = float(input(f"Digite a nota do aluno {numero}: "))

    if nota >= 7:
        print("Aprovado")

    elif nota >= 5:
        print("Recuperação")

    else:
        print("Reprovado")


# ------------------------------------------------------------
# 13. EXERCÍCIO
# ------------------------------------------------------------

# Crie um programa de menu que fique sendo executado
# até que o usuário escolha a opção "0".
#
# O menu deve possuir:
#
# 1 - Verificar número
# 2 - Tabuada
# 3 - Contagem
# 0 - Sair
#
# Na opção 1:
# Solicite um número e informe se ele é positivo,
# negativo ou zero.
#
# Na opção 2:
# Solicite um número e mostre sua tabuada de 1 a 10.
#
# Na opção 3:
# Mostre os números de 1 a 10.
#
# Utilize:
# if / elif / else
# while
# for
# break
# continue