Fila = []

def addClient(f1):
    
    cleanScreen()
    
    cliente = {
    'nome': '',
    'rg': ''
    }

    nome = str(input("Entre com o nome do cliente: ")) 
    rg = str(input("Entre com o rg do cliente: "))
       
    cliente["nome"] = nome
    cliente['rg'] = rg


    f1.append(cliente)

def analysis(f1):
    
    cleanScreen()

    if(len(f1) == 0):
        print("A fila está vazia.\n\n")
    else:
        for i in range (0, len(f1)):
            print(f"{i+1} - {f1[i]['rg']} - {f1[i]['nome']}")

def answerClient(f1):
    
    cleanScreen()
    
    if(len(f1) == 0):
        print("Não há cliente para ser atendido no momento.\n\n")
    else:
        target = f1.pop(0)

        print(f"O cliente {target['nome']}, de RG {target['rg']} acabou de ser atendido.\n\n")

def cleanScreen():
    print("\n"*100)