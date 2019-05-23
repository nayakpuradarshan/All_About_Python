Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> a, b = 6, 7
>>> 
>>> a
6
>>> b
7
>>> a == 6, b == 7
(True, True)
>>> a == 6, b != 7
(True, False)
>>> a == 6 and b == 7
True
>>> a == 6 and b != 7
False
>>> a == 6 and b != 7
False
>>> bool(a)
True
>>> not a
False
>>> a == 6 or b == 7
True
>>> a == 6 or b != 7
True
>>> a == 6 or b != 9
True
>>> b = 0
>>> bool(b)
False
>>> not a
False
>>> 
>>> 
>>> 
>>> a = 5
>>> if a == 5
SyntaxError: invalid syntax
>>> a = 5
>>> if a == 5:
	print('ok')

	
ok
>>> date = {'perl': 'larry wall',
	'python': 'guido',
	'linux': 'lius'
	}
>>> date.get('perl', "don't' know")
'larry wall'
>>> weight = 85
>>> if weight>80:
	print('fat  ')
	else:
		
SyntaxError: invalid syntax
>>> if weight>80:
	print('fat  ')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> r = True
>>> ("not fat", "fat")[r]
'fat'
>>> r = True
>>> ("not fat", "fat")[r]
'fat'
>>> r = False
>>> ("not fat", "fat")[r]
'not fat'
>>> 
>>> 
>>> 
>>> 
>>> a = 9
>>> if a == 8:
	pass
elif a == 7:
	print('ok')
else:
	print('ok ok ')

	
ok ok 
>>> a = 8
>>> if a == 8:
	pass
elif a == 7:
	print('ok')
else:
	print('ok ok ')

	
>>> 
