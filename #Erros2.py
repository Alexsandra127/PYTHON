#Erros 
    #Não realiza o 'stop' no programa
    #Mensagens customizadas quando encontra um erro
    
try:
    valor = int(input('Digite o valor do seu prodruto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
    
print('Mais código abaixo')