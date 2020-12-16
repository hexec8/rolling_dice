import random

dice = [1, 2, 3, 4, 5, 6]

user = input("Would you like to roll the dice? (y/n) ").lower()

if user == 'y':
    die_count = int(input("One (1) die?; or two (2)? "))

    if die_count == 1:
        print(random.choice(dice))
    elif die_count == 2:
        print((random.choice(dice)) + (random.choice(dice)))
    else:
        print("Invalid input")
else:
    print("Maybe next time... ")