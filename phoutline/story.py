from hangman import hangman
from guessnumber import use_tips
from guessnumber import guess_the_number
from trivia import trivia
from decode import decode

def main():
    turnips = 2

    # Intro
    print("Welcome to Clover's farm!")
    print("Life on the farm is usually peaceful for Clover the pig, but this week is no ordinary week.")
    print("Mischievous critters, wild weather, and sneaky thieves are after Clover the pig's precious crops.")
    print("Your lives are turnips— lose one each time you fail a mini-game. Lose them all, and the farm is doomed!")
    print("You currently have 2 turnips.")
    print("Help Clover conquer challenges and save the crops. Can you keep all the turnips and protect the farm? The adventure starts now!")

    # Hangman
    print("\nDay 1:")
    print("Clover notices the scarecrow is missing! Without it, the pesky crows are feasting on her crops.")
    print("To rebuild it, she must guess the missing word in Farmer Tom’s old instructions.")
    print("Complete the word before too many wrong guesses or the scarecrow stays broken, and Clover loses a turnip.\n")
    turnips += hangman()
    print(f"\nYou have {turnips} turnips remaining!")

    # Trivia
    print("\nDay 2:")
    print("Farmer Tom appears with extra supplies, but he’s feeling playful.")
    print("“Let’s see how well you know Clover,” he says.")
    print("Tom's trivia is special because if you pass, you gain an extra turnip!")
    print("You do not lose any turnips for failing the trivia, because he is feeling nice.")
    turnips += trivia()
    if turnips == 0:
        print("Oh no! You have lost all of your turnips, and Clovers farm was overrun by crows and critters.")
        print("Better luck next time!")
        exit()
    print(f"\nYou have {turnips} turnips remaining!")
    
    # Guess the Number
    print("\nDay 3:")
    print("A section of the fence has collapsed, letting critters sneak in.")
    print("Clover must measure the perfect length of wood needed to fix it.")
    print("Guess the correct number within a limited range before the critters invade.")
    print("If Clover fails, she loses another precious turnip.\n")
    turnips += guess_the_number()
    if turnips == 0:
        print("Oh no! You have lost all of your turnips, and Clovers farm was overrun by crows and critters.")
        print("Better luck next time!")
        exit()
    print(f"\nYou have {turnips} turnips remaining!")

    # Decode
    print("\nDay 4 (Last Day!)")
    print("Clover intercepts a note from the crop thief that reveals the time of the heist.")
    print("But, the letters are all scrambled up!")
    print("You must unscramble the letters to save Clover and her farm.")
    print("If you solve the puzzle in time, Clover catches the thief red-handed and saves her crops.")
    print("Fail, and the thief escapes with the crops, costing Clover all of her turnips.")
    if decode() == -1:
        print("Oh no! You have lost all of your turnips, and Clovers farm was attacked by the crop theif!")
        print("Better luck next time!")
        exit()
    print("Yippeeee!!!! You have saved Clover and her farm!")    

    

        









if __name__=="__main__":
    main()    