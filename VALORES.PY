L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar:"))
v = int(input("Digite o segundo valor a procurar:"))
achou_p = False
achou_v = False
pos_p = -1
pos_v = -1

x = 0
while x < len(L):
    if L[x] == p and not achou_p:
        achou_p = True
        pos_p = x
    x += 1

y = 0
while y < len(L):
    if L[y] == v and not achou_v:
        achou_v = True
        pos_v = y
    y += 1

if achou_p and achou_v:
    print(f"{p} e {v} achados nas posições {pos_p} e {pos_v}")
elif achou_p:
    print(f"{p} encontrado na posição {pos_p}, {v} não encontrado")
elif achou_v:
    print(f"{v} encontrado na posição {pos_v}, {p} não encontrado")
else:
    print(f"{p} e {v} não encontrados")
