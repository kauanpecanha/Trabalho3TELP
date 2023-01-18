# Faça um programa que solicita ao usuário sua data de nascimento e, em seguida, em um loop, pede as datas de admissão e demissão de todos os empregos ocupados por ele. Em seguida, calcula quantos dias o usuário já trabalhou desde o início da sua carreira.

from datetime import datetime

option = 0
job = ""
enterprise = ""

summ = 0

day0 = 0
month0 = 0
year0 = 0

day1 = 0
month1 = 0
year1 = 0

bornDay = int(input(" Entre com o seu dia de nascimento: "))
bornMonth = int(input(" Entre com o seu mês de nascimento: "))
bornYear = int(input(" Entre com o seu ano de nascimento: "))

while(True):
    print(" Entre com a ação que você deseja executar.\n 1 - Adicionar emprego\n 2 - Finaliar Programa")
    option = int(input("Opção: "))

    if(option == 1):
        job = str(input("Entre com o cargo em que você trabalhou(ex.: Assessor do Setor Comercial): "))
        enterprise = str(input("Entre com a empresa/organização em que você trabalhou(ex.: Serra Jr. Engenharia): "))

        day0 = int(input(" Entre com o dia de ingresso: "))
        month0 = int(input(" Entre com o mês de ingresso: "))
        year0 = int(input(" Entre com o ano de ingresso: "))

        date0 = datetime(year0, month0, day0)

        day1 = int(input(" Entre com o dia de egresso: "))
        month1 = int(input(" Entre com o mês de egresso: "))
        year1 = int(input(" Entre com o ano de egresso: "))

        date1 = datetime(year1, month1, day1)

        parcialSumm = date1 - date0

        summ = summ + parcialSumm.days

        # print(type(parcialSumm))

        print(f" Você trabalhou durante {parcialSumm} como {job} na {enterprise}")
    
    if(option == 2):
        break

print(f"\n\nVocê trabalhou durante um total de: {summ} dias durante toda a sua carreira!")

# exercício 3 finalizado com sucesso