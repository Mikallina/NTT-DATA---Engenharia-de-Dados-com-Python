from datetime import timedelta, datetime,date


tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

menu = """
Digite o tamanho do seu carro: 
    [p] Carro Pequeno
    [m] Carro Médio
    [g] Carro grande
    [s] Sair

====> """

while True:
    opcao = input(menu).strip() 
    print(f"Você digitou: '{opcao}'")
        
    if opcao =='p':
       data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
       print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    elif opcao == "m":
       data_estimada = data_atual + timedelta(minutes=tempo_medio)
       print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    elif opcao == "g":
       data_estimada = data_atual + timedelta(minutes=tempo_grande)
       print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
    elif opcao == 's':
       print("Volte sempre")
       break
    print("Outro exemplo",date.today() - timedelta(days=1))       



