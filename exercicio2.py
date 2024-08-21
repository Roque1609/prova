import random
opc = ["pedra", "papel", "tesoura"]
escolha = random.choice(opc)
print("Jogue pedra, papel e tesoura com o Computador!\n")

while True:
    user = input("Escolha entre pedra, papel e tesoura:")
    if user == escolha:
        print('O jogo deu Empate!\n')
    elif (user == 'pedra' and escolha == 'tesoura') or \
    (user == 'papel' and escolha == 'pedra') or \
    (user == 'tesoura' and escolha == 'papel'):
        print('Você ganhou!\n')
    else:
        print('Você perdeu!\n')
    break
print('O jogo acabou inicie o programa caso queira jogar novamente!')




    

