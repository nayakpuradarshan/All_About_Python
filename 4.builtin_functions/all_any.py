Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> all([1, 2, 3, 4])
True
>>> all([1, 2, 3, 0])
False
>>> any([1, 2, 3, 4])
True
>>> any([1, 2, 3, 0])
True
>>> all([1, 2, 3, 4, 5, 6, 7])
True
>>> all([1, 2, 3, 4, 5, 9, 7])
True
>>> all([1, 0, 3, 4, 5, 9])
False
>>> any([1, 2, 3, 4, 5, 0, 7, ])
True
>>> 
