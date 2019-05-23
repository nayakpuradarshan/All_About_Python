Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> x = lambda x, y: x + y
>>> x (11, 22)
33
>>> type(x)
<class 'function'>
>>> x = lambda a='xyz', b='pqr', c='abc': a+b+c
>>> x()
'xyzpqrabc'
>>> def test():
	title = 'hello'
	acbm = lambda x: title+' '+x
	return action

>>> 
>>> a = test()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a = test()
  File "<pyshell#10>", line 4, in test
    return action
NameError: name 'action' is not defined
>>> a('harshil')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a('harshil')
NameError: name 'a' is not defined
>>> a = test()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = test()
  File "<pyshell#10>", line 4, in test
    return action
NameError: name 'action' is not defined
>>> L = [lambda x: x ** 2],
>>> L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]
>>> 
>>> for x in L:
	print(f(1))

	
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    print(f(1))
NameError: name 'f' is not defined
>>> a = lambda x: lambda y = y + x
SyntaxError: invalid syntax
>>> a (11)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a (11)
NameError: name 'a' is not defined
>>> a(11)(22)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a(11)(22)
NameError: name 'a' is not defined
>>> a = lambda x: lambda x=x+y
SyntaxError: invalid syntax
>>> a = lambda x: lambda x=x+y
SyntaxError: invalid syntax
>>> a(11)a()
SyntaxError: invalid syntax
>>> def test():
	L = []
	for i in range(a):
		L.append(lamda x: i ** x)
		
SyntaxError: invalid syntax
>>> 
