import random   
num_sec = random.randint(1,20)
print('Acerte o Numero!!!\n')

while True:
    num = int(input('Defina um numero:'))
    if num_sec == num:
        print('Acertou!')
        break 
    elif num_sec < num:
        print('O numero é menor')
    else:
        print('O numero é maior')
        continue
    
    