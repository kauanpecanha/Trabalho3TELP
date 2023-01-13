# Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, em que a chave é o nome do corredor. Ao final, diga de quem foi a melhor volta da prova, em que volta e mostre o nome e os tempos do campeão, que é o que tem a menor média de tempos.

# dizer de quem foi a melhor volta (check)
# em que volta foi o melhor tempo (check)
# mostrar o nome e os tempos do campeão

runner1 = 'KAUAN'
runner2 = 'JOÃO'
runner3 = 'MARIA'
runner4 = 'JONATHAN'
runner5 = 'MARTHA'
runner6 = 'ISABELLA'

tempo1 = []
media1 = 0
melhor1 = 0
melhorVolta1 = 0

tempo2 = []
media2 = 0
melhor2 = 0
melhorVolta2 = 0

tempo3 = []
media3 = 0
melhor3 = 0
melhorVolta3 = 0

tempo4 = []
media4 = 0
melhor4 = 0
melhorVolta4 = 0

tempo5 = []
media5 = 0
melhor5 = 0
melhorVolta5 = 0

tempo6 = []
media6 = 0
melhor6 = 0
melhorVolta6 = 0

storage = {}
medias = []

time = 0

melhorCorredor = ''
melhorTempo = 0
melhorVolta = 0


# corredor 1

for i in range(0, 10):
    print(f"\n Corredor: {runner1}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo1.append(time)

    if(i == 0):
        melhor1 = time
        melhorVolta1 = i+1
    else:
        if(time<melhor1):
            melhor1 = time
            melhorVolta1 = i+1
    
    media1 += time

media1 = media1/10
melhorCorredor = runner1
melhorTempo = melhor1
melhorVolta = melhorVolta1

# corredor 2

for i in range(0, 10):
    print(f"\n Corredor: {runner2}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo2.append(time)

    if(i == 0):
        melhor2 = time
        melhorVolta2 = i+1
    else:
        if(time<melhor2):
            melhor2 = time
            melhorVolta2 = i+1
    
    media2 += time

media2 = media2/10

if(melhor2<melhorTempo):
    melhorCorredor = runner2
    melhorTempo = melhor2
    melhorVolta = melhorVolta2

# corredor 3

for i in range(0, 10):
    print(f"\n Corredor: {runner3}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo3.append(time)

    if(i == 0):
        melhor3 = time
        melhorVolta3 = i+1
    else:
        if(time<melhor3):
            melhor3 = time
            melhorVolta3 = i+1
    
    media3 += time

media3 = media3/10

if(melhor3<melhorTempo):
    melhorCorredor = runner3
    melhorTempo = melhor3
    melhorVolta = melhorVolta3

# corredor 4

for i in range(0, 10):
    print(f"\n Corredor: {runner4}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo4.append(time)

    if(i == 0):
        melhor4 = time
        melhorVolta4 = i+1
    else:
        if(time<melhor4):
            melhor4 = time
            melhorVolta4 = i+1
    
    media4 += time

media4 = media4/10

if(melhor4<melhorTempo):
    melhorCorredor = runner4
    melhorTempo = melhor4
    melhorVolta = melhorVolta4


# corredor 5

for i in range(0, 10):
    print(f"\n Corredor: {runner5}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo5.append(time)

    if(i == 0):
        melhor5 = time
        melhorVolta5 = i+1
    else:
        if(time<melhor5):
            melhor5 = time
            melhorVolta5 = i+1
    
    media5 += time

media5 = media5/10

if(melhor5<melhorTempo):
    melhorCorredor = runner5
    melhorTempo = melhor5
    melhorVolta = melhorVolta5


# corredor 6

for i in range(0, 10):
    print(f"\n Corredor: {runner6}")
    time = float(input(f"\n\n Entre com o tempo da volta {i+1}, em segundos: "))
    tempo6.append(time)

    if(i == 0):
        melhor6 = time
        melhorVolta6 = i+1
    else:
        if(time<melhor6):
            melhor6 = time
            melhorVolta6 = i+1
    
    media6 += time

media6 = media6/10

if(melhor6<melhorTempo):
    melhorCorredor = runner6
    melhorTempo = melhor6
    melhorVolta = melhorVolta6


storage[runner1] = tempo1
storage[runner2] = tempo2
storage[runner3] = tempo3
storage[runner4] = tempo4
storage[runner5] = tempo5
storage[runner6] = tempo6


print(f"\n\n O melhor corredor foi {melhorCorredor} e seu melhor tempo foi {melhorTempo}s na volta {melhorVolta}")
print(f"\n\n\n CAMPEÃO: {melhorCorredor}")
print(f"\n TEMPOS: {storage[melhorCorredor]}")

# exercício 3 finalizado com sucesso