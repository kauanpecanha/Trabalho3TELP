import unidecode #installed via pip install unidecode - responsible for substitute special caracters(ex.: á, ô, etc) for thenselves in normal version, in order to do the verification the right way ('cause á != a)

frase = str(input("Entre com uma frase: "))

contador = 1
frase = frase.lower()
frase = frase.replace(" ", '')
frase = unidecode.unidecode(frase)
limit = len(frase)

print(frase)
print(f"Tamanho: {limit}")

most = frase.count(f'{frase[0]}')
letra = frase[0]


while(contador<limit):
    if((frase.count(f'{frase[contador]}'))>most):
        most = frase.count(f'{frase[contador]}')
        letra = frase[contador]
    
    contador+=1

print(f"A letra que mais apareceu foi: {letra}, {most} vezes! ")