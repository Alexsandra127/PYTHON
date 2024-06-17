def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Exemplos de uso
print(mdc(48, 18))  # Saída: 6
print(mdc(56, 98))  # Saída: 14
