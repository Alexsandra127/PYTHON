KM = int(input("Digite quantos KM deseja percorrer: "))
if KM <= 200:
    print("O valor da passagem é: R$ {: .2f}" .format(KM*0.50))
else:
    print("O valor da passagem é: R$ {: .2f}" .format(KM*0.45))