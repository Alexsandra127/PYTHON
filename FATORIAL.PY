fat = int(input("Digite um número: "))
ans = 1
if fat >= 2:
    while fat > 1:
        ans = ans * fat
        fat = fat - 1 
    print("O fatorial é: ", ans) 
else:
    print("O fatorial de", fat, "não está definido.")
