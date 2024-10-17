from datetime import date, datetime, time

print ("Informando uma data: ",date(2023,7,16))
print("Data e hora local: ", datetime.today())
print("INformando um horário",time(10,20,0))

#Podemos guardar em uma váriavel.
hora = time(11,20,5)
print(hora)
data = datetime.today()
print("Guardando valor da data em uma variável: ", data)