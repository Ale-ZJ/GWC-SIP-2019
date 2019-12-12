print("Welcome to the restaurant!")
quantity = input("How much do you eat? (little/normal/lot)") #how much for the menu

#lists of all the possible food for the menu
appetizer = ["no appetizer ", "Caesar Salad ", "Garlic Bread "]
main = ["Fish ", "Short Ribs ", "Adobe Chicken ", "Curry ", "Meatballs "]
sides = ["no side ", "Kimchi ", "Rice ", "Mashed Potatoes ", "Sautee Corn "]
dessert = ["Cheesecream ", "Cookies ", "Croissant ", "Egg Tart ", "Gelatin "]

#generate random index
from random import *
A = randint(0, (len(appetizer)-1))
B = randint(0, (len(main)-1))
C = randint(0, (len(sides)-1))
D = randint(0, (len(dessert)-1))

#change the index according to how much food ppl wants
if quantity == "little":
    C = 0
    A = 0
elif quantity == "normal":
    C = 0

#print the generated menu
print("Your couse meal for today is: ")
print(appetizer[A] + main[B] + sides[C] + dessert[D])
