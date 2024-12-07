#Paul Lichtenwalner
#Advent of Code 2024
#Day 3 Challenge 1

#Import the library for using regex
import re

#Read in the input text from the file
file = open('AOC24_Input/AOC24_Day3Input.txt', 'r')
txt = file.read()

#Use the regex to sort through the text and pull out
#segments that follow the pattern of mul(***,***)
x = re.findall(r'mul\(\d{1,3},\d{1,3}\)', txt)

#Use regex again to separate the digits from the rest
#of the sorted text and create a 2D array
numList = []
for elem in x:
    i = re.findall(r'\d{1,3}', elem)
    numList.append(i)

#Convert the string numbers in the 2D array into 
#integer values
for array in numList:
    for i in range(0, 2):
        array[i] = int(array[i])

#Initialize the total variable and add the product of
#the numbers in the 2D array to the total variable
total = 0
for array in numList:
    total += array[0] * array[1]

#Print the total value
print(total)

#***************************************************
#Day 3 Challenge 2
#***************************************************

#Create a list that follows the pattern above while also
#including any statements like do() and don't()
y = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', txt)

#Find the indexes of the do()s and don't() within the
#big list
doIndexes = [i for i, j in enumerate(y) if j == 'do()']
dontIndexes = [k for k, l in enumerate(y) if l == 'don\'t()']

#Create a new list to add the mul values to when the 
#doDontCondition is True
newList = []

#Loop through the entire list add the mul value to newList
#doDontCondition is True if the current element is a do or
#don't alter the condition accordingly
i = 0
doDontCondition = True
while i <= len(y) - 1:
    if (doDontCondition == True) and (i not in doIndexes) and (i not in dontIndexes):
        newList.append(y[i])
    elif (i in doIndexes):
        doDontCondition = True
    elif (i in dontIndexes):
        doDontCondition = False
    i += 1

#Everything below works exactly as in part 1
#Use regex again to separate the digits from the rest
#of the sorted text and create a 2D array
numList = []
for elem in newList:
    i = re.findall(r'\d{1,3}', elem)
    numList.append(i)

#Convert the string numbers in the 2D array into 
#integer values
for array in numList:
    for i in range(0, 2):
        array[i] = int(array[i])

#Initialize the total variable and add the product of
#the numbers in the 2D array to the total variable
total = 0
for array in numList:
    total += array[0] * array[1]

#Print the total value
print(total)