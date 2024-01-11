a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# Inicializa os valores inicialmente como o maior e o menor
maior_valor = menor_valor = a

# Verifica e atualiza para o maior valor
if b > maior_valor:
    maior_valor = b
if c > maior_valor:
    maior_valor = c

# Verifica e atualiza para o menor valor
if b < menor_valor:
    menor_valor = b
if c < menor_valor:
    menor_valor = c

# Imprime os resultados
print("O maior valor é:", maior_valor)
print("O menor valor é:", menor_valor)
