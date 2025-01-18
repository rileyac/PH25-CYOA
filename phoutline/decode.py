def decode():
    print(f"You must decode the word within {max_attempts} attempts and input the correct word to pass!")
    print("The scrambled time is: tighdnmi")
    
    answer = "midnight"
    guess = ""
    turn = 0
    max_attempts = 3 
    
    while guess != answer and turn < max_attempts:
        if turn > 0:
            print("Incorrect! Try again:")
        guess = input("Please enter your answer: ").lower()
        turn += 1
    
    if guess == answer:
        print("That is correct! You have revealed the time of the heist!")
        return 0
    else:
        print("You have run out of guesses! You did not reveal the time of the heist.")
        return -1