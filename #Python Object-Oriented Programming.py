#Python Object-Oriented Programming

#Classes
    #Utilizados para criar Objetos (instances)
    #Objetos são partes dentro de uma Class (instances)
    #Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    #=====
    
    #class: Frutas
    #Objects: Abacate, Banana...
    
class Funcionarios:
    nome = 'Joao'
    sobrenome = 'Fonseca'
    data_nascimento = '12/,1/1979'
    
usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)