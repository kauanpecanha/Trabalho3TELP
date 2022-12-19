while(True):
    option = int(input("Entre com o número da opção, a seguir: "))

    if(option<1 or option>4):
        print("Opção inválida! Por favor entre com um número entre 1 e 4. ")
        continue

    if(option == 1):
        nome = []
        idade = 0
        salario = 0.0
        sexo = ['']
        estadoCivil = ['']

        nome = (str(input("Entre com seu nome a seguir: ")))
        idade = int(input("Entre com sua idade: "))
        salario = float(input("Entre com seu salário: "))
        sexo = str(input("Entre com seu sexo( m, f ): ")).lower()
        estadoCivil = str(input("Entre com seu Esatdo Civil( s, c, v, d ): ")).lower()

        check = True #variável para checkar a procedência das informações na opção 1

        
        if(len(nome)<=3):
            check = False
            print("1")
        elif(idade<=0 or idade>=130):
            check = False
            print("2")
        elif(salario<=0):
            check = False
            print("3")
        elif((sexo in ['m', 'f']) == False):
            print(sexo in ['m', 'f'])
            check = False
            print("4")
        elif((estadoCivil in ['s', 'c', 'd', 'v'])==False):
            check = False
            print("5")
        else:
            check = True
        
        if(check == True):
            print("Informações Corretamente colocadas. ")
            print("Informações:")
            print(f"\nNome: {nome} \nIdade: {idade} \nSalário:{salario:.2f} \nSexo{sexo} \nEstado Civil: {estadoCivil}")
        else:
            print("Alguma informação não foi corretamente colocada. ")
    
    if(option == 2): #ok
        str1 = str(input("Entre com a primeira string: "))
        str2 = str(input("Entre com a segunda string: "))

        print(f"Conteúdo da primeira string: {str1}\nConteúdo da segunda string: {str2}")
        print(f"Comprimenro da primeira string: {len(str1)}\nConteúdo da segunda string: {str2}")

        if((len(str1)) == (len(str2))):
            print("São iguais em comprimento!")
        else:
            print("Não tem o mesmo comprimento!")

        if(str1 == str2):
            print("São iguais em conteúdo!")
        else:
            print("Não são iguais em conteúdo!")
    
    if(option == 3): #ok
        nome = str(input("Entre com um nome: ")).upper()
        changed = nome[::-1]
        print(changed)
    
    if(option == 4): #ok
        seq = str(input("Entre com uma cadeia de caracteres: "))
        test = seq[::-1]

        if(seq == test):
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo!")