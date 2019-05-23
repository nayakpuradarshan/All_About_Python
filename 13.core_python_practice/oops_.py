Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> class A:
	def test():
		print("I am A")

		
>>> class B(A):
	def test():
		print("I am B")

		
>>> a = A()
>>> type(a)
<class '__main__.A'>
>>> a.test()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.test()
TypeError: test() takes 0 positional arguments but 1 was given
>>> class A:
	def test(self):
		print("I am A")

		
>>> class B(A):
	def test(test):
		print("I am B")

		
>>> a=A()
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'test']
>>> a.test()
I am A
>>> b = B()
>>> b.test()
I am B
>>> object
<class 'object'>
>>> is
SyntaxError: invalid syntax
>>> isinstance(a, A)
True
>>> isinstance(a, B)
False
>>> isinstance(b, B)
True
>>> 
>>> 
>>> r="harshil"
>>> type(r)
<class 'str'>
>>> isinstance(r, int)
False
\
>>> isinstance(r, 'int')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    isinstance(r, 'int')
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> isinstance(r, int)
False
>>> isinstance(r, sttr)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    isinstance(r, sttr)
NameError: name 'sttr' is not defined
>>> isinstance(r, str)
True
>>> 
>>> 
>>> 
>>> e=(1,2,3)
>>> isinstance(e, tuple)
True
>>> 
>>> issubclass(B, A)
True
>>> issubclass(A, B)
False
>>> issubclass(A, object)
True
>>> issubclass(B, object)
True
>>> dir(A)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'test']
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> 
>>> 
>>> 
>>> mro
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    mro
NameError: name 'mro' is not defined
>>> 
>>> 
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'test']
>>> mro(a)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    mro(a)
NameError: name 'mro' is not defined
>>> A.__mro__
(<class '__main__.A'>, <class 'object'>)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> B
<class '__main__.B'>
>>> A
<class '__main__.A'>
>>> object
<class 'object'>
>>> 
>>> 
>>> B.__mro__
(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> B.harshil()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    B.harshil()
AttributeError: type object 'B' has no attribute 'harshil'
>>> a=(1,2,3)
>>> a.replace(1,2)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.replace(1,2)
AttributeError: 'tuple' object has no attribute 'replace'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> a.count(1)
1
>>> a=[1,2,3]
>>> b=[10,2,3]
>>> a == b
False
>>> a > b
False
>>> a=[20,2,3]
>>> b=[10,2,3]
>>> a > b
True
>>> a=[20,1,3]
>>> a > b
True
>>> a
[20, 1, 3]
>>> b
[10, 2, 3]
>>> a > b
True
>>> result=True
>>> index=0
>>> for v in a:
	if v < b[i]:
		result=False
	index+=1

	
Traceback (most recent call last):
  File "<pyshell#93>", line 2, in <module>
    if v < b[i]:
NameError: name 'i' is not defined
>>> for v in a:
	if v < b[indext]:
		result=False
	index+=1

	
Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    if v < b[indext]:
NameError: name 'indext' is not defined
>>> for v in a:
	if v < b[index]:
		result=False
	index+=1

	
>>> result
False
>>> a
[20, 1, 3]
>>> b
[10, 2, 3]
>>> index=0
>>> a[index] < b[index]
False
>>> 20 < 10
False
>>> 
>>> 
>>> index=0
>>> result=True
>>> for v in a:
	if v < b[index]:
		result=False
	index+=1

	
>>> result
False
>>> 20 < 10
False
>>> if 20 < 10:
	print(" hello")

	
>>> if 20 < 21:
	print(" hello")

	
 hello
>>> 
>>> 
>>> 
>>> a=[10,20,30]
>>> b=[1,2,3]
>>> indec=0
>>> index=0
>>> result=True
>>> for v in a:
	if v < b[index]:
		result=False
	index+=1

	
>>> result
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class A(int):
	pass

>>> a = A(10)
>>> a
10
>>> type(a)
<class '__main__.A'>
>>> a
10
>>> a + 10
20
>>> die(a)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    die(a)
NameError: name 'die' is not defined
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> a.__add__(10)
20
>>> class A(int):
	def __add__(self, other):
		return self + other

	
>>> a=A(10)
>>> 
>>> 
>>> 
>>> class A(int):
	def __add__(self, other):
		return super().__add__(other)

	
>>> a = A(10)
>>> a + 10
20
>>> class A(int):
	def __add__(self, other):
		return super().__add__(other) + 10

	
>>> a = A(10)
>>> a + 10
30
>>> 
>>> 
>>> a=A(10)
>>> a + 10
30
>>> return self + value + 10
SyntaxError: 'return' outside function
>>> 
>>> 
