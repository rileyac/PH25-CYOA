def trivia():
    instructions = (
    "\nWelcome to Clover Trivia!"    
    "\nPlease enter only one-word answers."
    "\nIf the answer is numerical, please spell out the word, i.e., 'three', 'two', etc."
    "\nAnswers are not case-sensitive."
    )

    questions = [
        "What is Clover's occupation?",
        "How tall is Clover, in feet?",
        "What is Clover's favorite hobby? Hint: ends with -ing."
    ]

    answers = ["farmer", "one", "pickling"]

    success_message = "That was correct!"
    fail_message_template = "Oh no! That was not the correct answer. The correct answer was: "

    print(instructions)
    print("To gain Farmer Tom's help, you must answer the following 3 questions correctly.")

    for i in range(len(questions)):
        print("\n" + questions[i]) # adds an empty line to break up the questions
        guess = input("Enter your answer here: ").lower()
        if guess == answers[i]:
            print(success_message)
        else:
            print(fail_message_template + answers[i])
            print("You did not pass Farmer Tom's Trivia :(")
            return 0

    print("\nCongratulations! You passed the Farmer Tom's Trivia and gained a turnip!")
    return 1