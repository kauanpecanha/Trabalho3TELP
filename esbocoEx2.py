
class percurso(): # classe para definir objetos do tipo percurso, que terão atributos referentes aos tempos de cada volta feita pelo corredor em questão
    def __init__(self, tvolta1, tvolta2, tvolta3, tvolta4, tvolta5, tvolta6, tvolta7, tvolta8, tvolta9, tvolta10): # construtor que definirá esses atributos
        # definição dos atributos de tempo das voltas
        self.volta1 = tvolta1
        self.volta2 = tvolta2
        self.volta3 = tvolta3
        self.volta4 = tvolta4
        self.volta5 = tvolta5
        self.volta6 = tvolta6
        self.volta7 = tvolta7
        self.volta8 = tvolta8
        self.volta9 = tvolta9
        self.volta10 = tvolta10
    
    def printData(self):
        print(f" Primeira volta: {volta1} \n Segunda volta: {volta2} \n Terceira volta: {volta3} \n Quarta volta: {volta4} \n Quinta volta: {volta5} \n Sexta volta: {volta6} \n Sétima volta: {volta7} \n Oitava volta: {volta8} \n Nona volta: {volta9} \n Décima volta: {volta10}")

# variável para armazenar o nome dos corredores em questão
name1 = str(input(" Entre com o nome do primeiro corredor: "))
name2 = str(input(" Entre com o nome do segundo corredor: "))
name3 = str(input(" Entre com o nome do terceiro corredor: "))
name4 = str(input(" Entre com o nome do quarto corredor: "))
name5 = str(input(" Entre com o nome do quinto corredor: "))
name6 = str(input(" Entre com o nome do sexto corredor: "))

# variáveis para definir os tempos de cada volta
volta1 = 0
volta2 = 0
volta3 = 0
volta4 = 0
volta5 = 0
volta6 = 0
volta7 = 0
volta8 = 0
volta9 = 0
volta10 = 0

# variável que armazenará o dicionário de tempos(que armazenará seis objetos do tipo percurso, e estes, os tempos de cada uma das voltas)
storage = {name1: "", name2: "", name3: "", name4: "", name5: "", name6: ""}

for i in range(0, 6):
    
    volta1 = float(input("Entre com o tempo da primeira volta: "))
    volta2 = float(input("Entre com o tempo da segunda volta: "))
    volta3 = float(input("Entre com o tempo da terceira volta: "))
    volta4 = float(input("Entre com o tempo da quarta volta: "))
    volta5 = float(input("Entre com o tempo da quinta volta: "))
    volta6 = float(input("Entre com o tempo da sexta volta: "))
    volta7 = float(input("Entre com o tempo da sétima volta: "))
    volta8 = float(input("Entre com o tempo da oitava volta: "))
    volta9 = float(input("Entre com o tempo da nona volta: "))
    volta10 = float(input("Entre com o tempo da décima volta: "))

    storage[i] = percurso(volta1, volta2, volta3, volta4, volta5, volta6, volta7, volta8, volta9, volta10)

    (storage[i]).printData()
    print("\n\n")