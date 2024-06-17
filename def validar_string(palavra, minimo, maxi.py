def validar_string(palavra, minimo, maximo):
    tamanho = len(palavra)
    if minimo <= tamanho <= maximo:
        return True
    else:
        return False

# Exemplo de uso
palavra = "exemplo"
minimo = 5
maximo = 10

if validar_string(palavra, minimo, maximo):
    print("O tamanho da string está dentro do intervalo.")
else:
    print("O tamanho da string está fora do intervalo.")
