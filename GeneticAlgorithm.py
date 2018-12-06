import random
import string
import numpy as np
POOL_SIZE = 20
'''
Genetic Algorithm


'''
class Child:
	def __init__(self,_index):
		self.index = _index
		self.string= ""


	def getStr(self):
		for i in range(10):
			rndChar = random.choice(string.ascii_lowercase)
			self.string +=rndChar
		return self.string
	def setFitness(self, _fitness):
		self.fitness = _fitness
		return 0
	def getFitness(self):
		return self.fitness
	def setProbability(self,_sumOfFitness):
		self.probability = self.fitness/_sumOfFitness
	def getProbability(self):
		return self.probability

#Get Input String from user.
print("== Please enter myStr ==")
myStr = input()
print("========================",end="\n\n")


#Create an Child class array of size POOL_SIZE
children = []
for i in range(POOL_SIZE):	
	children.append(Child(i))
child1 = Child(1)
print("== Generated children ==")
for i in range(len(children)):
	print("index %d is %s\t" %(i, children[i].getStr()),end="")
	if( i%4 == 3):
		print("\n")
print("========================",end="\n\n")

#Calculate fitness and Probability
sumOfMyStr = 0
for k in range(len(myStr)):				
	sumOfMyStr += ord(myStr[k])-97
fienessOfMyStr = sumOfMyStr/len(myStr)


for i in range(len(children)):
	rndStr = children[i].getStr()
	sumOfAscii = 0
	sumOfFitness = 0
	for j in range(len(rndStr)):
		sumOfAscii += ord(rndStr[j])-97 # rndChar - 'a'
		sumOfFitness +=float(sumOfAscii)/len(rndStr)
	children[i].setFitness(sumOfAscii/len(rndStr))
	children[i].setProbability(sumOfFitness)

#print fitness
print("== Calculated fitness ==")
print("%s is %d"%(myStr,fienessOfMyStr))
for i in range(len(children)):
	print("index %d is %d\t" %(i, children[i].getFitness()),end="")
	if( i%4 == 3):
		print("\n")
print("========================",end="\n\n")

#print probability
print("== Calculated Probability ==")
print("%s is %d"%(myStr,fienessOfMyStr))
for i in range(len(children)):
	print("index %d is %f\t" %(i, children[i].getProbability()),end="")
	if( i%4 == 3):
		print("\n")
print("========================",end="\n\n")

#Select the fittest genes
	
fittest = []
for i in range(len(children)):
	fittest.append(children[i].getProbability())
value = np.random.choice(list(range(POOL_SIZE)), p=fittest)
print(value)


