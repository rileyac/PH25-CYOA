import random

def use_tips(target_number, lower_bound, upper_bound):
    """Narrow the range to 50% around the target number."""
    range_span = upper_bound - lower_bound
    new_range = range_span // 2

    lower_bound = target_number - new_range // 2
    upper_bound = target_number + new_range // 2

    return max(lower_bound, 1), min(upper_bound, 100)

def guess_the_number():
    # Set the range for the number to guess
    lower_bound = 1
    upper_bound = 50

    # Randomly select a number
    target_number = random.randint(lower_bound, upper_bound)

    # Set available tips
    available_tips = 3
    available_guesses = 5
    
    # Intro
    print("Welcome to Guess the Number!")
    print(f"You have {available_guesses} attempts to guess the perfect amount of wood that Clover needs to fix her fence!")
    print(f"At any point, you can also use one of your tips. Tips will narrow the guessing range by about 50%.")
    print(f"The number is between {lower_bound} and {upper_bound}.")

    while True:
        
        if available_guesses == 0:
            print(f"You did not guess the number {target_number}")
            return -1
        
        # Ask the user if they want to use a tip
        if available_tips > 0:
            use_tip = input(f"You have {available_tips} tips left. Enter 'yes' to use a tip: ").strip().lower()
            if use_tip == "yes":
                lower_bound, upper_bound = use_tips(target_number, lower_bound, upper_bound)
                available_tips -= 1
                print(f"Tip: The number is now between {lower_bound} and {upper_bound}.")
        
        # Get user's guess
        guess = input("Enter your guess: ")
        # Make sure guess is an int
        if not guess.isdigit():
            print("Please enter a valid digit")
            continue
        guess = int(guess)

        # Make sure guess is in range
        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            continue
        
        available_guesses -= 1

        # Check the guess
        if guess < target_number:
            print("Too low!")
            print(f"You have {available_guesses} guesses left!")
        elif guess > target_number:
            print("Too high!")
            print(f"You have {available_guesses} guesses left!")
        else:
            print(f"Congratulations! You guessed the number {target_number}.")
            return 0        