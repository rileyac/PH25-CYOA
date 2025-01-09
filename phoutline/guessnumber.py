import random

def use_tips(target_number, lower_bound, upper_bound):
    """Narrow the range to 70% around the target number."""
    range_span = upper_bound - lower_bound
    new_range = int(range_span * 0.5)
    mid_point = (lower_bound + upper_bound) // 2

    if target_number < mid_point:
        upper_bound = target_number + new_range // 2
        lower_bound = max(lower_bound, target_number - new_range // 2)
    else:
        lower_bound = target_number - new_range // 2
        upper_bound = min(upper_bound, target_number + new_range // 2)

    return max(lower_bound, 1), min(upper_bound, 100)

def guess_the_number():
    print("Welcome to Guess the Number!")

    # Set the range for the number to guess
    lower_bound = 1
    upper_bound = 50

    # Randomly select a number
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    # Set available tips
    available_tips = 3
    available_guesses = 5

    print(f"I have chosen a number between {lower_bound} and {upper_bound}. Can you guess it in 5 tries?")

    while True:
        try:
            # Ask the user if they want to use a tip
            if available_tips > 0 and available_guesses > 0:
                use_tip = input(f"Do you want to use a tip? Using a tip will narrow the bound by 50%. You have {available_tips} tips left. (yes/no): ").strip().lower()
                if use_tip == "yes":
                    lower_bound, upper_bound = use_tips(target_number, lower_bound, upper_bound)
                    available_tips -= 1
                    print(f"Tip: The number is now between {lower_bound} and {upper_bound}.")

            if available_guesses == 0:
                print("You have used up all your guesses.")
                return -1
            
            # Get user's guess
            guess = int(input("Enter your guess: "))
            available_guesses -= 1

            # Check the guess
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif guess < target_number:
                print("Too low! Try again.")
                print(f"You have {available_guesses} guesses left!")
            elif guess > target_number:
                print("Too high! Try again.")
                print(f"You have {available_guesses} guesses left!")
            else:
                print(f"Congratulations! You guessed the number {target_number}.")
                return 0
        except ValueError:
            print("Invalid input. Please enter a valid number.")