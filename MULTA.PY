velo = int(input("Digite a velocidade do carro: "))
if velo > 80:
    multa = (velo - 80) * 5
    print("Você foi multado em R$ {:.2f}" .format(multa))
if velo <= 80:
    print("Sem multa! ")