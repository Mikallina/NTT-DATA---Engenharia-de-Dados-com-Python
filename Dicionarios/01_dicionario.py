
#Formas de Dicionário
pessoa = {"nome" : "Michelle", "idade": 40}
pessoa =  dict(nome = "Michelle", idade = 40)
#Adicionado nova chave
pessoa ["telefone"] = "9999-9999"

#Acessando os valores
print(pessoa["nome"])

#Dicionario Alinhados
contatos = {
    "email@email.com": {"nome": "michelle", "telefone": "99999-9999"},
    "email01@email.com": {"nome": "Daniela", "telefone": "1111-11111"},
    "email02@email.com": {"nome": "Vera", "telefone": "2222-2222"},
    "email03@email.com": {"nome": "Odair", "telefone": "99223-2354", "endereco": "Avenida X"},
}

print(contatos["email01@email.com"]["nome"])
print(contatos["email01@email.com"])
print(contatos["email03@email.com"]["endereco"])
telefone = contatos["email02@email.com"]
print(telefone)

for chave, valor in contatos.items():
    print(chave,valor)