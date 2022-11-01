#funções

def funcao_sem_parametros(): # função sem parâmetros
    print("Hello, word")

funcao_sem_parametros() #output da função sem parâmetros

def funcao_com_parametro(name): # função com parâmetros
    print("hello, " + name)


funcao_com_parametro("kauan") #output da função com parâmetros

def soma(x, y): # funcao que utiliza inteiros, e os soma
    print(f"A soma entre {x} e {y} eh {x+y}")

soma(18, 12)

def multiplicacao(x):
    return 5 * x

multiplicacao(10)

def situacao_aluno(name, nota):
    print(f"O aluno {name} tirou nota {nota} no trabalho de programação")

situacao_aluno("kauan", 18)

x = int(input("Entre com um numero: "))
y = int(input("Entre com um numero: "))

soma(x, y)
funcao_com_parametro("kauan") #passagem de uma string como parametro p funcao

nome = str(input("Entre com o nome do aluno em questão: "))
nota = float(input("Entre com a nota do trabalho de programação: "))

situacao_aluno(nome, nota)

# -------------------------------------------------------------------------

# manipulação de strigs

# capitalize() -> Coloca a 1ª letra Maiúscula;
# casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente);
# count() -> Conta a quantidade de vezes que um valor/símbolo/letra aparece na string;
# find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado (lá no início falamos que cada letra/símbolo tem uma posição no texto);
# format() -> Formata uma string de acordo com os valores passados;
# isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função;
# isalpha() -> Verifica se um texto é todo feito de letras;
# isnumeric() -> Verifica se um texto é todo feito por números;
# replace() -> Substitui um texto por um outro texto em uma string;
# split() -> Separa uma string de acordo com um delimitador em vários textos diferentes;
# splitlines() -> separa um texto em vários textos de acordo com os “enters” do texto;
# startswith() -> Verifica se a string começa com determinado texto;
# strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços “extras” no início e no final;
# title() -> Coloca a 1ª letra de cada palavra em maiúscula;
# upper() -> Coloca o texto todo em letra maiúscula.

nome = "kauan kauan peçanha peçanha lira lira"
NOME = "KAUAN PEÇANHA LIRA"

print(nome.capitalize())
print(NOME.casefold())
print(nome.count("kauan"))
print(nome.find("peçanha"))
print(nome.replace("peçanha", "silva"))
print(nome.split())
print(nome.startswith("kauan"))
print(nome.title())
print(nome.upper())