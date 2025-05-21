# 1.Faça um programa que verifique se a nota de um aluno está no intervalo entre 0 e 10. 
# Mostre uma mensagem caso o valor esteja fora deste intervalo e leia a nota 
# novamente até que o usuário informe um valor válido.

# Declaração
while True:
    Nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
    if 0 <= Nota <= 10:
        print(f"Nota válida: {Nota}")
        break
    else:
        print("Nota inválidade. Por favor, digite novamente um valor entre 0 e 10.")

