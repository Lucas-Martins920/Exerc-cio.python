estoque = []

while True:
    print("\nMenu:")
    print("a) Cadastrar produto")
    print("b) Ver total financeiro de um produto")
    print("c) Ver nome e quantidade de todos os produtos")
    print("s) Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "a":
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        estoque.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        print("Produto cadastrado!")

    elif opcao == "b":
        nome = input("Nome do produto: ")
        for produto in estoque:
            if produto["nome"].lower() == nome.lower():
                total = produto["preco"] * produto["quantidade"]
                print(f"Total financeiro: R$ {total:.2f}")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "c":
        for produto in estoque:
            print(f"{produto['nome']}: {produto['quantidade']} unidades")

    elif opcao == "s":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
