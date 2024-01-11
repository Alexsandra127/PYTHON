a= int(input("Digite o primeiro número: "))
b= int(input("Digite o segundo número: "))
escolha = input("Escolha qual operação deseja realizar, soma, subtração, multiplicação ou divisão: ")

if escolha == "soma" :
    resultado = a+b
    print("O resultado da operação é: ", resultado)
elif escolha == "subtração":
    resultado = a-b
    print("O resultado da subtração é: ", resultado)
elif escolha == "multiplicação":
    resultado = a*b
    print("O resultado da multiplicação é:", resultado)
elif escolha == "divisão":
    resultado = a/b
    print("O resultado da divisão é: ", resultado)
else:
    print("Opção inválida. Escolha uma operação válida: soma, subtração, multiplicação ou divisão.")