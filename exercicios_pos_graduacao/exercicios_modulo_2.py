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

tam_lista = 3
#int(input("insira a quantidade de números que quer ordenar: "))

lista_num = []

for posicao in range(tam_lista):
    num = int(input(f"Digite o valor {posicao + 1}: "))
    lista_num.append(num)
    
for posicao in range(tam_lista - 1):
    for posicao_prox in range(posicao + 1, tam_lista):
        if lista_num[posicao] > lista_num[posicao_prox]:
            lista_num[posicao], lista_num[posicao_prox] = lista_num[posicao_prox], lista_num[posicao]
            
print("Os numeros ordenados são: ", lista_num)

#------------------- 