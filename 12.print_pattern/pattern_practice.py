"""

*
**
***
****
*****
****
***
**
*



for i in range(5):
	
	for j in range(0, i+1):
		print("*", end="")
		
	print()
	

for i in range(4):
	
	for j in range(4-i):
		print("*", end="")
		
	print()
	
"""

"""

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *



times=5

for space in range(times-1, -1, -1):
	print(" " * space + '*' * (times-space))

for space in range(1, times):
	print(" " * space + '*' * (times-space))

"""

"""

a
ab
abc
abcd
abcde

"""







"""

*****
****
***
**
*



for i in range(5):
	
	for j in range(5-i):
		print("*", end="")
		
	print()
	
"""

"""

12345
1234
123
12
1



num=int(input("ENTER THE NUMBER HERE: "))

for i in range(num, -1, -1):

	for j in range(1, i+1):
		print(j, end="")
		
	print()
	
"""

"""

55555
4444
333
22
1



num=int(input("ENTER THE NUMBER HERE: "))

for i in range(num, -1, -1):

	for j in range(1, i+1):
		print(i, end="")
		
	print()
	
"""

"""

		1
	   2 2
	  3 3 3 
	 4 4 4 4
	5 5 5 5 5
	
"""

