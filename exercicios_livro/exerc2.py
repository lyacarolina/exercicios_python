def mysum(*numbers):
    soma = 0
    for number in numbers:
        soma = soma + number
    return soma

resultado = mysum(10, 10, 50, 100)
print(resultado)