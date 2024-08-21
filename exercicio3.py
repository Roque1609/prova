for i in range(1, 36):
    if i % 3 == 0 and i % 5 == 0:
        asw = "FizzBuzz"
    elif i % 3 == 0:
        asw = "Fizz"
    elif i % 5 == 0:
        asw = "Buzz"
    else:
        asw = str(i)
    
    user_asw = input(f"Número {i}: ")
    
    if user_asw != asw:
        print(f"Erro! Você deveria ter dito '{asw}'.")
        break
else:
    print("Parabéns! Você completou o jogo.")