#!usr/bin/env python
"""
countVowels.py
Insert an input then count the vowels, then report how many of each vowels
"""

A = 0
I = 0
U = 0
E = 0
O = 0

string = input("Insert a string: ")

for char in string:
	if char == "A" or "a":
		A+=1
	elif char == "I" or "i":
		I+=1
	elif char == "U" or "u":
		U+=1
	elif char == "E" or "e":
		E+=1
	elif char == "O" or "o":
		O+=1
	else:
		pass

print("A = "+str(A))
print("I = "+str(I))
print("U = "+str(U))
print("E = "+str(E))
print("O = "+str(O))