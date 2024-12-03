import random

def guessing_game():
    while True:
        print("Guess the Number Game!")
        secret_number = random.randint(1, 10)
        while True:
            try:
                guess = int(input("Guess a number between 1 and 10: "))
                if guess == secret_number:
                    print("Yeah, you guessed it!")
                    break
                else:
                    print("Try again!")
            except ValueError:
                print("Please enter a valid number.")
        
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

guessing_game()
