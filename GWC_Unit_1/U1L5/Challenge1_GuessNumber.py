from random import *

aRandomNumber = randint(1,20) #generates a random number

x = 0

while x <= 2:
    guess = input("Guess a number between 1 and 20 inclusive: ")

    if not guess.isnumeric(): #checks if a string is only digits 0 to 9
        print("Hey, that is not a positive whole number!")
    else:
        guess = int(guess) #converts a string to an integer

        if guess < aRandomNumber:
            print("Try a higher number!")
            x += 1
        elif guess > aRandomNumber:
            print("Try a lower number!")
            x += 1
        elif guess == aRandomNumber:
            print("YAY, YOU WON!")

print("Sorry, no more tries :c")
