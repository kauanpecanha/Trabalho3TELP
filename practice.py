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