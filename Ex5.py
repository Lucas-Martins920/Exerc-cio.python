# Variavel
soma = 0
quantidade = 0
menor = None
maior = None

print("Digite as temperaturas (digite 100 para parar):")

# Declaração
while True:
    temp = float(input("Temperatura: "))

    if temp == 100:
        break

    soma += temp
    quantidade += 1

    if menor is None or temp < menor:
        menor = temp

    if maior is None or temp > maior:
        maior = temp

# Final
if quantidade > 0:
    media = soma / quantidade
    print(f"\nMenor temperatura: {menor}")
    print(f"Maior temperatura: {maior}")
    print(f"Média das temperaturas: {media:.2f}")
else:
    print("\nNenhuma temperatura válida foi digitada.")
