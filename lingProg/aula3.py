# lista = []
# tupla = () - imutáveis


lista_fruta = ["laranja", "banana"]
tupla_frutas = ("laranja", "banana")

# conjuntos

A = {1, 2, 3, 4}
B = {4, 7, 8, 9}

print(A, B)

A.update(B) #correspondente a A u B

print(f"O conjunto A, após a incorporação do conjunto B é: {A}")

print(3 in A) # o comando in tem a função de se determinar um valor booleano, conforme o pertencimento de um elemento a um conjunto

# para criar um conjunto vazio, usa-se a função set()

conjunto_vazio = set() #um conjunto vazio é determinado como um dicionário

print(conjunto_vazio)

# dicionários {}

contato = {"id": 18, "nome":"Silvia", "telefone":"(21)99999-9999"}

print(contato["nome"]) #impressão do conteúdo da key "nome"

# obs.: pode conter chaves repetidas, referenciando a última definição da key como teste = {"nome":"Kauan", "nome":"Cláudia"}

teste = {"nome":"Kauan", "nome":"Cláudia"}

print(teste["nome"]) #impressão da definição Cláudia

# funções int, float, complex, str, bool

# crie um programa que solicite ao usuário 3 nomes de alunos e suas respectivas notas, e imprime a média do grupo usando uma lista para armazenar os nomes, e outra para as notas.

lista_nomes = []
lista_notas = []

for i in range(1, 4):
    nome = str(input(f"Entre com o nome do aluno {i}: "))
    lista_nomes.append(nome)

print(lista_nomes)

for i in range(1, 4):
    nota = float(input(f"Entre com a nota do aluno {i}: "))
    lista_notas.append(nota)

media = 0

for i in range (1, 4):
    media += lista_notas.pop(-1)

media = media/3

print(f"A média deste grupo é: {media:.2f}")


# dicionários

dic = {"nome": "Ana", "idade": 18, "cidade": "Rio de Janeiro", "cpf": 14611531740, "rg": 307406728}

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("nome"))

dic2 = {"nome_do_pai": "José", "nome_da_mae": "Maria"}

dic.update(dic2)

print(dic)