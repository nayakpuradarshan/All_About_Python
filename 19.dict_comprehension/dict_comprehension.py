Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> {i+i:i for i in range(10)}
{0: 0, 16: 8, 2: 1, 4: 2, 6: 3, 8: 4, 10: 5, 12: 6, 18: 9, 14: 7}
>>> D = {'a': 1, 'b': 2, 'A': 111, 'B': 222, 'F': 111,  'G': 174}
>>> {k.lower(): D.get(k.lower(), 0) + D.get(k.upper(), 0) for k in D.keys()}
{'b': 224, 'g': 174, 'a': 112, 'f': 111}
>>> 
