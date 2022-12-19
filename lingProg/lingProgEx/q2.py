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