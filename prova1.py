# Prova 1

base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

if base <= 0 or altura <= 0:
    print("Os valores da base e da altura devem ser positivos.")
else:
    area = base * altura
    print(f"O valor da área do retângulo é {area} metros quadrados")
