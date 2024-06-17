velocidade = int(input("Digite a velocidade " ))


if velocidade > 110:
    print("Acima da velocidade permitida!")
    print("Favor reduzr a sua velocidade")
elif velocidade < 60:
    print("Favor dirigir acima de 80Km/h")
else: 
    print("Velocidade OK")