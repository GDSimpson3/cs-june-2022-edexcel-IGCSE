# Q06
import random

def generateWord(pWords):
    # Fully completed function that generates and returns a secret word
    randomNum = random.randint(0,len(pWords)-1)
    secretWord = pWords[randomNum]
    return secretWord

# Add your subprograms here
def guesses(guess):
    print (wordToGuess)
    # print(guessed)
    if guess == wordToGuess:
        print('fml')
        return True
    if guess != wordToGuess:
        for char in guess:
            for root in wordToGuess:
                if char == root:
                    correctLetterStore.add(char)
                else:
                    incorrectLetterStore.add(char)
        # attempts = attempts - 1
        return False




#---------------------------------------------------------------------------------------
# End of subprograms and start of main program from here



# Array of words
words = ["antelope","ape","badger","bear","beaver","bison","crocodile","elephant",
         "elk","ferret","goat","goose","kangaroo","llama","lion","monkey","moose",
         "orangutan","shark","snake","tiger","whale","wombat"]

# Secret word is generated. 
wordToGuess = generateWord(words)

# Add your main program code here

attempts = len(wordToGuess) + 3
guessed = False
correctLetterStore:set={""}
incorrectLetterStore:set={""}
correctLetterStore.remove("")
incorrectLetterStore.remove("")

print(f'Welcome, in this game you must guess a randomly selected animal within {attempts} attempts')

while guessed == False and attempts != 0:
    print(f'Remember, there are {len(wordToGuess)} characters in the animals name and you only have {attempts} attempts, Good luck!')
    guess = input('Submit your guess: ')
    while len(guess) != len(wordToGuess):
        print(f'please enter a word with {len(wordToGuess)} characters: ')
        guess= input(f'Submit your guess with {len(wordToGuess)} characters: ')
    if guesses(guess) == True:
        guessed = True
    else:
        attempts = attempts -1
    print(f'Correct letters: {correctLetterStore}')
    print(f'inCorrect letters: {incorrectLetterStore}')


if attempts == 0 & guessed == False:
    print(f"You ran out of guesses, the word was: {wordToGuess}")


if guessed == True:
    print(f'Congrats, you guessed the word in only {len(wordToGuess) + 3 -attempts} guesses, well done')
