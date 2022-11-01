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