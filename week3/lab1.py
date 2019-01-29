import math

def readList():
    a = input("Enter a set of numbers (separated by space):")
    stringlist = a.split(" ")
    numberlist = []
    #改成 while loop？
    for astring in stringlist:
        numberlist.append(float(astring))
    numberlist.sort()
    return numberlist

def calculateMean(numberlist):
    sum = 0.0
    for number in numberlist:
        sum += number
    mean = sum / len(numberlist)
    return mean

def calculateStandarDev(numberlist):
    #不用 calculateMean会怎样
    mean = calculateMean(numberlist)
    squareError = 0

    standardDeviation = math.pow(squareError / (len(numberlist) - 1), 0.5)
    return standardDeviation

def outlier(numberlist):
    outlierList = []
    return outlierList

def main():
    while True:
        numberlist = readList()
        print(numberlist)
        print(calculateMean(numberlist))
        print(calculateStandarDev(numberlist))
        print(outlier(numberlist))
        play = input("Do you want to enter more data? (Y/N):")
        if play == 'N' or play == 'n':
            break
main()