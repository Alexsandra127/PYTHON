'''
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.
Vejamos como exemplo um programa que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor, apresentado na listagem
5.14. Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas
de R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1.
Modifique o programa para aceitar valores decimais, ou seja, também
contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50.
'''

# Definindo os valores das cédulas e moedas em centavos
valores = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 2, 1]

# Inicializando variáveis
valor = float(input("Digite um valor ou Zero para sair: "))

# Convertendo o valor para centavos
valor_em_centavos = int(valor * 100)

# Calculando a quantidade de cédulas e moedas
print("Quantidade de cédulas e moedas:")
for val in valores:
    quantidade = valor_em_centavos // val
    valor_em_centavos %= val
    if quantidade > 0:
        print(f"R$ {val/100:.2f}: {quantidade}")
