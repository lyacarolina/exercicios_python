#Hexadecimal output

#teoria com exemplo
# num hexadecimal => 3E0A
#para converter para decimal:
# 3 * 16^3 + E * 16^2 + 0 * 16^1 + A * 16^0
#precisa indexar as posições -> 3[0], E[1], 0[2], A[3] ---> func ENUMARATE
#multiplicar o dígito com o inverso das posições listadas -----> func REVERSED
#como iremos calcular a conversão de um num na base 16 para inteiro, é preciso passar dois argumentos na func int
#int(num_para_converter, 16) ---> 16 é a base





def hex_output():
    decnum = 0
    
    hexnum = input('Digite um número hexadecimal para converter: ')
    
    for power, digit in enumerate(reversed(hexnum)):
        decnum = decnum + (int(digit,16) * (16**power))
    print(decnum)
    
hex_output()