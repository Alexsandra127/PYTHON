# Functions (Funções)
#DRY - Don't repeat yourself
#Parametro --> Argumento

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)}')
    
boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2)