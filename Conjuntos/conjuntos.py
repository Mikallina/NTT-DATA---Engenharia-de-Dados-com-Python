numeros = {1,2,3,2,8}
numeros = list(numeros)
numeros[0]
print(numeros)

# Percorrer o conjunto
animais = {"cavalo", "cachorro", "galinha", "cachorro"}
for animal in animais:
    print(animal)

# Enumerate
for indice, animal in enumerate(animais):
    print(f"{indice}: {animal}")    

# Métodos

numero_1 = {1,2, 2, 4, 5, 8}
numero_2 = {3,4}
# {.union}
numeros_totais = numero_1.union(numero_2)
print("Union: ",  numeros_totais)

# intersection
intersection = numero_1.intersection(numero_2)
print(intersection)

# difference
num_1 = numero_1.difference(numero_2)
num_2 = numero_2.difference(numero_1)
print("Diferrence: ",num_1)
print("Diferrence: ",num_2)
print("Symmetric_differente: ",numero_1.symmetric_difference(numero_2))
print("issubset: ", numero_2.issubset(numero_1))
print("issuperset: ", numero_1.issuperset(numero_2))
print("isdisjoint: ", numero_1.isdisjoint(numero_2))
print("add: ", numero_1.add(25))
print("Discard: ", numero_1.discard(1))
print("Pop: ", numero_1.pop())
print("Remove: ", numero_1.remove(25))
print("Len: ", numero_1)
print("In: ", 1 in numero_1)

print(numero_1)






