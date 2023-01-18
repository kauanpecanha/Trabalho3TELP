# Crie um programa que controlará a fila de atendimentos em uma recepção. O usuário deverá escolher entre:
# Consultar a fila atual: Mostra quem está na fila no momento, por ordem de chegada.
# Incluir alguém na fila: Coloca o nome e RG de um cliente na fila.
# Atender ao próximo cliente: Quando selecionada esta opção, o primeiro cliente da fila será retirado desta e será mostrada a mensagem “Atendendo ao cliente nome do cliente — RG: RG do cliente”. Se a fila estiver vazia, exibir “Nenhum cliente a atender”.


# Você lembra do Exercício resolvido 2 do Capítulo 7, no qual demonstrei como criar uma fila usando a classe List? Refaça o exercício, desta vez criando funções para limpar a tela, verificar se a fila está vazia, incluir um cliente na fila e atender a um cliente. Deixe o loop principal do programa em um arquivo separado das funções que controlam a fila. Salve as funções da fila em um módulo chamado fila.py. Esse módulo implementa um TAD (Tipo Abstrato de Dados) fila.

import fila

f1 = fila.Fila

nome = ''
rg = ''
opcao = 0

while(True):
    print("Entre com uma opção:")
    print("1 - Incluir cliente na fila")
    print("2 - Listar pessoas na fila")
    print("3 - Atender o próximo cliente")
    print("4 - Finalizar programa")
    opcao = int(input("Opção escolhida: "))

    if(opcao == 1):
       fila.addClient(f1)
    
    if(opcao == 2):
        fila.analysis(f1)

    if(opcao == 3):
        fila.answerClient(f1)

    if(opcao == 4):
        break


# ex5 finalizado com sucesso