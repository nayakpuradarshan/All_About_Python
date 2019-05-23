Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> def count_down(value):
	for i in range(value, 0, -1):
		yield i

		
>>> c = count_down(5)
>>> next(c)
5
>>> next(c)
4
>>> next(c)
3
>>> next(c)
2
>>> next(c)
1
>>> next(c)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    next(c)
StopIteration
>>> exp Show_upper():
	
SyntaxError: invalid syntax
>>> def Show_upper():
	while True:
		text = yield
		print(text.upper())

		
>>> 
>>> s = Show_upper()
>>> s.send("darshan")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.send("darshan")
TypeError: can't send non-None value to a just-started generator
>>> 
>>> next(s)
>>> s.send("darshan")
DARSHAN
>>> 
>>> 
>>> def init_cor(fun()):
	
SyntaxError: invalid syntax
>>> def init_cor(fun)):
	
SyntaxError: invalid syntax
>>> def init_cor(fun):
	def init(*args, **kwargs):
		gen = func(*args, **kwargs)
		next(gen)
		return gen
	return init

>>> s = Show_upper()
>>> s.send("hello")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.send("hello")
TypeError: can't send non-None value to a just-started generator
>>> def init_cor(fun):
	def init(*args, **kwargs):
		gen = func(*args, **kwargs)
		next(gen)
		return gen
	return init
def Show_upper():
	
SyntaxError: invalid syntax
>>> def init_cor(fun):
	def init(*args, **kwargs):
		gen = func(*args, **kwargs)
		next(gen)
		return gen
	return init
	def Show_upper():
		while True():
			text = yield
			print(text.upper())

			
>>> s = Show_upper()
>>> s.send("hello")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.send("hello")
TypeError: can't send non-None value to a just-started generator
>>> 
>>> res = s.send("python")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    res = s.send("python")
TypeError: can't send non-None value to a just-started generator
>>> s.close()
>>> res = s.send('perl')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    res = s.send('perl')
StopIteration
>>> 
>>> 
>>> def fibonacci(n):
	a = b = 1
	for i in range(n):
		yield a
		a, b = b, a + b

		
>>> 
>>> for i in fibonacci(1):
	print(1)

	
1
>>> 
>>> def grep(pat):
	while True:
		line = yield
		if  pat in line:
			print(line)

			
>>> search = grep('test')
>>> next(search)
>>> search,send('py desting')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    search,send('py desting')
NameError: name 'send' is not defined
>>> search.send('py desting')
>>> 
