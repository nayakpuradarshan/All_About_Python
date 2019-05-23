Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t=tuple()
>>> type(t)
<class 'tuple'>
>>> bool(t)
False
>>> t = (1, 2, 's', (1, 2, [1, 2, 4, [1, 2, 3, {1, 2, 3}]]))
>>> type(t)
<class 'tuple'>
>>> len(t)
4
>>> type(t[0])
<class 'int'>
>>> type(t[0]), type(t[1]), type(t[2]), type(t[3]), type(t[4])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    type(t[0]), type(t[1]), type(t[2]), type(t[3]), type(t[4])
IndexError: tuple index out of range
>>> type(t[4])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type(t[4])
IndexError: tuple index out of range
>>> type(t[3])
<class 'tuple'>
>>> type(t[-1][-1][-1][-1])
<class 'set'>
>>> a = tuple(t[-1][-1][-1][-1])
>>> type(a)
<class 'tuple'>
>>> t[0] = 'python'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t[0] = 'python'
TypeError: 'tuple' object does not support item assignment
>>> t1 = (1, 2, 3)
>>> t2 = (4, 5, 6)
>>> t1 + t2
(1, 2, 3, 4, 5, 6)
>>> t2 + t1
(4, 5, 6, 1, 2, 3)
>>> t1
(1, 2, 3)
>>> t1 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> (t1) * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> [t1] * 3
[(1, 2, 3), (1, 2, 3), (1, 2, 3)]
>>> t1.count(1)
1
>>> t1.index(11)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t1.index(11)
ValueError: tuple.index(x): x not in tuple
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t = (1, 2, 3, (1, 2, 9), (1, 6, 7))
>>> t
(1, 2, 3, (1, 2, 9), (1, 6, 7))
>>> for i in t:
	print(i)

	
1
2
3
(1, 2, 9)
(1, 6, 7)
>>> a, b, c, d = t
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a, b, c, d = t
ValueError: too many values to unpack (expected 4)
>>> a, -, -, d = t
SyntaxError: invalid syntax
>>> a, -, *b = t
SyntaxError: invalid syntax
>>> 
>>> 
>>> x = (140)
>>> x
140
>>> type(x)
<class 'int'>
>>> y= tuple(x)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    y= tuple(x)
TypeError: 'int' object is not iterable
>>> y = (140, )
>>> type(y)
<class 'tuple'>
>>> a m= 10
SyntaxError: invalid syntax
>>> a = 10
>>> type(a)
<class 'int'>
>>> d = 100
>>> type(d)
<class 'int'>
>>> a = tuple(20)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a = tuple(20)
TypeError: 'int' object is not iterable
>>> a1 = tuple(20)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a1 = tuple(20)
TypeError: 'int' object is not iterable
>>> t = tuple(10, 20, 30)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    t = tuple(10, 20, 30)
TypeError: tuple() takes at most 1 argument (3 given)
>>> t = tuple(10)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t = tuple(10)
TypeError: 'int' object is not iterable
>>> t = (120)
>>> type(t)
<class 'int'>
>>> t = (120, )
>>> type(t)
<class 'tuple'>
>>> t = tuple(120)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t = tuple(120)
TypeError: 'int' object is not iterable
>>> t = tuple('120')
>>> t
('1', '2', '0')
>>> 
