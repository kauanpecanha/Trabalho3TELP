from random import choice

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