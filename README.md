# number-gussing-game
🎮 Code Breakdown
 SECTION           CODE                                      FUNCTIONALITY

Setup:           (import random)                  	-Imports the (random) module, which is needed to generate the secret number.
                 number_to_guess = random.
                 randint(1, 100)     	              -Generates a random integer between 1 and 100 (inclusive) and stores it as the target.
Game Loop:       while True:                        -Starts an infinite loop, allowing the player to keep guessing until they guess correctly or type 'exit'.
Input & Exit: 	 try: user_input = input(...)	      -Prompts the user for a guess and starts the error-handling block.
                 if user_input.lower() == 'exit':  	-Checks if the user wants to quit. If so, it prints a message and uses break to exit the loop.
                 guess = int(user_input)	          -Attempts to convert the user's input into an integer. If this fails (e.g., they enter a letter), the except                                                                 ValueError block handles it.
Input 
Validation:      if guess < 1 or guess > 100:       -Checks if the number is outside the allowed range (1-100) and uses continue to skip the rest of the loop and                                                                 prompt for a new guess. 
Comparison &
Feedback: 	     if guess < number_to_guess:        -Provides a hint if the guess is too low.
                 elif guess > number_to_guess:	    -Provides a hint if the guess is too high.
                 else:                           	  -If the guess is neither too low nor too high, it must be correct. Prints a success message and uses break to end                                                                  the game.
Error Handling:	except ValueError:	                -Catches the error if int(user_input) fails (meaning the user entered something that wasn't a number or 'exit').                                                               Prints an error message.
work:
- it picks a random number between 1 to  100
- you try gussing
- it tells too high / too low
- when correct / it shows number of attempts.
