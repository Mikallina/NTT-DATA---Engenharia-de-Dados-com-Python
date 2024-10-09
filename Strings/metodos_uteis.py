#Métodos Úteis da Classe String
curso = "   Python  "
print("Tira todos os espaços: ", curso.strip())
print("Tira espaços a esquerda: ",curso.lstrip())
print("Tira espaços a direita: ",curso.rstrip())

curso = "pYthon"
print("Maiusculo: ", curso.upper())
print("Minusculo: ",curso.lower())
print("Primeira Maiscula: ",curso.title())

curso = "Python"
print("Incluí ## na quantidade exigida (10): ", curso.center(10, "#"))
print(".".join(curso))


#Interpolação de Variáveis

# Com % ( não mais recomendado)
nome = "Michelle"
idade = 40
profissao = "Programadora"
linguagem ="Python"
#%s Para String %d para inteiros
print("Olá, me chamo %s. Tenho %d de idade, trabalho como %s e estou matriculada no curso de %s" % (nome, idade, profissao, linguagem))

#Com método format
print("Olá, me chamo {}. Tenho {} de idade, trabalho como {} e estou matriculada no curso de {}".format(nome, idade, profissao, linguagem))

#Passando como argumento
print("Olá, me chamo {nome}. Tenho {idade} de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}".format(nome = nome, idade=idade, profissao=profissao,linguagem = linguagem))

dados = {"nome": "Michelle", "idade": 40}

#Passando como Dicionário
print("Olá, me chamo {nome}. Tenho {idade} de idade".format(**dados))

#Fatiamento de Strings
nome =  "Michelle do Carmo Borges"
print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[::-1])

#String Triplas
nome = "Michelle"
mensagem = f"""
Olá meu nome é {nome}, 
Eu estou aprendendo Python
   Essa mensagem tem diferentes recuos
"""

print(mensagem)

print("""
      =================MENU===================

        1 - Depositar
        2 - Sacar
        3 - Sair
      ========================================
      
      """)