# Q02b

# Write the function here
def checkPrime(pNumber):
    check=False
    if pNumber == 1:
        check=False
    else:
        check = True
        for count in range(2,pNumber):
            if pNumber % count == 0:
                check = False
    return check

# Write the main program here

number = int(input('Enter a number: '))
result = checkPrime(number)

if result == True:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
