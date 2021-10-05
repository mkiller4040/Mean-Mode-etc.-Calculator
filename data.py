import math, csv, pandas, array, statistics

# with open('data.csv', newline = '') as f :
#     reader = csv.reader(f)
#     datalist = list(reader)

# data = []

# for j in datalist :
#     data.append(int(datalist[j]))

dataset = []

n = int(input("Enter number of numbers in the dataset : "))
print("Enter the numbers in the dataset one after another and press enter after inputting each one")

for i in range(0,n) :
    ele = int(input())
    dataset.append(ele)

# datalist = dataset.tolist()

def calcMean(data) :
    dataLength = 10
    dataSum = 0

    for i in data :
        # i = str(i)
        dataSum = dataSum + int(i)

    mean = dataSum/dataLength

    return mean

def calcMedian(data) :
    dataset.sort()

    lenght = int(len(dataset)/2)

    if(len(dataset)%2 == 0) :
        medianPt2 = dataset[int(lenght + 1)]
        medianPt1 = dataset[int(lenght)]

        median = (medianPt1 + medianPt2)/2

    else :
        median = dataset[int(len(dataset)/2)]

        return median

def calcMode(data) :
    mode = statistics.mode(dataset)

    return mode

def calcSTD(data) :
    squaredData = []
    for d in data :
        # d = str(d)
        meanDifference = int(d) - calcMean(dataset)
        meanDifferenceSq = meanDifference**2
        squaredData.append(meanDifferenceSq)
    
    squaredDataSum = 0

    for d in squaredData :
        squaredDataSum = squaredDataSum + d

    STD = math.sqrt((squaredDataSum/9))

    return STD

print("The mean of the dataset is :", calcMean(dataset))
print("The mode of the dataset is :", calcMode(dataset))
print("The median of the dataset is :", calcMedian(dataset))
print("The Standard Deviation of the dataset is :", calcSTD(dataset))