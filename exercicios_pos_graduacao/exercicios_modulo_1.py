# h = float(input("Digite sua altura: "))

# genero = input("Insira seu genero biologico (H para homem e M para mulher): ")

# if genero.upper() == "H":
#     calculo = (72.7*h) - 58
#     print(f"Seu peso ideial é: {calculo:.1f} ")
    
# elif genero.upper() == "M":
#     calculo = (62.1*h) - 44.7
#     print(f"Seu peso ideial é: {calculo:.1f}kg")
    
# else:
#     print("Gênero inserido é invalido")
    
#################################################################################################################

# vlr_hr = float(input("Quanto você ganha por hora? "))


# hrs_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))


# salario_bruto = vlr_hr * hrs_trabalhadas


# vlr_ir = salario_bruto * (0.11)


# vlr_inss = salario_bruto * (0.08)


# vlr_sind = salario_bruto * (0.05)


# salario_liquido = salario_bruto - vlr_ir - vlr_inss - vlr_sind

# print(f"+ Salário Bruto: R$ {salario_bruto}")
# print(f"- IR (11%): R$ {vlr_ir}")
# print(f"- INSS (8%): R$ {vlr_inss}")
# print(f"- Sindicato (5%): R$ {vlr_sind}")
# print(f"= Salário Líquido: R$ {salario_liquido}")


#################################################################################################################

# area_pintada = float(input("Insira área a ser pintada em m²: "))

# rendimento_lt = 6 


# nesc_lts_tinta = round((area_pintada/rendimento_lt * 1.1),2)



# qtd_latas = int((nesc_lts_tinta / 18) +1)
# vlr_total_lata = qtd_latas * 80

# qtd_galao =  int((nesc_lts_tinta / 3.6) +1)
# vlr_galao = qtd_galao * 25

# qtd_lata_misturado = int((nesc_lts_tinta / 18))
# resto_lata = nesc_lts_tinta % 18

# qtd_resto_galao = int(resto_lata/3.6) + (1 if resto_lata != 0 else 0 )
# print(f"x = {x}")


# total_lata_galao = qtd_lata_misturado + qtd_resto_galao
# vlr_total_lata_galao = (qtd_lata_misturado * 80) + (qtd_resto_galao * 25)


# print(f"Opção 1: Será necessário: {qtd_latas} lata(s) de tinta de 18L, totalizando um valor de R$ {vlr_total_lata}")
      
# print(f"Opção 2: Será necessário {qtd_galao} lata(s) de tinta de 3.6L, totalizando um valor de R$ {vlr_galao}")

# print(f"Opção 3: Será necessário {qtd_lata_misturado} lata(s) de tinta de 18L e {qtd_resto_galao} lata(s) de tinta de 3.6L, totalizando um valor de R$ {vlr_total_lata_galao}")

#################################################################################################################

# nota1 = float(input("Insira a primeira nota bimestral: "))
# nota2 = float(input("Insira a segunda nota bimestral: "))
# nota3 = float(input("Insira a terceira nota bimestral: "))
# nota4 = float(input("Insira a quarta nota bimestral: "))

# soma = nota1 + nota2 + nota3 + nota4

# media = soma/4

# print(f"A média dessa pessoa é: {media:.2f}")

#################################################################################################################
# tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download em MB: "))


# velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))


# tempo_download_minutos = (tamanho_arquivo_mb / (velocidade_internet_mbps / 8)) / 60  # Convertendo de Mbps para MBps
# tempo_download_minutos = round(tempo_download_minutos, 2)


# print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos} minutos.")
