import random
import string
import numpy as np
POOL_SIZE = 10
INPUT_LEN = 5
SELECTION_SIZE = 6 #Must be even number
'''
Genetic Algorithm


'''
class Child:
	def __init__(self,_index):
		self.index = _index
		self.string= ""
		self.fitness=0.0
		self.probability=0.0

	def setStr(self):
		for i in range(INPUT_LEN):
			rndChar = random.choice(string.ascii_lowercase)
			self.string +=rndChar

	def setFitness(self, _myStr):
		child_str = self.string
		ascii_value=0
		for i in range(len(child_str)):
			ascii_value += ord(child_str[i])-ord(_myStr[i])
		gap = float(ascii_value)/len(child_str)
		self.fitness = gap * gap

	def setProbability(self,_sumOfFitness):
		self.probability = (1.0 - (self.fitness/_sumOfFitness) - (1.0/POOL_SIZE)) / (POOL_SIZE-2)

	


def createChildren():
	#Create an Child class array of size POOL_SIZE
	children = []
	for i in range(POOL_SIZE):	
		children.append(Child(i))
	return children

def evalulateChildren(_children, _myStr):
	sumOfFitness = 0
	for i in range(len(children)): # i : 0~9
		children[i].setStr()
		children[i].setFitness(_myStr)
		sumOfFitness += children[i].fitness
	sumOfProbability = 0 #Defined just for check
	for i in range(len(children)): # j : 0~9
		children[i].setProbability(sumOfFitness)
		sumOfProbability += children[i].probability
		# print("%d'th sumOfProbability is %f" % (i,sumOfProbability)) #To Check it is up to 1 or not.
def printAttributesOfChildren(_children):
	print("================================================",end="\n")
	print("Generated string\tfitness\t\tprobability",end="\n\n")
	for i in range(len(_children)):
		print("index %d is %s\t%f\t%f" %(i, _children[i].string,_children[i].fitness,_children[i].probability))
	print("================================================",end="\n\n")

def getFittestGenes(_children,size):
	prob_list = []
	for i in range(len(_children)):
		prob_list.append(_children[i].probability)
	indexOfFittest = []
	for i in range(size) :
		indexOfFittest.append( np.random.choice(list(range(POOL_SIZE)), p=prob_list))
	return indexOfFittest

	#Afer crossover, assign to newGeneration's child's string
def crossoverChildren(_nextGeneration, _children, _fittestIndex):
	rndInt = 1+(np.random.randint(INPUT_LEN-1, size=1))[0] # rndInt : 1~INPUT_LEN-1
	print("rndInt is %d"%rndInt)
	j=0
	for i in range(0,len(_fittestIndex),2):
		print (_fittestIndex[i])
		newString = _children[_fittestIndex[i]].string[:rndInt] + _children[_fittestIndex[i+1]].string[rndInt:]
		_nextGeneration[j].string = newString
		j += 1


#Get Input String from user.
print("====== Please enter myStr ======")
myStr = input()
print("================================",end="\n\n")



#Create and Evaluate Chilren
children = createChildren()
evalulateChildren(children,myStr)

#Check Attributes
printAttributesOfChildren(children)

#Select  index of the fittest genes list size of SELECTION_SIZE
fittestIndex = []
fittestIndex = getFittestGenes(children,SELECTION_SIZE)
print(fittestIndex)
#
nextGeneration = createChildren()
crossoverChildren(nextGeneration, children, fittestIndex)


