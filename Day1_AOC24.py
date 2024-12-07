#Paul Lichtenwalner
#Advent of Code 2024
#Day 1 Challenge 1

#Open the text file with the input and create
#a list with the data
file = open('AOC24_Input/AOC24_Day1Input.txt', 'r')
data = file.read()
inputList = data.split('\n')

#Separate the list into two lists the left side
#values and the right side values
leftList = []
rightList = []
for set in inputList:
    leftList.append(int(set[0:5]))
    rightList.append(int(set[8:13]))

#Sort each list from least to greatest
leftList.sort()
rightList.sort()

#Calculate the total distance between corresponding
#values in each list
total = 0
for i in range(0, len(leftList)):
    total += abs(leftList[i] - rightList[i])
    i += 1

#Print the total distance between each corresponding
#vlue in each list
print(total)

#***************************************************
#Day 1 Challenge 2
#***************************************************

#Count the times the leftList number appears in the
#rightList
similarityScore = 0
for i in leftList:
    numCounter = 0
    for j in rightList:
        if i == j:
            numCounter += 1
    similarityScore += i * numCounter

#Print the similarity score
print(similarityScore)