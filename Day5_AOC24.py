#Paul Lichtenwalner
#Advent of Code 2024
#Day 5 Challenge 1

import re

def checkCond(pageArray, condArray):
    correctArray = []
    for update in pageArray:
        for i in range(0, (len(condArray) - 1)):
            if (condArray[i] in update) and (condArray[i + 1] in update):
                if (update.index(condArray[i]) < update.index(condArray[i + 1])):
                    correctArray.append(update)
    return correctArray

file = open('AOC24_Input/AOC24_Day5Input.txt', 'r')
data = file.read()
conditionals = re.findall(r'\d\d\|\d\d', data)
pageOrders = re.findall(r'\d\d\,.*', data)

newCond = []
for line in conditionals:
    nums = line.split('|')
    newCond.append(nums)
for conditional in newCond:
    for i in range(0, len(conditional)):
        conditional[i] = int(conditional[i])

newPages = []
for line in pageOrders:
    nums = line.split(',')
    newPages.append(nums)
for page in newPages:
    for j in range(0, len(page)):
        page[j] = int(page[j])
        
x = checkCond(newPages, newCond)
print(x)