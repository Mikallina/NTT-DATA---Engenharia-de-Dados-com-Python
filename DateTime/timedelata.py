from datetime import date, datetime, timedelta

print("Outro exemplo",date.today() - timedelta(days=1))      
resultado = datetime(2024,10,7,10,57,0) - timedelta(hours=2)
print("two hours before: ", resultado)



#Formatar data
data_hora_atual = datetime.now()
data_hora_str = "2024-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %H"
mascara_en= "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

#Data Convertida pra DateTime
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(type(data_convertida))
