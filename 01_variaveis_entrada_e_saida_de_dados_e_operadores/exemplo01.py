# ============================================================
# AULA: VARIÁVEIS, ENTRADA, SAÍDA E OPERADORES EM PYTHON
# ============================================================


# ------------------------------------------------------------
# 1. VARIÁVEIS E TIPOS DE DADOS
# ------------------------------------------------------------

# Em Python não precisamos declarar o tipo da variável.
# O Python identifica o tipo automaticamente.

nome = "João"       # str - texto
idade = 18          # int - número inteiro
altura = 1.75       # float - número decimal
aprovado = True     # bool - verdadeiro ou falso

print(nome)
print(idade)
print(altura)
print(aprovado)


# Podemos verificar o tipo de uma variável usando type().

print(type(nome))
print(type(idade))
print(type(altura))
print(type(aprovado))


# ------------------------------------------------------------
# 2. ENTRADA DE DADOS
# ------------------------------------------------------------

# O input() recebe informações digitadas pelo usuário.
#
# IMPORTANTE:
# O input() sempre retorna uma String.

nome = input("Digite seu nome: ")

print("Olá,", nome)


# Para receber um número inteiro, usamos int().

idade = int(input("Digite sua idade: "))

print("Sua idade é:", idade)


# Para receber um número decimal, usamos float().

altura = float(input("Digite sua altura: "))

print("Sua altura é:", altura)


# ------------------------------------------------------------
# 3. SAÍDA DE DADOS
# ------------------------------------------------------------

# O print() mostra informações na tela.

print("Olá, mundo!")

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)


# Podemos utilizar f-string para deixar a saída
# mais organizada.

print(f"Meu nome é {nome} e tenho {idade} anos.")


# ------------------------------------------------------------
# 4. OPERADORES ARITMÉTICOS
# ------------------------------------------------------------

numero1 = 10
numero2 = 3

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)


# Operadores que merecem atenção no Python:

resto = numero1 % numero2
potencia = numero1 ** numero2
divisao_inteira = numero1 // numero2

print("Resto:", resto)
print("Potência:", potencia)
print("Divisão inteira:", divisao_inteira)


# ------------------------------------------------------------
# 5. OPERADORES RELACIONAIS
# ------------------------------------------------------------

idade = 18

print(idade == 18)   # Igual
print(idade != 18)   # Diferente
print(idade > 18)    # Maior
print(idade < 18)    # Menor
print(idade >= 18)   # Maior ou igual
print(idade <= 18)   # Menor ou igual


# Os operadores relacionais retornam:
# True  -> verdadeiro
# False -> falso


# ------------------------------------------------------------
# 6. OPERADORES LÓGICOS
# ------------------------------------------------------------

idade = 20
possui_carteira = True

# and -> todas as condições precisam ser verdadeiras

resultado = idade >= 18 and possui_carteira

print(resultado)


# or -> pelo menos uma condição precisa ser verdadeira

resultado = idade >= 18 or possui_carteira

print(resultado)


# not -> inverte o resultado

resultado = not possui_carteira

print(resultado)


# ------------------------------------------------------------
# 7. EXEMPLO PRÁTICO
# ------------------------------------------------------------

# Vamos criar um pequeno programa para calcular
# o valor de uma compra.

produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço do produto: "))


# Calculando o valor total.

total = quantidade * preco


# Mostrando os resultados.

print("\n===== RESUMO DA COMPRA =====")

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço: R$ {preco:.2f}")
print(f"Total: R$ {total:.2f}")


# ------------------------------------------------------------
# 8. EXEMPLO PRÁTICO COM MÉDIA
# ------------------------------------------------------------

nome = input("Nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("\n===== RESULTADO =====")

print(f"Aluno: {nome}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")


# ------------------------------------------------------------
# 9. EXERCÍCIO
# ------------------------------------------------------------

# Crie um programa que receba:
#
# Nome do funcionário
# Salário
# Percentual de aumento
#
# Depois calcule:
#
# Valor do aumento
# Novo salário
#
# Exemplo:
#
# Nome: Carlos
# Salário: 2500
# Aumento: 10%
#
# Resultado:
# Aumento: R$ 250
# Novo salário: R$ 2750