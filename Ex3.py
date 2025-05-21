# 3.Um posto está vendendo combustíveis com a seguinte tabela de descontos abaixo. 
# Escreva um programa que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), e ao final imprima o valor a ser 
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 6,50 o preço do litro 
# do álcool é R$ 5,60:

# Declaração
Tipo_comb = input("Qual o tipo de combustivel você vai querer?? \n A - Alcool, G - Gasolina: ")
Qtd_Litros  = float(input("Informe a quantidade de litros: "))

# Operação
if Tipo_comb == "A":
    if Qtd_Litros <=20:
        preço = 0.97 * 5.60 * Qtd_Litros
    elif Qtd_Litros >=20:
        preço = 0.95 * 5.60 * Qtd_Litros


if Tipo_comb == "G":
    if Qtd_Litros <=20:
        preço = 0.96 * 6.50 * Qtd_Litros
    elif Qtd_Litros >=20:
        preço = 0.94 * 6.50 * Qtd_Litros


# Resultado
print(f"O valor a ser pago é R$ {preço:.2f}")

