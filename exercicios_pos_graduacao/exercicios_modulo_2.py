#Escrever um programa que leia 3 valores A, B e C, e os escreva em ordem crescente. 

#fazendo de forma simples, hardcode

# A = input("Insira o valor de A: ")
# B = input("Insira o valor de B: ")
# C = input("Insira o valor de C: ")

# if A > B:
#     A, B = B, A
# if A > C:
#     A, C = C, A
# if B > C:
#     B, C = C, B
    
# print("Valores em ordem crescente:", A, B, C)

#forma menos simples

# tam_lista = int(input("insira a quantidade de números que quer ordenar: "))

# lista_num = []

# for posicao in range(tam_lista):
#     num = int(input(f"Digite o valor {posicao + 1}: "))
#     lista_num.append(num)
    
# for posicao in range(tam_lista - 1):
#     for posicao_prox in range(posicao + 1, tam_lista):
#         if lista_num[posicao] > lista_num[posicao_prox]:
#             lista_num[posicao], lista_num[posicao_prox] = lista_num[posicao_prox], lista_num[posicao]
            
# print("Os numeros ordenados são: ", lista_num)

##########################################################################################------------------- 

#Faça um programa que leia uma data qualquer (dia, mês e ano) e calcule a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro tem 29 dias.

#(Dica: um ano é bissexto quando for divisível por 4)

# from datetime import timedelta, datetime

# data = input("Insira a data no formato: dd/mm/aaaa: ")


# data_convert = datetime.strptime(data, "%d/%m/%Y")
# #print(data_convert)

# soma_dia = data_convert + timedelta(1)
# print(soma_dia.strftime("%d/%m/%Y"))

#####################################################################################################################################

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

# nome = input("Insira seu nome: ")

# genero = input("Insira seu genero biologico (F feminino M masculino): ")

# estado_civil = input("Estado civil: ")

# if genero.upper() == "F" and estado_civil.upper() == "CASADA":
#     tempo_casada = input("Insira o tempo de casada (anos): ")
#     print(f"Nome: {nome}, Genero: {genero}, Estado Civil: {estado_civil}, Tempo Casada:{tempo_casada}")
# else:
#     print("Gratidão")


#############################################################################################
#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela. 


# a = int(input("Insira um valor A: "))
# b = int(input("Insira um valor B: "))

# if a == b:
#     c = a + b
#     print(f"Como A e B são iguais, obtemos o valor C através da soma dos dois. Logo, C = {c}")
# else:
#     print(f"Como A e B não são iguais, obtemos o valor C através da multiplicação dos dois. Logo, C = {a * b}")


####################################################################################################3
#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

# a = int(input("Insira um valor: "))

# if a > 0:
#     print(f'O resultado é: {a * 2}')
# else:
#     print(f'O resultado é: {a * 3}')

##################################################################################################
#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação. 

# a = int(input("Insira um valor: "))

# if a % 2 == 0:
#     print(f"O resultado é {a + 5}")
# else:
#     print(f"O resultado é {a + 8}")

##########################################################################################################

# O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar umaindicação sobre a condição de peso de uma pessoa adulta. 
# A fórmula é IMC = peso / ( altura )2

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.

# IMC em adultos Condição Abaixo

# de 18,5 Abaixo do peso
# Entre 18,5 e 25 Peso normal
# Entre 25 e 30
# Acima do peso Acima de 30 obeso

# peso = float(input("Insira seu peso: "))
# altura = float(input("Insira sua altura: "))


# imc = round(peso / ((altura)**2),2)

# if imc <= 18.5:
#     print("Abaixo do peso")
# elif 18.5 < imc <= 25:
#     print("Peso normal")
# elif 25 < imc <= 30:
#     print("Acima do peso")
# else: 
#     print("Obeso")






######################################################################################################

# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

# Código Condição de pagamento: 

# À vista em dinheiro ou cheque, recebe 10% de desconto
# À vista no cartão de crédito, recebe 15% de desconto
# Em duas vezes, preço normal de etiqueta sem juros
# Em duas vezes, preço normal de etiqueta mais juros de 10%

# print(" 1. À vista em dinheiro ou cheque")
# print(" 2. À vista no cartão de crédito") 
# print(" 3. Em duas vezes")
# print(" 4. Em três vezes")

# opcao = int(input("Insira o numero da opção desejada conforme acima: "))
# preco = float(input("Insira o valor em R$: "))

# if opcao == 1:
#     print(f"Valor a pagar: {(preco*0.9):.2f}")
# elif opcao == 2:
#     print(f"Valor a pagar: {(preco*0.85):.2f}")
# elif opcao == 3: 
#     print(f'Valor a pagar: duas parcelas de {(preco/2):.2f}, totalizando {preco:.2f}')
# elif opcao == 4:
#     preco_juros = preco * 1.1
#     print(f'Valor a pagar: tres parcelas de {(preco_juros/3):.2f}, totalizando {preco_juros:.2f}')
# else:
#     print("Opção inválida!")


###############################################################################################################


# Faça um programa, utilizando estrutura de condição, que receba um número real, 
# digitado pelo usuário e mostre o menu para selecionar o tipo de cálculo que deve ser realizado com base nos códigos abaixo:

# 101-Raiz quadrada
# 102-A metade
# 103-10% do número
# 104-O dobro

# num = float(input("Insira um numero: "))

# print("Dadas as seguintes opções:")
# print("101-Raiz quadrada")
# print("102-A metade")
# print("103-10% do número")
# print("104-O dobro")

# opcao = input("Insira um valor: ")

# if opcao == "101":
#     print(f"{(num ** 0.5):.2f}")
# elif opcao == "102":
#     print(f"{(num * 0.5):.2f}")
# elif opcao == "103":
#     print(f"{(num * 0.1):.2f}")
# elif opcao == "104":
#     print(f"{(num * 2):.2f}")
# else:
#     print("Opção inválida!")
seq = 'AUUCCUUCTGG'
seq = seq.replace('A','G')
seq = seq.replace('U','T')

G = seq.count('G')
C = seq.count('C')
T = seq.count('T')
print (G, C, T)