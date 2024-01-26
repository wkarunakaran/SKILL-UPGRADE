import random

def guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Initialize the user's guess
    user_guess = None

    # Keep prompting the user until they guess the correct number
    while user_guess != target_number:
        try:
            user_guess = int(input("Enter your guess: "))

            if user_guess < target_number:
                print("Too low! Try again.")
            elif user_guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number, {target_number}!")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the guessing game
guessing_game()
