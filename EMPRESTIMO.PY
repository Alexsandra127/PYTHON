imovel = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos será o financiamento: "))
prestacao = imovel/(anos*12)
if prestacao<= salario*0.30:
    print("Emprestimo aprovado! valor da prestação R$: {:.2f} " .format(prestacao))
else:
    print("Emprestimo reprovado! renda insuficiente.")