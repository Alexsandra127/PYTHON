salário=float(input("Digite o salário para cálculo do imposto: "))
base = salário 
imposto = 0
if base > 3000: 
 imposto = imposto + ((base - 3000) * 0.35) 
 base = 3000 
if base > 1000: 
 imposto = imposto + ((base - 1000) * 0.20) 
print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salário, imposto))