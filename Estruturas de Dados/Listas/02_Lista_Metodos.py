# Adicionando Objeto
lista = []
lista.append(1)
lista.append("Objeto Qualquer")
lista.append([1,2,3,4])
print(lista)

# Limpando a lista
lista.clear

#Copy Para não modificar

lista = [1,2,5,8,8,9,8,7,9]
lista_2 = lista.copy()
print(lista, lista_2)
lista_2[0] = 3
print(lista, lista_2)

#contador Conta quantas ocorrencias tem
print(lista.count(8))

#Extend Inclui o que precisa
lista.extend([25,10,30])
print(lista)

#Index qual a primeira ocorrencia.
print(lista.index(1))

#Pop Conceito de Pilha - Exclui o ultimo da lista ou passa o índice
lista.pop(1)
print(lista)

#Remove
lista.remove(30)
print(lista)

#Reverse
lista.reverse()
print(lista)

#Sort Ordena a lista
lista.sort()
print(lista)
#Lista reversa com o sort
lista.sort(reverse=True)
print(lista)

#Ordem Decrescente
linguagens = ["Python","Java", "Go", "Csharp","Js"]
linguagens.sort(reverse=True)
print(linguagens)

#Ordem por quantidade de caracteres
print("Ordem por quantidade de caracteres")
linguagens.sort(key=lambda x: len(x))
print(linguagens)


print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0])
