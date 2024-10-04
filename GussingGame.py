from random import randint

for x in range(1, 6):
    guessNumber = int(input("Enter your guess between 1 to 6: "))
    randomNumber = randint(1, 6)

    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was : ", randomNumber)
