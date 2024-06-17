#Functions (Funções)
    #DRY - Don't repeat yoursel;
    #Realizam uma tarefa
    #Calcula e retorna um valor
    
def cliente1(nome):
    print(f'Olá {nome}')
    

def cliente2(nome):
    return f'olá {nome}'

x = cliente1('Maria')
y = cliente2('Aligtor')

print(x)
print(y)

