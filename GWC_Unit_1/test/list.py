"""numbers = [1,2,3,2,1]

for num in numbers:
  print(num)

for i in range(len(numbers)):
    print(numbers[i])"""

"""anExample = "Alex!"
print(len(anExample))
#output: 5
print("ex" in anExample)
#output: True
print(anExample[2])
#output: e
print(anExample[2] + anExample[1])
#output: el
for letter in anExample:
    print(letter)"""

listA = [1, 2, 3, 4, 5]
listB = [listA, 6, 7, 8, 9]

for x in range(len(listB)):
    # if there is a list within this list
    if type(listB[x]) is list:
        for item in listB[x]:
            print(item)
    else:
        print(listB[x])

#2D List
twoD = [[1, 2, 3],[7, 8, 9]]

#print(twoD[0])
print(twoD[0][0])

#for item in twoD[0]:
#    print(item)
