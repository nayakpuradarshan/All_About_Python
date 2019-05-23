Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> 
>>> a="a#b#c#d$1$2$3"
>>> a.split()
['a#b#c#d$1$2$3']
>>> a
'a#b#c#d$1$2$3'
>>> a.split('@')
['a#b#c#d$1$2$3']
>>> a.split('#', 1)
['a', 'b#c#d$1$2$3']
>>> a.split('#', 3)
['a', 'b', 'c', 'd$1$2$3']
>>> a.split('#', '$', 3)
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    a.split('#', '$', 3)
TypeError: split() takes at most 2 arguments (3 given)
>>> a='abcd'
>>> a
'abcd'
>>> type(a)
<class 'str'>
>>> list(a)
['a', 'b', 'c', 'd']
>>> a=['a', 'b', 'c', 'd']
>>> a
['a', 'b', 'c', 'd']
>>> '',join(a)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    '',join(a)
NameError: name 'join' is not defined
>>> ''.join(a)
'abcd'
>>> ' '.join(a)
'a b c d'
>>> "*".join(a)
'a*b*c*d'
>>> 
>>>
