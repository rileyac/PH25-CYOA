def decode():
    print("For this mini-game, you must decode the message within 3 attempts and input the correct key to pass!")
    print("The encoding is in the form of an anagram. An anagram is ...")
    print("The anagram is: elrpa kscah")
    print("Answers are not case sensitive.")
    
    answer = "pearl hacks"
    guess = ""
    turn = 0
    max_attempts = 3 
    
    while guess != answer and turn < max_attempts:
        if turn > 0:
            print("Incorrect! Try again:")
        guess = input("Please enter your answer: ").lower()
        turn += 1
    
    if guess == answer:
        print("That is correct! You have passed the mini-game.")
    else:
        print("You have run out of guesses! You did not pass the mini-game.")


def riddle():
    print("For the following riddle, please enter a number as your answer. You are allowed 3 attempts.")
    print("The riddle is:")
    print("I am a three-digit number. My second digit is four times bigger than the third digit,")
    print("and my first digit is three less than the second digit. What number am I?")
    
    answer = 141
    guess = None
    turn = 0
    max_attempts = 3
    
    while guess != answer and turn < max_attempts:
        if turn > 0:
            print("Incorrect! Try again:")
        try:
            guess = int(input("Please enter your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        turn += 1
    if guess == answer:
        print("That is correct! You have passed the mini-game.")
    else:
        print("You have run out of guesses! You did not pass the mini-game.")


def trivia():
    instructions = (
    "Please enter only one-word answers. If the answer is numerical, please spell out the word, i.e., 'three', 'two', etc.\n"
    "Answers are not case-sensitive."
    )

    questions = [
        "What is the occupation of the Pearl Hacks mascot, Clover?",
        "How tall is Clover, in feet?",
        "What is Clover's favorite hobby? Hint: ends with -ing."
    ]

    answers = ["farmer", "one", "pickling"]

    success_message = "That was correct!"
    fail_message_template = "Oh no! That was not the correct answer. The correct answer was: "

    print("Welcome to the trivia mini-game! To pass this level, you must answer the following 3 questions correctly.")
    print(instructions)

    for i in range(len(questions)):
        print("\n" + questions[i]) # adds an empty line to break up the questions
        guess = input("Enter your answer here: ").lower()
        if guess == answers[i]:
            print(success_message)
        else:
            print(fail_message_template + answers[i])
            exit()

    print("\nCongratulations! You passed the trivia mini-game!")


decode()
riddle()
trivia()