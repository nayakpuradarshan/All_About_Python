Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> '{} {} {]'.format(123, 5, [1,2,3])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    '{} {} {]'.format(123, 5, [1,2,3])
ValueError: expected '}' before end of string
>>> '{} {} {]'.format(123, '5', [1,2,3])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    '{} {} {]'.format(123, '5', [1,2,3])
ValueError: expected '}' before end of string
>>> '{} {} {]'.format(123, 's', [1,2,3])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    '{} {} {]'.format(123, 's', [1,2,3])
ValueError: expected '}' before end of string
>>> double()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    double()
NameError: name 'double' is not defined
>>> def double():
	pass

>>> 
>>> doubke
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    doubke
NameError: name 'doubke' is not defined
>>> double
<function double at 0x035BDA08>
>>> double()
>>> def double():
	return 4 * 2

>>> double
<function double at 0x035BDA98>
>>> double()
8
>>> 
>>> 
>>> 
>>> 
>>> '{ } { } { }'.format(123, '5', [1,2,3])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    '{ } { } { }'.format(123, '5', [1,2,3])
KeyError: ' '
>>> '{0} {1} {2}'.format(123, '5', [1,2,3])
'123 5 [1, 2, 3]'
>>> '{2} {1} {0}'.format(123, '5', [1,2,3])
'[1, 2, 3] 5 123'
>>> '{1} {2} {0}'.format(123, '5', [1,2,3])
'5 [1, 2, 3] 123'
>>> '{}{}{}'.format(a='aaa', b='bbb', c='ddd')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    '{}{}{}'.format(a='aaa', b='bbb', c='ddd')
IndexError: tuple index out of range
>>> '{a}{b}{c}'.format(a='aaa', b='bbb', c='ddd')
'aaabbbddd'
>>> '{a} {b} {c}'.format(a='aaa', b='bbb', c='ddd')
'aaa bbb ddd'
>>> 
>>> 
>>> L=[1,2,3,4]
>>> '{0},{1}'.format(L)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    '{0},{1}'.format(L)
IndexError: tuple index out of range
>>> '{0},{1}'.format(*L)
'1,2'
>>> '{0},{1},{2},{3}'.format(*L)
'1,2,3,4'
>>> '{0},{1},{2},{3}'.format(*L)
'1,2,3,4'
>>> '{0},{1}'.format(*L)
'1,2'
>>> D={'a':11, 'b':22, 'c':33}
>>> '{} {}'.format(*d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    '{} {}'.format(*d)
NameError: name 'd' is not defined
>>> '{} {}'.format(*D)
'a b'
>>> '{a} {b}'.format(*D)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    '{a} {b}'.format(*D)
KeyError: 'a'
>>> 
>>> 
>>> '{a} {b}'.format(**D)
'11 22'
>>> '{a} {b}'.format(**D)
'11 22'
>>> 

>>> L=[11, 22, 33]
>>> '{1} {3}'.format(*L)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    '{1} {3}'.format(*L)
IndexError: tuple index out of range
>>> '{1} {2}'.format(*L)
'22 33'
>>> '{0} {1}'.format(L, 99)
'[11, 22, 33] 99'
>>> 
>>> '{0[0]} {0[2]}'.format(L)
'11 33'
>>> '{0[0]} != {0[2]}'.format(L)
'11 != 33'
>>> '{0[0]} = {0[2]}'.format(L)
'11 = 33'
>>> '{0[0]} != {0[2]}'.format(L)
'11 != 33'
>>> 
>>> 
>>> D={'first':'darshan', 'last':'patel'}
>>> '{p[first]} {p[last]}'.format(p=D)
'darshan patel'
>>> '{p[first]} {p[first]}'.format(p=D)
'darshan darshan'
>>> '{p[last]} {p[first]}'.format(p=D)
'patel darshan'
>>> 
>>> 
>>> '{}{}'.format(11,22,33,00,'dd')
'1122'
>>> '{1}{d}'.format(11,22,33,00,'dd')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    '{1}{d}'.format(11,22,33,00,'dd')
KeyError: 'd'
>>> '{1}{d}'.format(11,22,3.00,'dd')
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    '{1}{d}'.format(11,22,3.00,'dd')
KeyError: 'd'
>>> '{1:d}'.format(11,22,3.00,'dd')
'22'
>>> '{1:f}'.format(11,22,33.00,'d')
'22.000000'
>>> '{1:f}'.format(11,22,33.00,'dd')
'22.000000'
>>> '{1:f}'.format(11,22,3.00,'dd')
'22.000000'
>>> 
>>> 
>>> '{}'.format(64,65,33.00,'dd')
'64'
>>> '{1:c}'.format(64,65,33.00,'dd')
'A'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> '{1:0}'.format(164,64)
'64'
>>> '{1:x} {1:x}'.format(11,10)
'a a'
>>> '{1:x} {1:X}'.format(11,10)
'a A'
>>> '{0:1}'.format(164,64)
'164'
>>> '{1:0}'.format(164,64)
'64'
>>> '{0:b}'.format(10)
'1010'
>>> '{0:e}'.format(10)
'1.000000e+01'
>>> '{0:e}'.format(10)
'1.000000e+01'
>>> 
>>> 
>>> '{0:f}, {0:2f}, {0:+.2f}'.format(11.111)
'11.111000, 11.111000, +11.11'
>>> a='python'
>>> '{:<30}'.format(a)
'python                        '
>>> '{:>30}'.format(a)
'                        python'
>>> '{:^30}'.format(a)
'            python            '
>>> '{:.<30}'.format(a)
'python........................'
>>> '{:.>30}'.format(a)
'........................python'
>>> '{:.^30}'.format(a)
'............python............'
>>> 
>>> 
>>> '{:3}'.format('python')
'python'
>>> '{:.3}'.format('python')
'pyt'
>>> '{:1.3}'.format('python')
'pyt'
>>> '{:3.1}'.format('python')
'p  '
>>> '{:4d}'.format(42)
'  42'
>>> '{:06.2f}'.format(3.111111)
'003.11'
>>> '{:+d}'.format(42)
'+42'
>>> 
>>> 
>>> '{: d}'.format(42)
' 42'
>>> '{: d}'.format(-42)
'-42'
>>> 
>>> 
>>> '{:=5d}'.format(-42)
'-  42'
>>> '{:=3d}'.format(-42)
'-42'
>>> 
