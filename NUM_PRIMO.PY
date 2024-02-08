def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

contador = 0
num = 2  # Começamos a busca a partir do número 2, o primeiro primo

while contador < 100:
    if eh_primo(num):
        print(num, end=' ')
        contador += 1
    num += 1