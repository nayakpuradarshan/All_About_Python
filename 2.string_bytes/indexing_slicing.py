Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> x='python lerning'
>>> len(x)
14
>>> type(x)
<class 'str'>
>>> x[0]
'p'
>>> x[6]
' '
>>> x[3]
'h'
>>> x[0] == x[-15]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    x[0] == x[-15]
IndexError: string index out of range
>>> x[0] == x[-14]
True
>>> x
'python lerning'
>>> x=[2:]
SyntaxError: invalid syntax
>>> x=[2: ]
SyntaxError: invalid syntax
>>> x=[2:6 ]
SyntaxError: invalid syntax
>>> x[2:6 ]
'thon'
>>> x[2:6 ]
'thon'
>>> x[4:6 ]
'on'
>>> x[0:13 ]
'python lernin'
>>> x[-13:]
'ython lerning'
>>> x[-12:5]
'tho'
>>> 
>>> 
>>> 
