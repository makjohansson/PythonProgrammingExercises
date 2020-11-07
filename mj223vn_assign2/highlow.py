import random

GUESS_LIMIT = 11
guesses = 1
toGuess = random.randint(1,100)
won = False

while guesses < GUESS_LIMIT:
    theGuess = int(input(f"Guess {guesses}: "))
    if theGuess == toGuess:
        print(f"\tCorrect answer after only {guesses} guesses - Excellent!")
        won = True
        break
    clue = "lower" if theGuess > toGuess else "higher"
    print(f"\tClue: {clue}")
    guesses += 1
    

if not won:
    print("Better luck next time!!\nBye")


