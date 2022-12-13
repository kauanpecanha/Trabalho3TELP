palavra = "girafa"
word = []
hidden = []
store = []
s = len(palavra)
contador = 0
erros = 0
exists = False
boolLetra = False

# print(palavra[contador])

while(contador<s):
    word.append(palavra[contador])
    hidden.append("_")
    # print(hidden)
    # print(word)
    contador+=1

while(boolLetra):
    letra = str(input("Entre com uma letra: "))
    if(len(letra)>1):
        print("Entre com somente uma letra!")
        boolLetra = False
    else:
        boolLetra = True

contador = 0

while(contador<s):
    if(palavra[contador] == letra):
        store.append(contador)
        print(f"{contador}")

        contador+=1
    else:
        print(f"{contador}")
        contador+=1


print(f"Esta letra se encontra nas posições: {store}")

contador = 0

print(len(store))

while(contador<len(store)):
    hidden[store[contador]] = letra
    contador+=1

print(hidden)