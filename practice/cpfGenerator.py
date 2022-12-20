# gerador de cpf

print("\n\nBEM VINDO AO GERADOR DE CPFs da Caixa Econômica Federal!!\n\n")

from random import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nomes_primeiros = ["Kauan", "Isabella", "Emanuela", "Cláudia", "Flávio"]
sobrenomes = ['Silva', 'Oliveira', 'Bastos', 'Alves']

cpf = []
contador = 0
cont = 0
nome = (choice((nomes_primeiros))) + (choice(sobrenomes))

for i in range(0, 11):
    cpf.append(choice(numbers))
    contador+=1
    if((contador%3) == 0):
        if(cont<2):
            cpf.append(".")
            cont+=1
        else:
            cpf.append("-")

contador = 1
cont = 1
tam = len(cpf)

print("CPF gerado: ")
print(*cpf)
print("\nBem vindo ao mundo, ")
print(*nome)