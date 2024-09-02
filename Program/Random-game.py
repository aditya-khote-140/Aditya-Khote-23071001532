import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    computer_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while True:
        # Get the user's guess
        user_guess = input("Enter your guess: ")
        
        # Check if the input is a valid integer
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        
        # Compare the user's guess with the computer's number
        if user_guess < computer_number:
            print("Too low! Try again.")
        elif user_guess > computer_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {computer_number}.")
            break

# Run the game
number_guessing_game()