#Dicionários
    #Utiliza index no fomrato de Keys e values 
    #Aceita string, integer, float, boolena..
    
aluno = {'nome': 'Ana', 'Idade': 16, 'nota_final': 'A', 'aprovação':True}
#aluno.update({'endereco': 'Rua A'})

#del aluno['idade']

print(aluno.get('endereco', 'Não existe'))