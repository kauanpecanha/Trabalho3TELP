# início do código

alunos = []
notas = []

codigo = 1

while(codigo != 0):
    nome = str(input("Entre com o nome do aluno: "))
    nota = float(input("Entre com a nota do aluno: "))

    alunos.append(nome)
    notas.append(nota)

    codigo = int(input("Entre com o código(1 para continuar, 0 para parar): "))

    if(codigo != 1 and codigo!=0):
        while(codigo != 1 or codigo!=0):

            print("Código inválido. Entre com 1 ou 0: ")
        
            codigo = int(input("Entre com o código(1 para continuar, 0 para parar): "))


if(len(alunos) == len(notas)):
    for i in range(len(alunos)):
        print(f"Nome: {alunos[i]} \t\t Nota: {notas[i]}")
elif(len(alunos)<len(notas)):
    print("\n Alunos insuficientes")
else:
    print("\n Notas insuficientes")