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
		self.mutation = 0

	def setStr(self):
		for i in range(INPUT_LEN):
			rndChar = random.choice(string.ascii_lowercase)
			# print("rndChar %c is attached to %s"%(rndChar, self.string))
			self.getMutation()
			if(self.mutation == 1):
				# chr(ord(rndChar) + 1)
				if(rndChar != 'z'):
					self.string += chr(ord(rndChar) + 1)
				else :
					self.string += chr(ord(rndChar) - 1)
				print("mutation invoked!")
				self.mutation = 0
			else :
				self.string +=rndChar

	def getMutation(self):
		mlist =[1,0]
		prob = [0.9, 0.1]
		if( np.random.choice(mlist, p=prob) == 0):
			self.mutation = 1
		
	def setFitness(self, _myStr):
		child_str = self.string
		ascii_value=0
		for i in range(len(child_str)):
			# print("%s %s %d"%(child_str, _myStr, i))
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

def evalulateChildren(_children, _myStr,_startIndex=0):
	sumOfFitness = 0
	for i in range(len(_children)): # i : 0~9
		if( (_startIndex ==0 ) or (_startIndex != 0 and i>= _startIndex)):
			_children[i].setStr() 
		_children[i].setFitness(_myStr)
		sumOfFitness += _children[i].fitness
	sumOfProbability = 0 #Defined just for check
	for i in range(len(_children)): # j : 0~9
		_children[i].setProbability(sumOfFitness)
		sumOfProbability += _children[i].probability
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
	# print("rndInt is %d"%rndInt)
	j=0
	for i in range(0,len(_fittestIndex),2):
		newString = _children[_fittestIndex[i]].string[:rndInt] + _children[_fittestIndex[i+1]].string[rndInt:]
		print("newString %s is assign to newGen's %dth index"%(newString,j))
		_nextGeneration[j].string = newString
		j += 1
		# print(j) #newGeneration의 j 번째부터 넣ㅇ면 된다. 

	evalulateChildren(_nextGeneration, myStr, j)
	return _nextGeneration


def evolution(times):
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
# print(fittestIndex)
#
nextGeneration = createChildren()
nextGeneration = crossoverChildren(nextGeneration, children, fittestIndex)

printAttributesOfChildren(nextGeneration)
