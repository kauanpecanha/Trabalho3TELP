class pessoa:

    def __init__(self, nome, idade): # construtor
        self.nome = nome
        self.idade = idade
    
    def falar(self, frase): # método que permite o pessoa falar uma frase
        print("\n")
        print(str(self.nome) + " está dizendo: " + frase)
    
    def __str__(self): # método que permite transformar as informações sobre o objeto, em string
        print("Me chamo " + str(self.nome) + ", e tenho " + str(self.idade) + " anos!")
        print("\n")

p1 = pessoa("João", 18) #o objeto p1 é do tipo pessoa, e assume os atributos nome como João, e idade, como 18
p2 = pessoa("Maria", 19) #o objeto p2 é do tipo pessoa, e assume os atributos nome como Maria, e idade, como 19

p1.falar("Olá, Maria!") #chamada da função de fala, referente ao João, dizendo Olá para Maria
p1.__str__() #chamada da função para imprimir as informações acerca de João

p2.falar("Olá, João!") #chamada da função de fala, referente à Maria, dizendo Olá de volta, para joão
p2.__str__() #chamada da função para imprimir as informações acerca de Maria
