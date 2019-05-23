Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> class Test:
	def __init__(self, start):
		self.counter = start + 1
	def __iter__(self):
		return self
	def __next__(self):
		self.count -= 1
		return self.couter

	
>>> a = Test(5)
>>> a
<__main__.Test object at 0x0000000003A40470>
>>> next(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    next(a)
  File "<pyshell#9>", line 7, in __next__
    self.count -= 1
AttributeError: 'Test' object has no attribute 'count'
>>> 
>>> 
>>> next(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    next(a)
  File "<pyshell#9>", line 7, in __next__
    self.count -= 1
AttributeError: 'Test' object has no attribute 'count'
>>> class Test:
	def __init__(self, start):
		self.counter = start + 1
	def __iter__(self):
		return self
	def __next__(self):
		self.counter -= 1
		return self.counter

	
>>> a = Test(5)
>>> a
<__main__.Test object at 0x0000000003A89978>
>>> next(a)
5
>>> next(a)
4
>>> next(a)
3
>>> next(a)
2
>>> next(a)
1
>>> next(a)
0
>>> next(a)
-1
>>> next(a)
-2
>>> i = iter(range(5, 0, -1))
>>> next(i)
5
>>> next(i)
4
>>> next(i)
3
>>> 
>>> 
>>> 
>>> next(i)
2
>>> next(i)
1
>>> next(i)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    next(i)
StopIteration
>>> a = Test(5)
>>> next(a)
5
>>> next(a)
4
>>> next(a)
3
>>> next(a)
2
>>> next(a)
1
>>> next(a)
0
>>> next(a)
-1
>>> import itertools
>>> cycler = itertools.cycle
>>> cycler = itertools.cycle([1, 2, 3])
>>> 
>>> for i in cycler:
	print(i)

	
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
23
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
2
3
1
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    print(i)
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> c = itertools.count(5)
>>> c
count(5)
>>> for i in c:
	print(i)

	
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    print(i)
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
>>> 
>>> r = itertools.repeat(10)
>>> for i in r:
	print(i)

	
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    print(i)
  File "C:\Python34\lib\idlelib\PyShell.py", line 1352, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> list(itertools.repeat(4, 2))
[4, 4]
>>> list(itertools.repeat(4, 20))
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
>>> list(itertools.zip_longest(['a', 'b', 'c'], [1, 2, 3, 4, 5]))
[('a', 1), ('b', 2), ('c', 3), (None, 4), (None, 5)]
>>> list(itertools.zip_longest(['a', 'b', 'c'], [1, 2, 3, 4, 5], filvalue = 111))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(itertools.zip_longest(['a', 'b', 'c'], [1, 2, 3, 4, 5], filvalue = 111))
TypeError: zip_longest() got an unexpected keyword argument
>>> list(itertools.zip_longest(['a', 'b', 'c'], [1, 2, 3, 4, 5], fillvalue = 111))
[('a', 1), ('b', 2), ('c', 3), (111, 4), (111, 5)]
>>> 
>>> list(itertools.chain([1, 2, 3], [4, 5, 6],[7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(iyertools.islice(range(10, 5)))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list(iyertools.islice(range(10, 5)))
NameError: name 'iyertools' is not defined
>>> list(itertools.islice(range(10, 5)))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list(itertools.islice(range(10, 5)))
TypeError: islice expected at least 2 arguments, got 1
>>> list(itertools.islice(range(10), 5)))
SyntaxError: invalid syntax
>>> list(itertools.islice(range(10), 5))
[0, 1, 2, 3, 4]
>>> list(itertools.islice(range(10), 5))
[0, 1, 2, 3, 4]
>>> list(itertools.islice(range(10), 5, 8))
[5, 6, 7]
>>> 
