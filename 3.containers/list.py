Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> L=[]
>>> L=list()
>>> type(L)
<class 'list'>
>>> bool(L)
False
>>> L=[0, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3,[4, 5, 6]], 9]
>>> L
[0, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9]
>>> type(L)
<class 'list'>
>>> L[7], L[6], L[6][1]
(9, [1, 2, 3, [4, 5, 6]], 2)
>>> type(L), type(L[0], type(L[-2]))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type(L), type(L[0], type(L[-2]))
TypeError: type() takes 1 or 3 arguments
>>> type(L), type(L[0]), type(L[-2]))
SyntaxError: invalid syntax
>>> type(L), type(L[0]), type(L[-2])
(<class 'list'>, <class 'int'>, <class 'list'>)
>>> L[0] = 12345
>>> type(L)
<class 'list'>
>>> L
[12345, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9]
>>> L[0:4]
[12345, 1, 1.1, 'a']
>>> len(L)
8
>>> L1=[11, 22, 33]
>>> L
[12345, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9]
>>> L1
[11, 22, 33]
>>> L + L1
[12345, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9, 11, 22, 33]
>>> L1 + L
[11, 22, 33, 12345, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9]
>>> [L] + [L1]
[[12345, 1, 1.1, 'a', 'abc', {'a', 'b'}, [1, 2, 3, [4, 5, 6]], 9], [11, 22, 33]]
>>> 
>>> 
>>> L1 * 3
[11, 22, 33, 11, 22, 33, 11, 22, 33]
>>> [L1] * 3
[[11, 22, 33], [11, 22, 33], [11, 22, 33]]
>>> 
>>> 33 in L1
True
>>> 'a' in L
True
>>> 
>>> L == L1
False
>>> L > L1, L < L1
(True, False)
>>> 
>>> 
>>> L = [9, 8, 7, 6, 4, 9, 1]
>>> for i in L:
	print(I)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    print(I)
NameError: name 'I' is not defined
>>> for i in L:
	print(i)

	
9
8
7
6
4
9
1
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> L.sort()
>>> L
[1, 4, 6, 7, 8, 9, 9]
>>> type(L)
<class 'list'>
>>> len(l)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    len(l)
NameError: name 'l' is not defined
>>> len(L)
7
>>> L[7]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    L[7]
IndexError: list index out of range
>>> L[7] = 9
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    L[7] = 9
IndexError: list assignment index out of range
>>> L.append(9)
>>> L
[1, 4, 6, 7, 8, 9, 9, 9]
>>> L.append(99)
>>> L
[1, 4, 6, 7, 8, 9, 9, 9, 99]
>>> L.append([1, 2, 3, 4])
>>> L
[1, 4, 6, 7, 8, 9, 9, 9, 99, [1, 2, 3, 4]]
>>> L.insert(0, 9)
>>> L
[9, 1, 4, 6, 7, 8, 9, 9, 9, 99, [1, 2, 3, 4]]
>>> 
>>> L.extend('harshil')
>>> L
[9, 1, 4, 6, 7, 8, 9, 9, 9, 99, [1, 2, 3, 4], 'h', 'a', 'r', 's', 'h', 'i', 'l']
>>> L.pop
<built-in method pop of list object at 0x0000000003E506C8>
>>> L.pop()
'l'
>>> L.pop()
'i'
>>> L.pop()
'h'
>>> L.pop()
's'
>>> L.pop()
'r'
>>> L.pop()
'a'
>>> L.pop()
'h'
>>> L.pop()
[1, 2, 3, 4]
>>> L.pop()
99
>>> L
[9, 1, 4, 6, 7, 8, 9, 9, 9]
>>> L.extend('darshan')
>>> L
[9, 1, 4, 6, 7, 8, 9, 9, 9, 'd', 'a', 'r', 's', 'h', 'a', 'n']
>>> L.extend(9)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    L.extend(9)
TypeError: 'int' object is not iterable
>>> 
>>> 
>>> L.clear()
>>> L
[]
>>> L.count(4)
0
>>> L
[]
>>> L=[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L.count(4)
1
>>> L.count()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    L.count()
TypeError: count() takes exactly one argument (0 given)
>>> L.count(1)
1
>>> L.count(1111)
0
>>> L.count(0, 1)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    L.count(0, 1)
TypeError: count() takes exactly one argument (2 given)
>>> L.count(10)
0
>>> help(count)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    help(count)
NameError: name 'count' is not defined
>>> help(list.count)
Help on method_descriptor:

count(...)
    L.count(value) -> integer -- return number of occurrences of value

>>> L.count(l)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    L.count(l)
NameError: name 'l' is not defined
>>> L.count(L)
0
>>> L.count(18)
0
>>> L.count(4)
1
>>> L.reverce()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    L.reverce()
AttributeError: 'list' object has no attribute 'reverce'
>>> L.reverse()
>>> L
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> L.sort()
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L.sort(reverse = True)
>>> L
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> 
>>> L.pop()
1
>>> L.pop(0)
9
>>> L
[8, 7, 6, 5, 4, 3, 2]
>>> L.pop(-1)
2
>>> L
[8, 7, 6, 5, 4, 3]
>>> L.remove('d')
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    L.remove('d')
ValueError: list.remove(x): x not in list
>>> L.remove(0)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    L.remove(0)
ValueError: list.remove(x): x not in list
>>> L
[8, 7, 6, 5, 4, 3]
>>> L.sort()
>>> L
[3, 4, 5, 6, 7, 8]
>>> L=[1, 2, 3, [4, 5, 6]]
>>> L
[1, 2, 3, [4, 5, 6]]
>>> p=L.copy()
>>> p
[1, 2, 3, [4, 5, 6]]
>>> p[0]
1
>>> p[0] = 123
>>> P
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    P
NameError: name 'P' is not defined
>>> p
[123, 2, 3, [4, 5, 6]]
>>> p , L
([123, 2, 3, [4, 5, 6]], [1, 2, 3, [4, 5, 6]])
>>> p[-1][0] = 12
>>> p
[123, 2, 3, [12, 5, 6]]
>>> p, L
([123, 2, 3, [12, 5, 6]], [1, 2, 3, [12, 5, 6]])
>>> 
>>> L=range(4)
>>> L
range(0, 4)
>>> print(L)
range(0, 4)
>>> for i in L:
	print(i)

	
0
1
2
3
>>> for i in L:
	print(i + 1)

	
1
2
3
4
>>> for i in range(11, 22):
	print(i)

	
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
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(1, 5):
	print(i)

	
1
2
3
4
>>> for i in range(0, 101, 2:)
SyntaxError: invalid syntax
>>> for i in range(0, 101, 2):
	print(i)

	
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
>>> for i in range(0, 101, 2):
	print(i)

	
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
>>> for i in range(1, 101, 2):
	print(i)

	
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> type(m)
<class 'list'>
>>> print(m)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> import copy
>>> L = [1, 2, 3, [4, 5, 6]]
>>> L
[1, 2, 3, [4, 5, 6]]
>>> c = copy.copy(L)
>>> c
[1, 2, 3, [4, 5, 6]]
>>> d=L.copy()
>>> d
[1, 2, 3, [4, 5, 6]]
>>> dir(copy)
['Error', 'PyStringMap', '_EmptyClass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_copy_with_constructor', '_copy_with_copy_method', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'builtins', 'copy', 'deepcopy', 'dispatch_table', 'error', 'name', 't', 'weakref']
>>> c=copy.copy(L)
>>> c
[1, 2, 3, [4, 5, 6]]
>>> c[-1][0] = 123
>>> c
[1, 2, 3, [123, 5, 6]]
>>> t = copy.deepcopy(L)
>>> t
[1, 2, 3, [123, 5, 6]]
>>> dir(copy)
['Error', 'PyStringMap', '_EmptyClass', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_copy_dispatch', '_copy_immutable', '_copy_with_constructor', '_copy_with_copy_method', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', 'builtins', 'copy', 'deepcopy', 'dispatch_table', 'error', 'name', 't', 'weakref']
>>> help(copy.copy)
Help on function copy in module copy:

copy(x)
    Shallow copy operation on arbitrary Python objects.
    
    See the module's __doc__ string for more info.

>>> help(copy)
Help on module copy:

NAME
    copy - Generic (shallow and deep) copying operations.

DESCRIPTION
    Interface summary:
    
            import copy
    
            x = copy.copy(y)        # make a shallow copy of y
            x = copy.deepcopy(y)    # make a deep copy of y
    
    For module specific errors, copy.Error is raised.
    
    The difference between shallow and deep copying is only relevant for
    compound objects (objects that contain other objects, like lists or
    class instances).
    
    - A shallow copy constructs a new compound object and then (to the
      extent possible) inserts *the same objects* into it that the
      original contains.
    
    - A deep copy constructs a new compound object and then, recursively,
      inserts *copies* into it of the objects found in the original.
    
    Two problems often exist with deep copy operations that don't exist
    with shallow copy operations:
    
     a) recursive objects (compound objects that, directly or indirectly,
        contain a reference to themselves) may cause a recursive loop
    
     b) because deep copy copies *everything* it may copy too much, e.g.
        administrative data structures that should be shared even between
        copies
    
    Python's deep copy operation avoids these problems by:
    
     a) keeping a table of objects already copied during the current
        copying pass
    
     b) letting user-defined classes override the copying operation or the
        set of components copied
    
    This version does not copy types like module, class, function, method,
    nor stack trace, stack frame, nor file, socket, window, nor array, nor
    any similar types.
    
    Classes can use the same interfaces to control copying that they use
    to control pickling: they can define methods called __getinitargs__(),
    __getstate__() and __setstate__().  See the documentation for module
    "pickle" for information on these methods.

CLASSES
    builtins.Exception(builtins.BaseException)
        Error
    
    class Error(builtins.Exception)
     |  Method resolution order:
     |      Error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    copy(x)
        Shallow copy operation on arbitrary Python objects.
        
        See the module's __doc__ string for more info.
    
    deepcopy(x, memo=None, _nil=[])
        Deep copy operation on arbitrary Python objects.
        
        See the module's __doc__ string for more info.

DATA
    __all__ = ['Error', 'copy', 'deepcopy']

FILE
    c:\python34\lib\copy.py


>>> 
