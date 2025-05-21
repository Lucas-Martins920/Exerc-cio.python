# Variavel
numeros = []

# Declaração
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Final
print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])
