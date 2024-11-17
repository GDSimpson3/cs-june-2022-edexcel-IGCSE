# Q01g

storedLetter = "g"
letter = input("Input a letter ")
# Letter converted to lower case
letter = letter.lower()

# Amend the code by completing the if statement
if letter > storedLetter:
   print(f'{letter} comes after {storedLetter}') 
elif letter < storedLetter:
   print(f'{storedLetter} comes after {letter}')
else:
    print('they are the same')
