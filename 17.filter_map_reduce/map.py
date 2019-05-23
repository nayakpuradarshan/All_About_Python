Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> def test(n):
	return n ** 2

>>> L = [1, 2, 3, 4, 5]
>>> type(L)
<class 'list'>
>>> list(map(test, L))
[1, 4, 9, 16, 25]
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> 
>>> 
>>> def test(n, m):
	return n ** m

>>> L = [1, 2, 3, 4, 5]
>>> L1 = [3] * 5
>>> list(map(test, L, L1))
[1, 8, 27, 64, 125]
>>> 
>>> 
>>> L = [1, 2, 3, 4, 5]
>>> L1 = [2] * 4
>>> list(map(test, L, L1))
[1, 4, 9, 16]
>>> L = [1, 2, 3, 4, 5]
>>> L1 = [2] * 5
>>> list(map(test, L, L1))
[1, 4, 9, 16, 25]
>>> L1 = [2] * 3
>>> list(map(test, L, L1))
[1, 4, 9]
>>> 
>>> 
>>> 
>>> pow(3, 4)
81
>>> pow(2, 5)
32
>>> list(map(pow, [1, 2, 3], [1, 2, 3]))
[1, 4, 27]
>>> 
>>> 
>>> list(map(pow, [1, 2, 3]))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(map(pow, [1, 2, 3]))
TypeError: pow expected at least 2 arguments, got 1
>>> list(map([1, 2, 3]))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(map([1, 2, 3]))
TypeError: map() must have at least two arguments.
>>> def add(x):
	return x + x
def mud(x):
	
SyntaxError: invalid syntax
>>> def add(x):
	return x + x
    def mud(x):
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
