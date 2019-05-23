Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> [i for i in range(5, 10)]
[5, 6, 7, 8, 9]
>>> [i for i in range(10, 20)]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> [chr(i) for i in range(65, 70)]
['A', 'B', 'C', 'D', 'E']
>>> for i in range(65, 70):
	print(chr(i))

	
A
B
C
D
E
>>> for i in range(5, 10):
	print(i)

	
5
6
7
8
9
>>> for i in range(10, 20):
	print(i)

	
10
11
12
13
14
15
16
17
18
19
>>> for i in range(65, 75):
	print(chr(i))

	
A
B
C
D
E
F
G
H
I
J
>>> for x in range(5):
	if x % 2 == 0:
		print(x, y)

		
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    print(x, y)
NameError: name 'y' is not defined
>>> for x in range(5):
	if x % 2 == 0:
		print(x, y)
for y in range(5):
	
SyntaxError: invalid syntax
>>> for x in range(5):
	if x % 2 == 0:
		print(x, y)
for y in range(5):
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> list(map(ord, 'spam'))
[115, 112, 97, 109]
>>> [ord(i) for i in 'spam']
[115, 112, 97, 109]
>>> 
>>> 
>>> {i+i:i for i in range(10)}
{0: 0, 16: 8, 2: 1, 4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 18: 9, 14: 7}
>>> D = {'a': 1, 'b': 2, 'a': 111, 'b': 222, 'f': 111, 'g': 174}
>>> D
{'a': 111, 'g': 174, 'f': 111, 'b': 222}
>>> {k.lower():D.get(k.lower(), 0) + D.get(k.upper(), a) for k in d.keys()}
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    {k.lower():D.get(k.lower(), 0) + D.get(k.upper(), a) for k in d.keys()}
NameError: name 'd' is not defined
>>> 
>>> 
>>> 
>>> {x + 1 for x in [11, 22, 33, 44, 44]}
{34, 12, 45, 23}
>>> 
