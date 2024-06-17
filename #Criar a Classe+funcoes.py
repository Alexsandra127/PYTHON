#Criar a Classe
class Funcionarios:
                        #Aqui em baixo estão os argumetos
    def __init__ (self, nome, sobrenome, data_nascimento):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento 

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome         
    

#Criar o objeto 
                        #Aqui em baixo os parametros
usuario1 = Funcionarios('Teixeira', 'JR', '12/05/1978')
usuario2 = Funcionarios('Ana', 'Hikman', '04/06/1789')
usuario3 = Funcionarios('Edu', 'Guedes', '19/07/1306')

#print
#print(usuário1.nome+ ' ' = usuario1.sobrenome)
print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))
