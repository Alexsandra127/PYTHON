s = "AAACTBF"
z = "CBT"

comum = ""
for char in z:
    if char in s:
        comum += char

print(comum)

