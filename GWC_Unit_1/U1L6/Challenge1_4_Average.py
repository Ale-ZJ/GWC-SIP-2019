ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
sum = 0

for i in range(len(ages)): #begin counting indexes
    sum += ages[i] #add every number in the list

sum = sum / len(ages) #divide by amount of numbers in ages list

print(sum)


#another way
#for a in ages:
#   total += a
