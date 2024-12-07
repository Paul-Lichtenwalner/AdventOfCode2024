#Paul Lichtenwalner
#Advent of Code 2024
#Day 4 Challenge 1

#Import the RegEx library
import re

#Search for the amount of sequences of XMAS and SAMX
#that run horizontally and return the number
def horizontal(array):
    count = 0
    for elem in array:
        x = re.findall(r'XMAS|SAMX', elem)
#Account for overlapping
        y = re.findall(r'XMASAMX|SAMXMAS', elem)
        count += len(x) + len(y)
    return count

#Search for the amount of sequences of XMAS and SAMX
#that run vertically and return the number
def vertical(array):
    count = 0
#Search top to bottom
    for i in range(0, (len(array) - 3)):
        for j in range(0, len(array[i])):
            if array[i][j] == 'X':
                if array[(i + 1)][j] == 'M':
                    if array[(i + 2)][j] == 'A':
                        if array[(i + 3)][j] == 'S':
                            count += 1
            else:
                continue
#Search bottom to top
    for i in range((len(array) - 1), 2, -1):
        for j in range(0, len(array[i])):
            if array[i][j] == 'X':
                if array[(i - 1)][j] == 'M':
                    if array[(i - 2)][j] == 'A':
                        if array[(i - 3)][j] == 'S':
                            count += 1
            else:
                continue
    return count

#Search for the amount of sequences of XMAS and SAMX
#that run diagonally and return the number
def diagonal(array):
    count = 0
#Search top-bottom left-right
    for i in range(0, (len(array) - 3)):
        for j in range(0, (len(array[i]) - 3)):
            if array[i][j] == 'X':
                if array[(i + 1)][j + 1] == 'M':
                    if array[(i + 2)][j + 2] == 'A':
                        if array[(i + 3)][j + 3] == 'S':
                            count += 1
            else:
                continue
#Search top-bottom right-left
    for i in range(0, (len(array) - 3)):
        for j in range((len(array[i]) - 1), 2, -1):
            if array[i][j] == 'X':
                if array[(i + 1)][j - 1] == 'M':
                    if array[(i + 2)][j - 2] == 'A':
                        if array[(i + 3)][j - 3] == 'S':
                            count += 1
            else:
                continue
#Search bottom-top right-left
    for i in range((len(array) - 1), 2, -1):
        for j in range((len(array[i]) - 1), 2, -1):
            if array[i][j] == 'X':
                if array[(i - 1)][j - 1] == 'M':
                    if array[(i - 2)][j - 2] == 'A':
                        if array[(i - 3)][j - 3] == 'S':
                            count += 1
            else:
                continue
#Search bottom-top left-right
    for i in range((len(array) - 1), 2, -1):
        for j in range(0, (len(array) - 3)):
            if array[i][j] == 'X':
                if array[(i - 1)][j + 1] == 'M':
                    if array[(i - 2)][j + 2] == 'A':
                        if array[(i - 3)][j + 3] == 'S':
                            count += 1
            else:
                continue
    return count

#Read the file into a list and split the data by rows
file = open('AOC24_Input/AOC24_Day4Input.txt', 'r')
data = file.read()
crosswordRows = data.split('\n')

#Initialize the count and add the number of horizontal
#sequences before changing the list structure
xmasCount = 0
xmasCount += horizontal(crosswordRows)

#Change the structure of the list into individual letters
letterList = []
for elem in crosswordRows:
    tempList = list(elem)
    letterList.append(tempList)

#Add the number of vertical and diagonal sequences to the count
xmasCount += vertical(letterList) + diagonal(letterList)

#Print the total count
print(xmasCount)

#***************************************************
#Day 4 Challenge 2
#***************************************************

#Create a function to find all possible variations of
#the X-MAS pattern
def x_mas(array):
    count = 0
#Loop through the array to find the M M
#pattern                             A
#                                   S S
    for i in range(0, (len(array) - 2)):
        for j in range(0, (len(array[i]) - 2)):
            if (array[i][j] == 'M') and (array[i][j + 2] == 'M'):
                if array[(i + 1)][j + 1] == 'A':
                    if (array[(i + 2)][j] == 'S') and (array[(i + 2)][j + 2] == 'S'):
                        count += 1
            else:
                continue
#Loop through the array to find the S S
#pattern                             A
#                                   M M
    for i in range(0, (len(array) - 2)):
        for j in range(0, (len(array[i]) - 2)):
            if (array[i][j] == 'S') and (array[i][j + 2] == 'S'):
                if array[(i + 1)][j + 1] == 'A':
                    if (array[(i + 2)][j] == 'M') and (array[(i + 2)][j + 2] == 'M'):
                        count += 1
            else:
                continue
#Loop through the array to find the M S
#pattern                             A
#                                   M S
    for i in range(0, (len(array) - 2)):
        for j in range(0, (len(array[i]) - 2)):
            if (array[i][j] == 'M') and (array[i][j + 2] == 'S'):
                if array[(i + 1)][j + 1] == 'A':
                    if (array[(i + 2)][j] == 'M') and (array[(i + 2)][j + 2] == 'S'):
                        count += 1
            else:
                continue
#Loop through the array to find the S M
#pattern                             A
#                                   S M
    for i in range(0, (len(array) - 2)):
        for j in range(0, (len(array[i]) - 2)):
            if (array[i][j] == 'S') and (array[i][j + 2] == 'M'):
                if array[(i + 1)][j + 1] == 'A':
                    if (array[(i + 2)][j] == 'S') and (array[(i + 2)][j + 2] == 'M'):
                        count += 1
            else:
                continue
    return count

#Initialize a new counting variable and count
#all the sequences
newX_MASCount = 0
newX_MASCount += x_mas(letterList)

#Print the number of sequences
print(newX_MASCount)