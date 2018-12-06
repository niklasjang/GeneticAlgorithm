import random
import string
import numpy as np
POOL_SIZE = 10
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
		for i in range(10):
			rndChar = random.choice(string.ascii_lowercase)
			self.string +=rndChar

	def setFitness(self):
		my_str = self.string
		ascii_value=0
		for i in range(len(my_str)):
			ascii_value += ord(my_str[i])-97   # Char - 'a'
		self.fitness =float(ascii_value)/len(my_str)
	
	def setProbability(self,_sumOfFitness):
		self.probability = self.fitness/_sumOfFitness

	


def createChildren():
	#Create an Child class array of size POOL_SIZE
	children = []
	for i in range(POOL_SIZE):	
		children.append(Child(i))
	return children

def evalulateChildren(_children):
	sumOfFitness = 0
	for i in range(len(children)): # i : 0~9
		children[i].setStr()
		children[i].setFitness()
		sumOfFitness += children[i].fitness
	sumOfProbability = 0 #Defined just for check
	for i in range(len(children)): # j : 0~9
		children[i].setProbability(sumOfFitness)
		sumOfProbability += children[i].probability
		# print("%d'th sumOfProbability is %f" % (i,sumOfProbability))
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


#Get Input String from user.
print("== Please enter myStr ==")
myStr = input()

#Evaluate myStr
my_ascii_value = 0
for k in range(len(myStr)):				
	my_ascii_value += ord(myStr[k])-97
my_fitness= my_ascii_value/len(myStr)
print("%s's fitness is \t%f"%(myStr, my_fitness))
print("========================",end="\n\n")



#Create and Evaluate Chilren
children = createChildren()
evalulateChildren(children)

#Check Attributes
printAttributesOfChildren(children)

#Select the fittest genes list size of N
fittest = []
fittest = getFittestGenes(children,5)

for i in fittest:
	print (children[i].string)


