Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>>  x=' '
SyntaxError: unexpected indent
>>> x=' '
>>> x
' '
>>> x=" "
>>> x
' '
>>> x="""

"""
>>> 
>>> x
'\n\n'
>>> x='''

'''
>>> 
>>> x
'\n\n'
>>> x='c'
>>> x
'c'
>>> print(x)
c
>>> print('x')
x
>>> str(x)
'c'
>>> reps(x)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    reps(x)
NameError: name 'reps' is not defined
>>> repr(x)
"'c'"
>>> x
'c'
>>> x='python'
>>> 't' in x
True
>>> 't' in x
True
>>> 'z' in x
False
>>> print(x)
python
>>> len(x)
6
>>> x='test\ntest'
>>> x
'test\ntest'
>>> x="test\ntest"
>>> x
'test\ntest'
>>> x="test \ntest"
>>> x
'test \ntest'
>>> 
>>> 
>>> 
>>> x="darshan"
>>> y="patel"
>>> x+''+y
'darshanpatel'
>>> x+' '+y
'darshan patel'
>>> 'darshan'+'patel'
'darshanpatel'
>>> 'darshan' 'patel'
'darshanpatel'
>>> x="python"
>>> x*5
'pythonpythonpythonpythonpython'
>>> x**5
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x**5
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> x*5
'pythonpythonpythonpythonpython'
>>> x="pytohn"
>>> x="python"
>>> y="perl"
>>> x
'python'
>>> y
'perl'
>>> x, y = y, x
>>> x
'perl'
>>> 
>>> y
'python'
>>> x="10000"
>>> y="20000"
>>> x
'10000'
>>> y
'20000'
>>> x, y = y, x
>>> x
'20000'
>>> y
'10000'
SyntaxError: invalid syntax
>>> 
>>> 
>>> a='a3b#c#d'
>>> a.count('#')
2
>>> a.count('a')
1
>>> a.count('3')
1
>>> a.count('#', 0, 4)
1
>>> 
>>> 
>>> 
>>> a='a#b#c#d$1$2$3'
>>> a.find('1')
8
>>> len(a)
13
>>> a[8]
'1'
>>> a.find('4')
-1
>>> a.index('1')
8
>>> a[8]
'1'
>>> a.index('4')
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    a.index('4')
ValueError: substring not found
>>> a='python'
>>> a
'python'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> a.startswith('p')
True
>>> a.startswith('h')
False
>>> a.endwith('h')
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    a.endwith('h')
AttributeError: 'str' object has no attribute 'endwith'
>>> a.endswith('h')
False
>>> a.endswith('n')
True
>>> import textwrap
>>> dir(textwrap)
['TextWrapper', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_leading_whitespace_re', '_whitespace', '_whitespace_only_re', 'dedent', 'fill', 'indent', 're', 'shorten', 'wrap']
>>> print(textwrap.fill(s, 70))
sxxmmy
>>> print(textwrap.fill(a, 70))
python
>>> print(textwrap.fill(a))
python
>>> print(textwrap.fill(e))
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    print(textwrap.fill(e))
NameError: name 'e' is not defined
>>> s="""  1
	    2
	    3
	"""
>>> print(textwrap.dedent(s))
  1
	    2
	    3

SyntaxError: multiple statements found while compiling a single statement
>>> 
