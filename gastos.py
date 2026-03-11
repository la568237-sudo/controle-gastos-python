def adicionar_gasto():
    descricao = input("Descrição do gasto: ")
    valor = input("Valor: ")

    with open("gastos.txt", "a") as arquivo:
        arquivo.write(descricao + " - R$ " + valor + "\n")

    print("Gasto registrado com sucesso!\n")


def ver_gastos():
    try:
        with open("gastos.txt", "r") as arquivo:
            print("\nLista de gastos:\n")
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhum gasto registrado ainda.\n")


while True:
    print("Controle de Gastos")
    print("1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_gasto()

    elif opcao == "2":
        ver_gastos()

    elif opcao == "3":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida\n")
