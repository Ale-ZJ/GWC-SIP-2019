import random

"""
choices = ["example", "word", "yes", "what"]
word = random.choice(choices) #select a random word from the list choices"""

word = "patrick"

#variables used
tries = len(word) *2
guesses = "" #stores all the user's guesses
blanks = [" _ "] * len(word) #list of blanks for the word
is_correct = False



while tries <=7:
    guess = input("Guess a letter: ")
    for letter in word:
        if letter == guess:
            print(guess)
            word.index(guess)
        elif letter != guess:
            print("Noup")
            tries += 1
            continue



#for i in range(len(word)):
