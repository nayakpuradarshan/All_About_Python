Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> list(filter x: x > 0, range(-5, 5))
SyntaxError: invalid syntax
>>> list(filter(lambda x: x > 0, range(-5, 5)))
[1, 2, 3, 4]
>>> list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
[0, 4, 16, 36, 64]
>>> 
