from random import choice

lista = ['girafa']
# lista de palavras

palavra = choice(lista)
# escolhedor de palavras da lista

word = []
hidden = []
store = []
s = len(palavra)
contador = 0


for contador in range(s):
    word.append(palavra[contador])
    hidden.append("_")
    contador+=1

print(word)
print(hidden)


# medição do tamanho da palavra, necessário pro iterador while

erros = 0
# contador de erros do usuário



exists = False

print("Jogo da Forca!")
print("\n")
print("_ "*s)
print("\n")

while(erros<=6):
    
    letra = str(input("Entre com uma letra a seguir: "))
    s1 = len(letra)
    if(s1>1): # até aqui, tá correto
        print(" Entre com somente uma letra!")
        continue
    else:
        while(contador<s):
            if(palavra[contador] == letra):
                store.append(contador)
                print("Letra Encontrada")
                print(f"{contador}")

                contador+=1
            else:
                print(f"{contador}")
                print("Letra não encontrada")
                contador+=1
            
            print(f"Esta letra se encontra nas posições: {store}")

        
        # if(exists == False):
        #     erros+=1
        # else:

        contador = 0

    print(len(store))

    while(contador<len(store)):
        hidden[store[contador]] = letra
        contador+=1

    print(hidden)