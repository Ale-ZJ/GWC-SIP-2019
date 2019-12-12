#This is a comment
#Python doesn't read
#what goes here
#Only for Humans!

#prints hello world
print("Hello, Word!")

name = input("What is your name :) ? ")
print("Hello", name, "! Welcome to my survey")
ans1 = input("Are you ready?")

if (ans1 == 1):
    print("Roger that, let's begin")
    answer = input("Who inspires you? ")
    pet = input("What is your favorite animal?")
    hobby = input("What is your favorite hobby?")
    print("Wow,", name, " thanks for completing this survey. I have learned a lot of things about you!")
    print(answer, "inspires you! Amazing!")
    print("On your free time you ", hobby, " and you love", pet)
elif (ans1 == 0):
    print("Ok, donnut worry")
    print("See you next time")

value = True
anotherValue = False
yetAnotherValue = True

#print("& ", value & anotherValue)
#print("^ ", value & anotherValue)
#print("== ", value == yetAnotherValue)
