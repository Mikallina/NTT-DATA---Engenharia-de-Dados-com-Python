import random

menu_principal = """


[1] Criar Usuário
[2] Acessar Conta
[3] Sair

=> """

menu_conta = """


[1] Depositar
[2] Sacar
[3] Transferir para poupança
[4] Extrato
[5] Sair

=> """

usuarios = {}
contas = {}

def gerar_numero_conta():
    return random.randint(10000, 99999)

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    if cpf not in usuarios:
        usuarios[cpf] = nome
        numero_conta = gerar_numero_conta()
        criar_conta_corrente(cpf, numero_conta) 
        print(f"Usuário {nome} criado com sucesso e conta corrente #{numero_conta} vinculada!")
    else:
        print("Usuário já existe.")

def criar_conta_corrente(cpf, numero_conta):
    contas[numero_conta] = {
        'cpf': cpf,
        'saldo_corrente': 0,
        'saldo_poupanca': 0,
        'limite': 500,
        'extrato': "",
        'numero_saques': 0
    }

def depositar(numero_conta, valor):
    contas[numero_conta]['saldo_corrente'] += valor
    contas[numero_conta]['extrato'] += f"                               {valor:.2f}\n"

def sacar(numero_conta, valor):
    conta = contas[numero_conta]
    saldo_corrente = conta['saldo_corrente']
    limite = conta['limite']
    numero_saques = conta['numero_saques']

    excedeu_saldo = valor > saldo_corrente
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= 3

    if excedeu_saldo:
        print("Operação Inválida. Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação Inválida. O valor de saque excede o limite.")
    elif excedeu_saques:
        print("Operação Inválida. Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo_corrente'] -= valor
        conta['extrato'] += f"     -{valor:.2f}\n"
        conta['numero_saques'] += 1
    else:
        print("Operação Inválida. O valor informado é inválido.")

def transferir_poupanca(numero_conta, valor):
    conta = contas[numero_conta]
    saldo_corrente = conta['saldo_corrente']
    if 0 < valor <= saldo_corrente:
        conta['saldo_corrente'] -= valor
        conta['saldo_poupanca'] += valor
        conta['extrato'] += f"     -{valor:.2f} (Transferido para poupança)\n"
    elif valor > saldo_corrente:
        print("Valor maior que o saldo da conta corrente.")
    else:
        print("Operação Inválida. O valor deve ser positivo.")

def exibir_extrato(numero_conta):
    conta = contas[numero_conta]
    extrato = conta['extrato']
    saldo_corrente = conta['saldo_corrente']
    saldo_poupanca = conta['saldo_poupanca']
    
    print(" **************** Extrato *****************")
    print("Conta Corrente: ", numero_conta)
    print("      Débito                  Crédito      ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo Corrente: R$ {saldo_corrente:.2f}\nSaldo Poupança: R$ {saldo_poupanca:.2f}")
    print("*******************************************")

while True:
    opcao_principal = input(menu_principal).strip()
    
    if opcao_principal == '1':
        criar_usuario()
    elif opcao_principal == '2':
        numero_conta = int(input("Digite o número da conta (5 dígitos): "))
        if numero_conta in contas:
            while True:
                opcao_conta = input(menu_conta).strip()
                
                if opcao_conta == '1':
                    valor = float(input("Digite o valor do depósito: "))
                    depositar(numero_conta, valor)
                elif opcao_conta == '2':
                    valor = float(input("Digite o valor do saque: "))
                    sacar(numero_conta, valor)
                elif opcao_conta == '3':
                    valor = float(input("Digite o valor para depósito na poupança: "))
                    transferir_poupanca(numero_conta, valor)
                elif opcao_conta == '4':
                    exibir_extrato(numero_conta)
                elif opcao_conta == '5':
                    break
                else:
                    print("Opção Inválida")
        else:
            print("Conta não encontrada.")
    elif opcao_principal == '3':
        break
    else:
        print("Opção Inválida")
