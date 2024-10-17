contatos = {
    "email@email.com": {"nome": "michelle", "telefone": "99999-9999"},
    "email01@email.com": {"nome": "Daniela", "telefone": "1111-11111"},
    "email02@email.com": {"nome": "Vera", "telefone": "2222-2222"},
    "email03@email.com": {"nome": "Odair", "telefone": "99223-2354", "endereco": "Avenida X"},
}

#contatos.clear()
#contatos.copy()

copia = contatos.copy()
copia["email@email.com"] = {"nome" : "Michelle"}
#print(copia)
#print(contatos)

#Fromkyes
contatos.fromkeys(["endereco", "cep"])
contatos.fromkeys(["cpf"], "vazio")

print(contatos)
#contatos["chave"]
contatos.get("chave",{})
print(contatos.get("email@email.com",{}))

print(contatos.keys())


resultado = contatos.pop("email02@email.com.br","Removido")
print(resultado)

resultado = contatos.pop("email02@email.com.br","Não removido")

carro ={"marca"}

#Alguns metodos
#setdefault
#update
#values
#in
