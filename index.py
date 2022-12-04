# Trabalho de Kauan Peçanha - Matrícula: 202110048911

from math import ceil
from math import floor

# questao 1 - trabalho

numeros = []
media = 0.0

for i in range(0, 3):
    numeros.append(int(input("Entre com o número: ")))

    media += numeros[i]

print(f"A média aritmética entre estes termos é: {media/(len(numeros))}")

if((len(numeros)/2)%2 == 0):
    indice_maior = ceil(len(numeros)/2)
    indice_menor = floor(len(numeros)/2)

    mediana_par = ((numeros[indice_menor]) + (numeros[indice_maior]))/2

    print(f"A mediana desta sequência é: {mediana_par}")
else:
    indice = ceil(len(numeros)/2)
    print(f"{indice}")
    mediana_normal = numeros[indice-1]

    print(f"A mediana desta sequência é: {mediana_normal}")

# exercício 2

pares = 0.0
impares = 0.0

for i in range(1000, 10000+1):
    if(((i % 2)==0)):
        if(((i%3)==0) and ((i%4)==0)):
            pares = pares + 1
    elif(((i % 2)!=0)):
        if(((i%3)==0) and ((i%4)==0)):
            impares = impares + 1
    else:
        continue

print(f"A quantidade de pares e ímpares divisíveis por 3 e 4 são, respectivamente: {pares} e {impares}")

# exercício 3

from random import choice

codigo = False

while(codigo != True):
    usuario = int(input("Entre com um número entre 1 e 100: "))

    if(usuario>100 or usuario<1):
        print("Número Inválido. Tente novamente.")
    else:
        codigo = True

sequencia = []

for i in range(1, 100 + 1):
    sequencia.append(i)

computador = choice(sequencia)
print(computador)

print(f"Usuário: {usuario} | Computador: {computador}")

if(usuario == computador):
    print("Você venceu!")
else:
    print("A banca sempre ganha!")


# exercício 4

nome1 = str(input("Entre com o nome do jogador 1: "))
nome2 = str(input("Entre com o nome do jogador 2: "))

sequencia = [1, 2, 3, 4, 5, 6]

n1 = choice(sequencia)
n2 = choice(sequencia)

if(n1>n2):
    print("O jogador 1 venceu!")
    print(f"Placar: Jogador 1: {n1} | Jogador 2: {n2}")
elif(n1<n2):
    print("O jogador 2 venceu!")
    print(f"Placar: Jogador 1: {n1} | Jogador 2: {n2}")
else:
    print("Houve um empate!")
    print(f"Placar: Jogador 1: {n1} | Jogador 2: {n2}")