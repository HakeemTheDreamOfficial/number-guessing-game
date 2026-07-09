import random
#defines the input needed to choose a difficulty level
difficulty_easy = "easy"
difficulty_medium = "medium"
difficulty_hard = "hard"
while True:
    #prompt the user for inputs
    difficulty = input("What difficulty level do you want? The options are easy, medium, and hard.")
    #will make it all lowercase and strip any extra spaces to solve edge cases
    difficulty = difficulty.strip().lower()
    #will ensure that we get an input that will actually lead somewhere
    if difficulty == difficulty_easy:
        print("Easy Difficulty Selected")
        break
    elif difficulty == difficulty_medium:
        print("Medium Difficulty Selected")
        break
    elif difficulty == difficulty_hard:
        print("Hard Difficulty Selected")
        break
    else: 
        #ensures that  any difficulty that is not recognized will get rerouted to reattempt to choose a difficulty
        print("Please enter a valid difficulty. The options are: easy, medium, and hard.")
#runs easy level
if difficulty == difficulty_easy:
    #chooses a random number
    random_number = random.randint(1,10)
    print("In easy difficulty, you have 3 hints and infinite tries to guess a number between 1 and 10.")
    #this defines hint number 1
    if random_number <5:
        hint_one = ("The random number is less than 5.")
    else:
        hint_one = ("The random number is greater than or equal to 5.")
    #this defines hint number 2
    half_of_random_number = random_number/2
    half_of_random_number = str(half_of_random_number)
    if half_of_random_number.endswith(".5"):
        hint_two = ("The random number is odd.")
    else:
        hint_two = ("The random number is even.")
    #this defines hint number 3
    if random_number in [2, 3, 5, 7, ]:
        hint_three = ("The random number is a prime number.")
    else: 
        hint_three = ("The random number is not a prime number.")
    #number of hints remaining
    hint_number = 1
    while True:
        #asks the user whether they want a hint or to guess
        guess_or_hint = input("Would you like to guess a number or to receive a hint. The options are: guess or hint.")
        #gets rid of edge cases
        guess_or_hint = guess_or_hint.strip().lower()
        #what happens if the user chooses to guess
        if guess_or_hint == "guess":
            guessed_number = input("What is your guess?")
            try:    
                #successful guess
                if random_number == int(guessed_number):
                    print("Congratulations, you guessed the mystery number successfully.")
                    break
                else: 
                    #unsuccessful guess returns to the option of guessing or to ask for a hint
                    print("You did not guess the correct number. Try again.")
            except ValueError:
                print("Please enter a valid integer between 1 and 10.")
        #hint number and limits
        elif guess_or_hint == "hint":
            #hint one
            if hint_number == 1:
                print(hint_one)
                hint_number = 2
            #hint two
            elif hint_number == 2:
                print(hint_two)
                hint_number = 3
            #hint three
            elif hint_number == 3:
                print(hint_three)
                hint_number = 4
            else:
                print("You are out of hints.")
        #what will happen if user types neither
        else:
            print("Please either type 'Guess' or 'Hint'.")
#runs medium level
if difficulty == difficulty_medium:
    #chooses random number between 1 and 25 to make it harder
    random_number = random.randint(1,25)
    print("In medium difficulty, you have 2 hints and infinite tries to guess a number between 1 and 25.")
    #this defines hint number 1 for medium level
    if random_number <13:
        hint_medium_one = ("The random number is less than 13.")
    else:
        hint_medium_one = ("The random number is greater than or equal to 13.")
    #this defines hint number 2 for medium level
    if random_number in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        hint_medium_two = ("The random number is a prime number.")
    else: 
        hint_medium_two = ("The random number is not a prime number.")
    #number of hints remaining
    hint_medium_number = 1
    while True:
        #asks the user whether they want a hint or to guess
        guess_or_hint = input("Would you like to guess a number or to receive a hint. The options are: guess or hint.")
        #gets rid of edge cases
        guess_or_hint = guess_or_hint.strip().lower()
        #what happens if the user chooses to guess
        if guess_or_hint == "guess":
            guessed_number = input("What is your guess?")
            try:    
                #successful guess
                if random_number == int(guessed_number):
                    print("Congratulations, you guessed the mystery number successfully.")
                    break
                else: 
                    #unsuccessful guess returns to the option of guessing or to ask for a hint
                    print("You did not guess the correct number. Try again.")
            except ValueError: 
                print("Please enter a valid integer between 1 and 25.")
        #hint number and limits
        elif guess_or_hint == "hint":
            #hint medium one
            if hint_medium_number == 1:
                print(hint_medium_one)
                hint_medium_number = 2
            #hint medium two
            elif hint_medium_number == 2:
                print(hint_medium_two)
                hint_medium_number = 3
            #out of hints
            else:
                print("You are out of hints.")
        #what will happen if user types neither
        else:
            print("Please either type 'Guess' or 'Hint'.")
#runs hard level
if difficulty == difficulty_hard:
    #chooses random number between 1 and 25 to make it harder
    random_number = random.randint(1,40)
    print("In hard difficulty, you have 2 hints and 10 tries to guess a number between 1 and 40.")
    #this defines hint number 1 for medium level
    if random_number <20:
        hint_hard_one = ("The random number is less than 40.")
    else:
        hint_hard_one = ("The random number is greater than or equal to 40.")
    #this defines hint number 2 for medium level
    if random_number in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        hint_hard_two = ("The random number is a prime number.")
    else: 
        hint_hard_two = ("The random number is not a prime number.")
    #number of hints remaining
    hint_hard_number = 1
    # number of guesses
    number_of_guesses = 0
    while True:
        #asks the user whether they want a hint or to guess
        guess_or_hint = input("Would you like to guess a number or to receive a hint. The options are: guess or hint.")
        #gets rid of edge cases
        guess_or_hint = guess_or_hint.strip().lower()
        #what happens if the user chooses to guess
        if guess_or_hint == "guess":
            guessed_number = input("What is your guess?")
            try:    
                #successful guess
                if random_number == int(guessed_number):
                    print("Congratulations, you guessed the mystery number successfully.")
                    break
                if number_of_guesses < 9:
                    #unsuccessful guess returns to the option of guessing or to ask for a hint
                    number_of_guesses = number_of_guesses + 1
                    if number_of_guesses > 1:
                        print(f"You did not guess the correct number. Try again.You have {10 - number_of_guesses} guesses left.")
                    else:
                        print(f"You did not guess the correct number. Try again. You have {10 - number_of_guesses} guess left.")
                else:
                    print("You ran out of guesses. FAILURE!")
                    break
            except ValueError: 
                print("Please enter a valid integer between 1 and 40.")
        #hint number and limits
        elif guess_or_hint == "hint":
            #hint medium one
            if hint_hard_number == 1:
                print(hint_hard_one)
                hint_hard_number = 2
            #hint medium two
            elif hint_hard_number == 2:
                print(hint_hard_two)
                hint_hard_number = 3
            #out of hints
            else:
                print("You are out of hints.")
        #what will happen if user types neither
        else:
            print("Please either type 'Guess' or 'Hint'.")