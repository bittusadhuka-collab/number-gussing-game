import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        user_input = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
       
