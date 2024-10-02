class Pessoa:
    def __init__(self, nome):
        self.altura = 1.69
        self.idade = 22
        self.nome = nome
        

    def correr(self):
        print(f'olá meu nome é {self.nome}, tenho {self.altura}cm de altura e tenho {self.idade} anos')
        print('minha ação agora é correr até cansar')
        return f'{self.nome}: estou cansado, parei de correr'
    
    def comer(self):
        print('minha ação agora é comer')
        
        

minhaclasse = Pessoa(nome='matheus')

#response = minhaclasse.metodo2()
resp = minhaclasse.correr()
print(resp)

