# Q03

#  Initialise variables
orderTotal = 0 
priceDB = {
        5: 20,
        9: 15,
        10: 12,
        }

category = 5
#  Print prompt and take number of textbooks required
wantedBooks = int(input('how much books are required?: '))

#  Generate and display the price per textbook and the total cost
if wantedBooks >= 1 and wantedBooks <= 5:
    category = 5
elif wantedBooks >=6 and wantedBooks<=9:
    category = 9
elif wantedBooks >= 10:
    category = 10

orderTotal = orderTotal + (priceDB[category] * wantedBooks)

print(f'You ordered {wantedBooks} books at £{priceDB[category]} each \nYour order totaled up to £{orderTotal} ')
