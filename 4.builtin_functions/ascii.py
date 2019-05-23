Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ascii('a#')
"'a#'"
>>> ascii('b#')
"'b#'"
>>> d = 1
>>> callable(d)
False
>>> def d():
	pass
'
SyntaxError: EOL while scanning string literal
>>> def d():
	pass

>>> 
>>> callable(d)
True
>>> class d:
	pass

>>> callable(d)
True
>>> 
