def limpar():
    print("\n"*100)

fila = []

qtd = 0

while(True):
    opcao = ''

    limpar()

    print("\nMENU DO SISTEMA")
    print("1 - Incluir cliente na fila")
    print("2 - Listar pessoas na fila")
    print("3 - Atender o próximo cliente")
    print("4 - Sair do programa")

    opcao = int(input("Opção desejada: "))

    if(opcao == 1):
        qtd = qtd + 1

        limpar()

        nome = str(input("Digite o nome do cliente: "))

        rg = str(input("Entre com o RG do cliente: "))

        cliente = {
            'nome': nome,
            'rg': rg
        }

        fila.append(cliente)

    elif(opcao == 2):
        if(len(fila) > 0):
            for i in range(0, len(fila)):
                print(f"{i+1} - {fila[i]['rg']} - {fila[i]['nome']}")
            
            input("Tecle <ENTER> para retornar ao menu.")
        else:
            print("Fila vazia!")

            input("Tecle <ENTER> para retornar ao menu.")
    
    elif(opcao == 3):

        if(len(fila) > 0):

            limpar()

            cliente = fila.pop(0)

            print(f"Atendendo ao cliente: {cliente['nome']} - RG: {cliente['rg']}")

            print(f"Restam {len(fila)} clientes na fila.")

            input("Entre com a tecla <ENTER> para retornar ao menu principal.")
        
        else:
            print("Fila vazia!")

            input("Entre com a tecla <ENTER> para retornar ao menu principal.")
    
    elif(opcao == 4):

        print("Programa finalizado pelo usuário.")
        break