Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 

>>> a, b =5, 5
>>> a
5
>>> b
5
>>> id(a)
1865668848
>>> id(b)
1865668848
>>> a==b, a is b
(True, True)
>>> a==b
True
>>> a is b
True
>>> a, b= 256, 256
>>> id(a)
1865672864
>>> id(b)
1865672864
>>> a==b
True
>>> a is b
True
>>> a, b=1000, 1000
>>> id(a), id(b)
(50979264, 50979248)
>>> a==b, a is b
(True, False)
>>> a=1000
>>> b=a
>>> a==b
True
>>> a is b
True
>>> a, b= 'spam', 'spam'
>>> a==b, a is b
(True, True)
>>> 
>>> 
>>> a, b = 'space', 'space'
>>> a
'space'
>>> b
'space'
>>> a==b, a is b
(True, True)
>>> 
>>> 
>>> a='space'
>>> a
'space'
>>> b= a
>>> a=b, a is b
>>> a
('space', True)
>>> a='test'
>>> a==b, a is b
(False, False)
>>> a, b=(1,2,3), (1,2,3)
>>> a
(1, 2, 3)
>>> b
(1, 2, 3)
>>> a==b, a is b
(True, False)
>>> a=(1,2,3)
>>> b=a
>>> a==b, a is b
(True, True)
>>> a, b=[1,2,3], [1,2,3]
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> a == b
True
>>> a is b
False
>>> a=[1,2,3]
>>> b
[1, 2, 3]
>>> b = a
>>> a == b
True
>>>  a is b
SyntaxError: unexpected indent
>>> a is b
True
>>> a[0]= 6
>>> a==b, a is b
(True, True)
>>> 
>>> 
>>> 
>>> a, b={'a': 1, 'b': 2}, {'a': 1, 'b': 2}
>>> 
>>> a
{'a': 1, 'b': 2}
>>> b
{'a': 1, 'b': 2}
>>> a==b
True
>>> a is b
False
>>> 
a = {'a': 1, 'b': 2}
>>> b=a
>>> a
{'a': 1, 'b': 2}
>>> b
{'a': 1, 'b': 2}
>>> a==b, a is b
(True, True)
>>> a={'a': 1, 'b': 2}
>>> a
{'a': 1, 'b': 2}
>>> b= a
>>> a==b, a is b
(True, True)
>>> a['c']=123
>>> a==b, a is b
(True, True)
>>> 
>>> 
>>> a, b={1,2,30}, {1,2,3}
>>> a == b, a is b
(False, False)
>>> a= {1,2,3}
>>> b = a
>>> a==b, a is b
(True, True)
>>> 
>>> 
>>> 
>>> a, b=frozenset('234'), frozenset('2,3,4')
>>> a == b
False
>>> 
>>> a
frozenset({'2', '3', '4'})
>>> b['234']
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    b['234']
TypeError: 'frozenset' object is not subscriptable
>>> a, b
(frozenset({'2', '3', '4'}), frozenset({'2', '4', ',', '3'}))
>>> a, b=(frozenset({'2', '3', '4'}), frozenset({'2', '3', '4'}))
>>> a
frozenset({'2', '3', '4'})
>>> b
frozenset({'2', '3', '4'})
>>> a == b
True
>>> a=frozenset('234')
>>> a
frozenset({'2', '3', '4'})
>>> b = a
>>> a == b
True
>>> a is b
True
>>> 
