import random

def hangman():
    print("Welcome to Hangman!")
    print("Rules:")
    print("1. You need to guess the letters of a secret word.")
    print("2. You have a limited number of attempts to guess the word correctly.")

    words = ["glue", "rope", "twine", "patch", "straw"]
    word = random.choice(words)  # Randomly select a word
    current_state = ["_" for _ in word]  # Initialize blank state
    attempts = len(word) + 3  # Allow attempts equal to the length of the word plus 3

    print("The word to guess has", len(word), "letters.")
    print("Current state:", " ".join(current_state))

    while attempts > 0:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in word:
            i = 0
            for letter in word:
                if letter == guess:
                    current_state[i] = guess
                i += 1    
            print("Correct! Updated state:", " ".join(current_state))
        else:
            print("Wrong guess.")

        attempts -= 1
        print(f"Attempts remaining: {attempts}")

        if "_" not in current_state:
            print("Congratulations! You guessed the word:", word)
            return 0

    print("Out of attempts! The word was:", word)
    return -1