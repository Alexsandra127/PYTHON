kwh = float(input("Digite quantos kWh você gastou:"))
inst = (input("Infomre seu tipo de instalação, residêncial, comercial ou industrial: "))
if inst == "residencial":
   if kwh <= 500:
      valor = kwh  * 0.40
   else:
      valor = kwh * 0.65
   print("Você vai pagar R$ {: .2F}" .format (valor))
if inst == "comercial":
    if kwh <= 1000:
       valor = kwh * 0.55
    else:
       valor = kwh * 0.65
    print("Você vai pagar R$ {: .2F}" .format (valor))
if inst == "industrial":
    if kwh <= 5000:
       valor = kwh * 0.55
    else:
       valor = kwh * 0.60
    print("Você irá pagar R${: .2f}" .format(valor))