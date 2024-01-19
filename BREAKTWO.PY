'''
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.
'''

s = 0
contador = 0

while True:
    num = int(input("Digite um número inteiro ou Zero para sair: "))
    if num == 0:
        break
    else:
     s += num
    contador += 1

if contador == 0:
    print("Nenhum número inteiro diferente de zero foi digitado.")
else:
    media = s / contador
    print(f"A soma é {s} e a média é {media:.2f}.")


