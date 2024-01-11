c = int(input("Digite a quantidade de cigarros fumados por dia: "))
a = int(input("Digite por quantos anos fumou: "))
print("Restam-lhe tantos dias de vida: {:.0f}" .format((((a*365*c)*10)/60)/24))