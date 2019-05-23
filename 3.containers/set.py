Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> a=set('abcd')
>>> type(a)
<class 'set'>
>>> print(a)
{'c', 'a', 'd', 'b'}
>>> L=['apple', 'banana', 'orange', 'graps']
>>> L
['apple', 'banana', 'orange', 'graps']
>>> b=set(L)
>>> b
{'apple', 'orange', 'banana', 'graps'}
>>> c={'apple', 'banana', 'orange', 'graps'}
>>> type(a)
<class 'set'>
>>> type(c)
<class 'set'>
>>> type(b)
<class 'set'>
>>> 
>>> 
>>> 
>>> a = frozenset('abc')
>>> a
frozenset({'c', 'a', 'b'})
>>> type(a)
<class 'frozenset'>
>>> 
>>> 
>>> a.add('z')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.add('z')
AttributeError: 'frozenset' object has no attribute 'add'
>>> a
frozenset({'c', 'a', 'b'})
>>> a=('abcd')
>>> type?(a)
SyntaxError: invalid syntax
>>> type(a)
<class 'str'>
>>> a
'abcd'
>>> a
'abcd'
>>> a=set('abcd')
>>> a
{'c', 'a', 'd', 'b'}
>>> a.add('z')
>>> a
{'z', 'c', 'a', 'd', 'b'}
>>> a
{'z', 'c', 'a', 'd', 'b'}
>>> a.clear()
>>> a
set()
>>> a=set('abcd')
>>> a
{'c', 'a', 'd', 'b'}
>>> a.remove('e')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.remove('e')
KeyError: 'e'
>>> a
{'c', 'a', 'd', 'b'}
>>> a.remove('a')
>>> a
{'c', 'd', 'b'}
>>> a.discard('b')
>>> a
{'c', 'd'}
>>> a.update(b)
>>> a
{'apple', 'd', 'c', 'orange', 'banana', 'graps'}
>>> b
{'apple', 'orange', 'banana', 'graps'}
>>> a
{'apple', 'd', 'c', 'orange', 'banana', 'graps'}
>>> 
>>> 
>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sin
<built-in function sin>
>>> math.sin(10)
-0.5440211108893698
>>> mah.cos(10)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    mah.cos(10)
NameError: name 'mah' is not defined
>>> math.cos(10)
-0.8390715290764524
>>> math.log10(10)
1.0
>>> math.factorial(5)
120
>>> math.factorial(3)
6
>>> math.factorial(4)
24
>>> import random
>>> random.seed(10)
>>> random
<module 'random' from 'C:\\Python34\\lib\\random.py'>
>>> random.random
<built-in method random of Random object at 0x00000000032910B8>
>>> random.random()
0.5714025946899135
>>> random.random(10)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    random.random(10)
TypeError: random() takes no arguments (1 given)
>>> random.random()
0.4288890546751146
>>> random.randint(10, 100)
83
>>> random.randrange(10)
0
>>> random.randrange(10)
3
>>> random.randrange(10)
7
>>> random.randrange(10)
7
>>> random.randrange(10)
4
>>> random.randrange(10, 100)
93
>>> random.randrange(10, 100)
30
>>> random.randint(10, 100)
14
>>> random.randint(10, 100)
76
>>> random.randint(10, 100)
72
>>> random.randint(10, 100)
51
>>> dir(random.randint)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> random.randint(10, 20)
11
>>> random.randint(10, 20)
13
>>> random.randint(10, 20)
15
>>> random.randint(10, 20)
10
>>> random.randint(10, 20)
16
>>> random.ranrange(10, 20)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    random.ranrange(10, 20)
AttributeError: 'module' object has no attribute 'ranrange'
>>> random.ranrange(10, 20, 3)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    random.ranrange(10, 20, 3)
AttributeError: 'module' object has no attribute 'ranrange'
>>> random.randrange(50)
8
>>> random.randrange(50)
38
>>> random.randrange(50)
22
>>> random.randrange(50)
24
>>> random.randrange(10, 100, 2)
62
>>> random.randrange(10, 100, 2)
46
>>> random.randrange(10, 100, 2)
96
>>> random.randrange(10, 100, 2)
42
>>> random.randrange(10, 100, 1)
68
>>> random.randrange(10, 100, 1)
32
>>> random.randrange(10, 100, 1)
97
>>> a = [1, 2, 9, 'c', 'e', 1.1]
>>> a
[1, 2, 9, 'c', 'e', 1.1]
>>> type(a)
<class 'list'>
>>> randdom.choice(a)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    randdom.choice(a)
NameError: name 'randdom' is not defined
>>> random.choice(a)
9
>>> random.choice(a)
1.1
>>> random.choice(a)
9
>>> random.choice(a)
2
>>> random.shuffle(a)
>>> random.shuffle(a)
>>> 
>>> 
>>> 
>>> 
