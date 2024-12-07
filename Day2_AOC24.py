#Paul Lichtenwalner
#Advent of Code 2024
#Day 2 Challenge 1

#Returns boolean value if the list is ascending or not
def isAscending(array):
    for i in range(0, (len(array) - 1)):
        if array[i] < array[i+1]:
            continue
        else:
            return False
    return True

#Returns boolean value if the list is descending or not
def isDescending(array):
    for i in range(0, (len(array) - 1)):
        if array[i] > array[i+1]:
            continue
        else:
            return False
    return True

#Returns true if the step between values is never
#greater than 3
def checkStep(array):
    for i in range(0, (len(array) - 1)):
        if (abs(array[i] - array[i+1])) <= 3:
            continue
        else:
            return False
    return True

#Count how many arrays in the 2D array meet the 
#conditions to be "safe"
#Conditions: Must be either ascending or descending
#and not have a step greater than 3
def safeCount(array2D):
    safeCount = 0
    for list in array2D:
        if isAscending(list) or isDescending(list):
            if checkStep(list):
                safeCount += 1
    return safeCount

#Read the input data and separate it by lines into
#a list
file = open('AOC24_Input/AOC24_Day2Input.txt', 'r')
data = file.read()
inputList = data.split('\n')

#Further split the input list into a 2D array of
#each line and the integer values
reportList = []
for i in inputList:
    x = i.split(' ')
    tempList = []
    for j in x:
        tempList.append(int(j))
    reportList.append(tempList)

#Print the number of safe reports
print(safeCount(reportList))

#***************************************************
#Day 2 Challenge 2
#***************************************************

#Checks to see if the given array is safe
def isSafe(array):
    if isAscending(array) or isDescending(array):
            if checkStep(array):
                return True
    return False

#Initialize new safe count value
newSafeCount = 0

#Iterate through each report to determine if they are
#safe or not
for report in reportList:
    if isSafe(report):
        newSafeCount += 1
    else:
        isSafeWithDampener = False
#Loop through the list taking out one level and checking
#if it is now safe
        for i in range(len(report)):
#Creates a replica list of report only without
#the i element
            tempList = report[ : i] + report[i + 1 : ]
            if isSafe(tempList):
                newSafeCount += 1
                isSafeWithDampener = True
                break

#Print the updated safe count
print(newSafeCount)