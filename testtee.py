x = []
y = []

while True:
    n1 = int(input("Digite os números da primeira lista (0 sai): "))
    if n1 == 0:
        break
    x.append(n1)

b = 0
print("Números da primeira lista:")
while b < len(x):
    print(x[b])
    b = b + 1

while True:
    n2 = int(input("Digite os números da segunda lista (0 sai): "))
    if n2 == 0:
        break
    y.append(n2)

h = 0

while h < len(y):
    print(y[h])
    h = h + 1
