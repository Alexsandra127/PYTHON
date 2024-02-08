'''
Escreva um programa que calcule o resto da divisão inteira entre dois
números. Utilize apenas as operações de soma e subtração para calcular o resultado.

'''

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Verifique se o segundo número é maior que zero para evitar um loop infinito
if b == 0:
    print("Erro: Divisão por zero!")
else:
    q = 0
    resto = a
    
    while resto >= b:
        resto = resto - b
        q = q + 1

    print("O resultado da divisão de", a, "por", b, "é:", q)
    print("O resto da divisão é:", resto)

