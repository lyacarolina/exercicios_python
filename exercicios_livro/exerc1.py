import random


def guessing_game():
    number = random.randint(0,100)

    
    while True:
        
        user_number = int(input("Adivinhe um número entre 0 e 100: "))
        
        if user_number == number:
            print("Número correto!!")
            break
            
        if user_number > number:
            print("Menos")

        if user_number < number:
            print("Mais")
            
            
guessing_game()