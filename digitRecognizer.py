import math
import operator
# Setting up the dataset
def setUpDataSet(filename, dataSet):
	with open(filename,'r') as f:
		numLine = 0
		for line in f:
			lineList = line.split(" ")
			dataSet.append(lineList)
			del dataSet[numLine][-1]
			for y in range(len(dataSet[numLine])):
				dataSet[numLine][y] = int(dataSet[numLine][y])
			numLine += 1

#Calculating distance
def getDistance(source, destination):
	distance = 0
	for x in range (len(source) - 1):
		distance += pow(source[x] - destination[x], 2)
	return math.sqrt(distance)

#Calculating K Nearest Neighbor
def getNeighbors(dataSet, target, k):
	potentialNeighbors = []
	for x in range(len(dataSet)):
		distance = getDistance(target, dataSet[x])
		potentialNeighbors.append((distance,dataSet[x]))
	potentialNeighbors.sort(key=operator.itemgetter(0))
	kNeighbors = []
	for x in range(k):
		kNeighbors.append(potentialNeighbors[x][1])
	return kNeighbors

#Getting the majority
def getMajority(neighbors):
	voteCount = [0,0,0,0,0,0,0,0,0,0]
	for x in range(len(neighbors)):

		#print(neighbors)
		voteCount[neighbors[x][-1]] += 1
		#print(neighbors[x][-1])
	majority = []
	for x in range(len(voteCount)):
		majority.append((x,voteCount[x]))
	#print(majority)
	majority = sorted(majority, key = operator.itemgetter(1), reverse = True)
	#print (majority)
	return majority[0][0]




#Main Method
dataSet = []
testSet = []
setUpDataSet('Training Data.txt', dataSet)
setUpDataSet('Test Data.txt', testSet)
correct = 0;
print(dataSet[0][len(dataSet[0]) - 1])
for x in range (len(testSet)):
	neighbors = getNeighbors(dataSet, testSet[x], 3)
	result = getMajority(neighbors)
	if result == testSet[x][-1]:
		correct += 1
	#print (result)
print ('Acc = ' + str((correct/float(len(testSet))) * 100.0) + '%')