'''
WHILE LOOPS
Excelente para loops dependentes de uma condição.
Publicar um produto com comissão de 10% se for acima de R$20
'''

valor = int(input('Digite o valor do seu produto em r$: '))
while valor>20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de r${valor}')
    break

