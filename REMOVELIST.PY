ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacoes = input("Operações (F, A ou S): ")

    i = 0
    while i < len(operacoes):
        operacao = operacoes[i]
        if operacao == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")

        i += 1
    
    if operacao == "S":
        break
