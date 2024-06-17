#Unpacking Lists
    #Armazenar mais de uma informação  em variáveis. 
    #Manter a sequencia dos dados em uma variável. 

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5,6,7,8]

item1, item2, *outros, item8 = produtos

print(item1) #arroz
print(item2) #feijão
print(item8) #8
print(outros ) #['laranja, 'banana', 5,6,7,]