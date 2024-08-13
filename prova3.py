# Prova 3 (MEU DEUS ISSO AQUI É MUITO DIFICIL MESMO EU ENTENDENDO O QUE CADA COISA FAZ NO CODIGO AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)

import random

num_gerado = random.randint(1, 10)
tentativa = 3

while True:
    if(tentativa < 1):
        print("Suas chances acabaram!")
        break
    
    tentativa = tentativa-1
    num = int(input('Digite um número:'))
    if num == num_gerado:
        print("O número que você escolheu está correto!")
        tentardenovo = input('Deseja continuar?:')
        if(tentardenovo == "sim"):
            tentativa = 3
            num_gerado = random.randint(1, 10)
        else:
            break
