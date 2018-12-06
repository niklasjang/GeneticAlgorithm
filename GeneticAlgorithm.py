import random
import string

POOL_SIZE = 10
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

#Get Input String from user.
print("Please enter myStr>> ",end="")
myStr = input()
print("Entered str is %s\n" % myStr)

#Create an Child class array of size POOL_SIZE
children = []
for i in range(POOL_SIZE):	
	children.append(Child(i))
child1 = Child(1)
print("== Generated children ==")
for i in range(len(children)):
	print("index %d is %s" %(i, children[i].getStr()))
print("========================",end="\n\n")

#Calculate 
print("calculate")

