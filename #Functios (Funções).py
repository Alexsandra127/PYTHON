#Functios (Funções)
    #DRY - Don't repeat yourself.
    #Parametro --> Argumento
    #Default = Aquele que você define o valor no parametro
    #Non-Defult = Aquele que você não define o valor no parametro
    
def boas_vindas(quantidade, nome='Linda'):
    print(f'Olá`{nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')
    
boas_vindas(6)