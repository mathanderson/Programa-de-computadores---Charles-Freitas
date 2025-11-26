saldo = 0

opcao = ""

while opcao != "X" and opcao != "x":
    print("C - Credito")
    print("D - Debito")
    print("S - Saldo")
    print("X - Sair")

    opcao = input("Opcao: ")

    if opcao == "C" or opcao == "c":
        valor = float(input("Valor: "))
        if valor > 0:
            saldo = saldo + valor
        else:
            print("Valor invalido")

    elif opcao == "D" or opcao == "d":
        valor = float(input("Valor: "))
        if valor > 0:
            if valor <= saldo:
                saldo = saldo - valor
            else:
                print("Saldo insuficiente")
        else:
            print("Valor invalido")

    elif opcao == "S" or opcao == "s":

        print("Saldo =", saldo)

    elif opcao == "X" or opcao == "x":

        print("Saldo final =", saldo)

    else:    print("Opcao invalida")