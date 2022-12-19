# questao 1 - trabalho

from math import ceil
from math import floor

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
