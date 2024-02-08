a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

if a == 0:
    print("Erro: Divisão por zero")
else: 
    print(f"O quociente é: {a/b} o qual foi truncado para: {a//b} ")