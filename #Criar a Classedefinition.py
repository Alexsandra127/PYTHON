#Criar a Classe
class Funcionarios:
                        #Aqui em baixo estão os argumetos
    def __init__ (self, nome, sobrenome, data_nascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento 

#Criar o objeto 
                        #Aqui em baixo os parametros
usuario1 = Funcionarios('Teixeira', 'JR', '12/05/1978')
usuario2 = Funcionarios('Ana', 'Hikman', '04/06/1789')
usuario3 = Funcionarios('Edu', 'Guedes', '19/07/1306')

#print
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)        