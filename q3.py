from random import choice

# Questão 3

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