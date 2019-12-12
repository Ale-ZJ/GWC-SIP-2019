from random import *

#--- Define your functions below! ---

def main():
    intro()
    user = input("(What is your name?) ")
    print("(%s!, what a beautiful name) " %(user))

    answer = input("(What will you say?) ")
    process_answer(answer)

    games()

    bye(user)

#Other functions
def intro(): #bot presents itself
    print("(Hello, I am Karex the chatbot.) ")

def process_answer(response): #greet back or not
    greetings = ["hi", "hello", "hellow", "howdy", "hola", "hey", "aloha", "helo", "hey there"] #all possible greetings
    if response.lower() in greetings: #convert the response to lowercase and compare with the greetings list.
        greeting()
    else:
        default_ans()

def greeting():
    print("(Greetings non-artificial creation UwU.) ")

def default_ans():
    print("(I am not smart enough to answer to that... Anyways!) ")

def games():
    is_a_valid_input = False
    while not is_a_valid_input:
        answer = input("(I'm bored! What do you want to do?) ")
        is_a_valid_input = is_a_valid_answer(answer)
    if answer == "joke":
        action = input("(Would you like to hear a joke?) ")
        process_action(action)
    elif answer == "play":
        guess_the_number()
    elif answer == "surprise":
        surprise()

def is_a_valid_answer(response):
    valid_answer = ["joke", "play", "surprise"]
    unsure_answer = ["idk", "don't know", "you can pick", "you pick"]
    if response.lower() in valid_answer:
        return True
    elif response.lower() in unsure_answer:
        random_game()
    else:
        print("(Sorry, I didn't understand you.) ")
        return False

def random_game():
    games = ["joke", "play", "surprise"]
    randomIndex = randint(0, 2)
    if randomIndex == 0:
        action = input("(Would you like to hear a joke?) ")
        process_action(action)
    elif randomIndex == 1:
        guess_the_number()
    elif randomIndex == 2:
        surprise()

def process_action(joke_ans):
    x = ["yes", "ok", "yeah", "sure", "y"]
    if joke_ans in x:
        joke()
    else:
        print("(But my jokes are really good! :c) ")

def joke():
    answer = input("(What is absolute happiness?) ")
    if answer == "|happiness|":
        print("(:o Yas, you know your math! ) ")
    else:
        print("(Wrong!!)\n(Absolute happiness is |happiness|) ")

def guess_the_number():
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
                break
    print("Sorry, no more tries :c")

def surprise():
    print("KABOOM")

def bye(name):
    print("(It was really fun talking to you, %s!)\n(but I need to get my beauty sleep UwUr)\n(I hope you had fun today :3)" %(name))

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
