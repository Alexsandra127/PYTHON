# Solicita ao usuário os dois números
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Inicializa a string que representará a multiplicação
rep = f"{a} % {b} = "

# Inicializa o resultado do quociente como zero
quociente = 0

# Utiliza um loop para calcular o quociente (divisão inteira) 
while a >= b:
    a -= b
    quociente += 1
# Calcula o resto
resto = a
# Imprime o resultado
print(rep + f"Quociente: {quociente}, Resto: {resto}")