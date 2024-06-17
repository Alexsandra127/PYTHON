#Erros
    #Excelente para testes
    #Não realiza o 'stop' no programa
    #Mensagens custmizadas quando encontra um erro
    
try: 
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:
    print('código ok')
    
#else:
#   print('Usuario digitou um valor correto)
#   resultado = valor * 2
#   print(resultado)