'''
Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

'''

contador = 0
total = 0

while True:
    cp = int(input("Digite o código do produto (ou 0 para sair): "))
    if cp == 0:
        break 

    q = int(input("Digite a quantidade comprada: "))

    if q == 0:
        break
    if cp == 1:
        total += q * 0.50
    elif cp == 2:
        total += q * 1.00
    elif cp == 3:
        total += q * 4.00
    elif cp == 5:
        total += q * 7.00
    elif cp == 9:
        total += q * 8.00
    else:
        print("Código inválido")

    contador += 1

print(f"O total da sua compra é: R$ {total:.2f}")