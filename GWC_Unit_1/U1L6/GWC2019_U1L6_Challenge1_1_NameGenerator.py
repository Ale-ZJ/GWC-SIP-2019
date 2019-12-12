print("Welcome to the name generator!")
lenght = input("How long do you want the name to be? (short/med/long)") #ask how long the name should be

#possible name combinations
nameA = ["Al", "Ber", "Bel", "Car", "Kar", "Moon", "Nas", "Lat", "Jes"]
nameB = ["ex", "lo", "la", "na", "ba", "hi", "lar"]
nameC = ["", "an", "en", "fis", "te", "yu"]
nameD = ["", "dra", "der", "dro", "na", "th"]

#generate a random index
from random import *
A = randint(0, (len(nameA)-1))
B = randint(0, (len(nameB)-1))
C = randint(0, (len(nameC)-1))
D = randint(0, (len(nameD)-1))

#change index depending on the preferred lenght
if lenght == "short":
    C = 0
    D = 0
elif lenght == "med":
    D = 0

#join everything together
print(nameA[A] + nameB[B] + nameC[C] + nameD[D])
