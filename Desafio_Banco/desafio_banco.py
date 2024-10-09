menu = """


[1] Depositar
[2] Sacar
[3] Transferir para poupança
[4] Extrato
[5] Sair

=> """

saldo_corrente = 0
saldo_poupanca = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo_corrente, extrato):
    try:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo_corrente += valor
            extrato += f"                               {valor:.2f}\n"
        else:
            print("Operação Inválida. Digite um valor positivo")
    except ValueError:
        print("Valor inválido. Tente novamente.")
    return saldo_corrente, extrato

def sacar(saldo_corrente, limite, extrato, numero_saques):
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo_corrente
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Inválida. Você não tem saldo suficiente")
        elif excedeu_limite:
            print("Operação Inválida. O valor de saque excede o limite")
        elif excedeu_saques:
            print("Operação Inválida. Número máximo de saques excedido")
        elif valor > 0:
            saldo_corrente -= valor
            extrato += f"     -{valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação Inválida. O valor informado é inválido")
    
        print("Valor inválido. Tente novamente.")
        return saldo_corrente, extrato, numero_saques

def transferir_poupanca(saldo_corrente, saldo_poupanca, extrato):
    try:
        valor = float(input("Digite o valor para depósito na poupança: "))
        if 0 < valor <= saldo_corrente:
            saldo_corrente -= valor
            saldo_poupanca += valor
            extrato += f"     -{valor:.2f} (Transferido para poupança)\n"
        elif valor > saldo_corrente:
            print("Valor maior que o saldo da conta corrente")
        else:
            print("Operação Inválida. O valor deve ser positivo")
    except ValueError:
        print("Valor inválido. Tente novamente.")
    return saldo_corrente, saldo_poupanca, extrato

def exibir_extrato (extrato, saldo_corrente, saldo_poupança):        
    print(" **************** Extrato *****************")
    print("      Débito                  Crédito      ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo Corrente: R$ {saldo_corrente:.2f}\nSaldo Poupança: R$ {saldo_poupanca:.2f}")
    print("*******************************************")


while True:
    
    opcao = input(menu).strip()  # Remove espaços em branco
    print(f"Você digitou: '{opcao}'")  # Mostra o que foi digitado

    if opcao == '1':
       saldo_corrente,extrato = depositar(saldo_corrente, extrato)
    elif opcao == '2':
       saldo_corrente, extrato, numero_saques = sacar(saldo_corrente, limite, extrato, numero_saques)
    elif opcao == '3':
       saldo_corrente, saldo_poupanca, extrato = transferir_poupanca(saldo_corrente, saldo_poupanca, extrato)  
    elif opcao == '4':
       exibir_extrato(extrato, saldo_corrente, saldo_poupanca)
    elif opcao == '5':
        break
    else:
        print("Opção Inválida")
