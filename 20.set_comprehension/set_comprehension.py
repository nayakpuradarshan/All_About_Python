Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> {x+1 for x in [11, 22, 33, 44, 44]}
{34, 12, 45, 23}
>>> for line in open('a.txt')
SyntaxError: invalid syntax
>>> """for line in open('a.txt'):
	uppers = [line.uppers() for line in open('a.txt')]
	list(map(str.upper, open('a.txt')))
	"""
