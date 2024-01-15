import random


def guessing_game():
    number = random.randint(0,100)
    

    for x in range(1,4):
        user_number = int(input("Adivinhe um número entre 0 e 100: "))
                
        if user_number > number:
            print("Menos")

        elif user_number < number:
            print("Mais")
            
        else: 
            print("Número correto!!")
            return
            
    print(f"Você não tem mais tentativas. A resposta é {number}.")
        
guessing_game()