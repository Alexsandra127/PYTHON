a = "CTA"
b = "ABC"
c = "BT"

comum = ""
for char in b:
    if char in a:
      comum += char 

for char in c:
    if char in a: 
      comum += char

print(comum)
