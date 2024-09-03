import random

def number_guessing_game():
    com_num = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while True:
        user_guess = input("Enter your guess: ")
        
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        
        if user_guess < com_num:
            print("Too low! Try again.")
        elif user_guess > com_num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {com_num}.")
            break

# Run the game
number_guessing_game()