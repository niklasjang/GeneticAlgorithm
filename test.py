import random
import string
mstr = "abc"
for i in range(10):
	rndChar = random.choice(string.ascii_lowercase)
	print(rndChar)
	print (chr(ord(rndChar) + 1))
