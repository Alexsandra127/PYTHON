# Solicita ao usuário os dois números
z = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

# Inicializa a string para imprimir o resultado da multiplicação como uma soma
resultado_soma = f"{z} x {y} ="

# Utiliza um loop para somar y ao resultado z vezes
while z > 0:
    resultado_soma += f" {y} +"
    z -= 1

# Remove o último sinal de adição
resultado_soma = resultado_soma.rstrip('+')

# Imprime o resultado
print(resultado_soma)
