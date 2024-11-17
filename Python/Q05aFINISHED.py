import re 

# Q05(a)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; # Valid uppercase letters in the alphabet
digit = "0123456789"; # Valid digits

passwordFile = open("passwords.txt", "r") # Open the file password.txt to read

# Add your code here
incorrectPasswords = 0 

formatRegexAZ = "^[A-Z]{1}"
for line in passwordFile:
    match = re.match(formatRegexAZ,line)
#    print(match)
    if not match:
        print(f'no capital letter at {line}')
        incorrectPasswords = incorrectPasswords + 1
    else:
        anynumbers = re.search("[0-9]",line)
        if not anynumbers:
            print(f'No numbers in {line}')
            incorrectPasswords = incorrectPasswords + 1

print(f'total of {incorrectPasswords} bad passwords')





passwordFile.close()
