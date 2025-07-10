menu = f"""

[d] Depoistar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor é inválido")

    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Você atingiu o limite de saques dários!")

        else:
            print(f"Seu limite de saque diário é: {LIMITE_SAQUES}.")
            print(f"Você fez {numero_saques} Saques hoje, ainda pode realizar {LIMITE_SAQUES - numero_saques} saques.")
            print(f"Seu limite por saque é: R$ {limite:.2f}")
            print(f"Seu saldo é: R$ {saldo:.2f}\n")

            saque = float(input("Qual valor deseja sacar: "))

            if saque > 0 and saldo > saque and saque < limite:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"

            elif saque > 0 and saque > saldo:
                print("Operação falhou! Saldo inválido para saque!")

            elif saque > 0 and saque > limite:
                print("Operação falhou! Saque maior que o limite")
                
            else:
                print("Operação falhou! O valor é inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")