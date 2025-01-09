import random

def hangman():
    print("Welcome to Hangman!")
    print("Rules:")
    print("1. You need to guess the letters of a secret word.")
    print("2. You have a limited number of attempts to guess the word correctly.")
    print("3. You can use up to 3 tips. When you use a tip, you'll be given 3 letters to choose from for the first blank position.")

    words = ["glue", "rope", "twine", "patch", "straw"]
    word = random.choice(words)  # Randomly select a word
    current_state = ["_" for _ in word]  # Initialize blank state
    attempts = len(word) + 3  # Allow attempts equal to the length of the word plus 3

    print("The word to guess has", len(word), "letters.")
    print("Current state:", " ".join(current_state))

    while attempts > 0:
        try:
            guess = input("Enter a letter: ").strip().lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue

            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        current_state[i] = guess
                print("Correct! Updated state:", " ".join(current_state))
            else:
                print("Wrong guess.")

            attempts -= 1
            print(f"Attempts remaining: {attempts}")

            if "_" not in current_state:
                print("Congratulations! You guessed the word:", word)
                return 0
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if "_" in current_state:
        print("Out of attempts! The word was:", word)
        return -1

#if __name__ == "__main__":
    #hangman_game()