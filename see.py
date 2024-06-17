T = [ -10, -8, 0, 1, 2, 5, -2, -4]
minimo = T[0] 
maximo = T[0]


for e in T:
  if e < minimo:
    minimo = e
print(minimo)

for e in T: 
  if e > maximo:
    maximo = e
print(maximo)

media = 0
for e in T:
    media += e

media /= len(T)
print(media)




