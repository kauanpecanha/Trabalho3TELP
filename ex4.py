#Considere que um homem possa se aposentar aos 65 anos de idade e 35 de contribuição à previdência, e uma mulher, 62/30. Elabore um programa que solicite os dados do gênero do(a) usuário(a), sua data de nascimento, as datas de início e fim de cada emprego ocupado, e informe quanto tempo falta para essa pessoa se aposentar.

from datetime import date, datetime

gender = ''
option = 0

job = ''
enterprise = ''

parcialSumm = 0
summ = 0

work = 0

while(True):
    print("\n\nEntre com seu gênero: masculino ou feminino.")
    gender = (str(input("Gênero: "))).lower()

    if(gender != 'masculino'):
        if(gender != 'feminino'):
            print(" Você entrou com um gênero inválido. Por favor, opte por ou masculino ou feminino.")
            continue

    dayBorn = int(input("Entre com seu dia de nascimento: "))
    monthBorn = int(input("Entre com seu mês de nascimento: "))
    yearBorn = int(input("Entre com seu ano de nascimento: "))

    born = (date(year=yearBorn, month=monthBorn, day=dayBorn))

    today = (date.today())

    age = (today.year - born.year)

    print(f"Age: {age}")

    while(True):
        print("Ações:\n 1 - Adicionar emprego\n 2 - Encerrar adições")

        option = int(input("\n\n Entre com a opção desejada a seguir: "))

        if(option == 1):
            job = str(input(" Entre com o cargo que você ocupou(Exemplo: Assessor do Setor Comercial): "))
            enterprise = str(input(" Entre com o cargo que você ocupou(Exemplo: Serra Jr. Engenharia): "))

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

            print(f" Você trabalhou durante {parcialSumm} como {job} na {enterprise}")

        elif(option == 2):
            break

        else:
            print(" Opção inválida. Escolha entre 1 e 2, somente.")
    
    print(f" Você trabalhou um total de {summ} dias durante sua carreira. ")

    if(gender == 'masculino'):
        if(age>=65):
            if(summ>=(30*365)):
                print("\n Você já pode se aposentar!")
            else:
                print(f"\n Ainda faltam {(30*365)-(summ)} dias para você se aposentar!")
        else:
            print("\n Você ainda não atingiu a idade mínima de 65 anos para se aposentar!")
    if(gender == 'feminino'):
        if(age>=62):
            if(summ>=(35*365)):
                print("\n Você já pode se aposentar!")
            else:
                print(f"\n Ainda faltam {(35*365)-(summ)} dias para você se aposentar!")
        else:
            print("\n Você ainda não atingiu a idade mínima de 65 anos para se aposentar!")
        
    break