x=[]
y=[]


while True:
    n1 = int(input("Digite os núermos da primeira lista (0 sai): "))
    if n1 == 0:
        break
    x.append(n1)
   
b = 0

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
        h = h+1
x.extend(y)
print("Nova lista com elementos das duas listas:")      
z = 0 
while z < len(x):
    print(x[z])
    z += 1

    