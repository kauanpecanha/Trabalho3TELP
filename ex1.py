#Crie um programa para gerenciar uma pilha de processos em Python. Cada processo possui um identificador (número) e uma descrição (string). Você deverá pedir ao usuário para escolher se deseja encerrar, incluir ou retirar um processo da pilha. Se a operação for uma inclusão, colocar o processo na pilha e imprimir o novo estado dessa; se for uma exclusão, caso a pilha não esteja vazia, imprimir “removido o processo #identificador — descrição da pilha” e mostrar o conteúdo atual dela; se a pilha estiver vazia, mostrar “pilha vazia”. Se o usuário escolher encerrar, esvazie a pilha (caso ainda existam elementos nela) e encerre o programa.

class processo(): # classe para os objetos do tipo processo
    def __init__(self, idd, desc): # construtor para setar suas informações
        self.idd = idd # atribuidor de identificador, do tipo int
        self.desc = desc # atribuidor de descrição do tipo string


option = 0 # variável para armazenar a opção escolhida pelo usuário
identity = 0 # variável para armazenar o identificador do objeto em questão
description = "" # variável para armazenar a descrição do objeto em questão
processes = [] # lista que armazenará os processor
ide = 0 # variávle para armazenar a identidade do objeto que será deletado
target = 0

while(True): # ciclo infinito que somente é encerrado quando uma das condições retorna a instrução break
    
    print("\n\nEntre com uma opção a seguir:")
    print(" 1 - Adicionar processo\n 2 - Excluir Processo\n 3 - Encerrar aplicação")
    option = int(input("Opção escolhida: "))

    if(option == 1):
        identity = int(input("Entre com o identificador: "))
        description = str(input("Entre com a descrição do processo: "))

        processes.append(processo(identity, description))

        print(f"Processos armazenados: {len(processes)}")
    
    if(option == 2):
        ide = int(input(" Entre com o identificador do processo que você deseja deletar.\n Identificador: "))

        if((len(processes)) == 0):
            print("\nLista vazia!")
        else:
            for i in range(len(processes)):
                if(((processes[i]).idd) == ide):
                    print("\nProcesso encontrado!")

                    processes.pop(i)

                    print("\n\nProcesso deletado com sucesso!")
                else:
                    print("\nProcesso não encontrado!")

    if(option == 3):
        break;