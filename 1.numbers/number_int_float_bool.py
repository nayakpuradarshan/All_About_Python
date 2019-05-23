Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> a = 0*a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = 0*a
NameError: name 'a' is not defined
>>> a = 10
>>> a = 0*a
>>> a
0
>>> a = ob100
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a = ob100
NameError: name 'ob100' is not defined
>>> a = 10
>>> hex(a)
'0xa'
>>> oct(a)
'0o12'
>>> 
>>> bin(a)
'0b1010'
>>> a = 10
>>> hex(a)
'0xa'
>>> 
>>> 
>>> a = 10
>>> hex(a)
'0xa'
>>> 
>>> 
>>> a = 4
>>> oct(a)
'0o4'
>>> bin()a
SyntaxError: invalid syntax
>>> bin(a)
'0b100'
>>> 
>>> 
>>> a = 64
>>> oct(a)
'0o100'
>>> 
>>> 
>>> 
>>> a = 9 , b= 2
SyntaxError: can't assign to literal
>>> q
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> a
64
>>> a = 9
>>> b = 2
>>> a + b
11
>>> a - b
7
>>> a / b
4.5
>>> a * b
18
\
>>> a * b
18
>>> a ** b
81
>>> a // b
4
>>> a % b
1
>>> -a
-9
>>> --a
9
>>> ---a
-9
>>> +a
9
>>> 
>>> 
>>> a = 9
>>> b = 2
>>> a < b
False
>>> a <= 2
False
>>> a > 2
True
>>> a >= 2
True
>>> a == 2
False
>>> a != 2
True
>>> a<a<10
False
>>> 0<2<10
True
>>> 0 <= a <= 10
True
>>> 
>>> 
>>> 
>>> a << 2
36
>>> a
9
>>> 1001 >> 1
500
>>> a
9
>>> b
2
>>> a += b
>>> a
11
>>> a -= b
>>> a
9
>>> a *=
SyntaxError: invalid syntax
>>> a *= b
>>> a
18
>>> a /= b
>>> a
9.0
>>> a %= b
>>> a
1.0
>>> a = 9
>>> b= 2
>>> a ** b
81
>>> a !=
SyntaxError: invalid syntax
>>> a != b
True
>>> a &= b
>>> a
0
>>> a ^= b
>>> a
2
>>> a <<= b
>>> a
8
>>> a >>= b
>>> a
2
>>> not a
False
>>> a or b
2
>>> a and b
2
>>> a == b, a is b
(True, True)
>>> a is not b
False
>>> 
>>> 
>>> 
>>> a = 1
>>> 1
1
>>> type(a)
<class 'int'>
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> bool(a)
True
>>> 
>>> 
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
>>> round(11.152)
11
>>> round(11.152, 1)
11.2
>>> round(11.152, -1)
10.0
>>> abs(-10)
10
>>> pow(2,3)
8
>>> pow(2, 3, 2)
0
>>> 
>>> 
>>> 
>>> a = set('abc')
>>> 
>>> a
{'a', 'b', 'c'}
>>> b = set('bcd')
>>> a | b
{'b', 'd', 'a', 'c'}
>>> a & b
{'b', 'c'}
>>> a - b
{'a'}
>>> b - a
{'d'}
>>> 'b' in a
True
>>> 'z' in a
False
>>> 
