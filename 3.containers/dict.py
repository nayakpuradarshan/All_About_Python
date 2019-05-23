Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> D = {}
>>> type(D)
<class 'dict'>
>>> D = dict()
>>> type(D)
<class 'dict'>
>>> bool(D)
False
>>> D={}
>>> D = {
	'a': 1,
	'b': (1, 2, 3),
	'c': [1, 2, 3,[4, 5,(1, 2)]],
	1: {1, 2, 3, 4},
	2: {'a': 1, 'b': 2},
	(1, 2, 3): {11, 22, 33}
	}
>>> type(D)
<class 'dict'>
>>> type(D), len(D)
(<class 'dict'>, 6)
>>> D.clear()
>>> D
{}
>>> D = {
	'a': 1,
	'b': (1, 2, 3),
	'c': [1, 2, 3,[4, 5,(1, 2)]],
	1: {1, 2, 3, 4},
	2: {'a': 1, 'b': 2},
	(1, 2, 3): {11, 22, 33}
	}
>>> D.keys()
dict_keys(['a', 2, 1, 'b', 'c', (1, 2, 3)])
>>> D.values()
dict_values([1, {'a': 1, 'b': 2}, {1, 2, 3, 4}, (1, 2, 3), [1, 2, 3, [4, 5, (1, 2)]], {33, 11, 22}])
>>> D.items()
dict_items([('a', 1), (2, {'a': 1, 'b': 2}), (1, {1, 2, 3, 4}), ('b', (1, 2, 3)), ('c', [1, 2, 3, [4, 5, (1, 2)]]), ((1, 2, 3), {33, 11, 22})])
>>> D['c']
[1, 2, 3, [4, 5, (1, 2)]]
>>> D['z']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    D['z']
KeyError: 'z'
>>> D['z', 0]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    D['z', 0]
KeyError: ('z', 0)
>>> D['z', o]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    D['z', o]
NameError: name 'o' is not defined
>>> T = D.copy()
>>> T
{'a': 1, 2: {'a': 1, 'b': 2}, 1: {1, 2, 3, 4}, 'b': (1, 2, 3), 'c': [1, 2, 3, [4, 5, (1, 2)]], (1, 2, 3): {33, 11, 22}}
>>> 
>>> 
>>> D = {'a': 'b', 'c': 'd'}
>>> type(D)
<class 'dict'>
>>> 'a' in D
True
>>> 'b' in D
False
>>> 
>>> 
>>> t = (1, 2, 3, (1, 2, 9, (1, 6, 7)))
>>> for i in TL
SyntaxError: invalid syntax
>>> for i in t:
	print(i)

	
1
2
3
(1, 2, 9, (1, 6, 7))
>>> len(t)
4
>>> a, b, c, d, = t
>>> t
(1, 2, 3, (1, 2, 9, (1, 6, 7)))
>>> a
1
>>> b
2
>>> c
3
>>> d
(1, 2, 9, (1, 6, 7))
>>> 
>>> D = {'a': [1, 2, 3],
     'b': 123,
     (1,2,3): 'bcd'
     }
>>> type(D)
<class 'dict'>
>>> D['a'] = 456
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'bcd'}
>>> D[(1,2,3)] = 'cd'
>>> type(D)
<class 'dict'>
>>> D['z'] = 1234
>>> D
{'a': 456, 'z': 1234, 'b': 123, (1, 2, 3): 'cd'}
>>> D
{'a': 456, 'z': 1234, 'b': 123, (1, 2, 3): 'cd'}
>>> D.pop('z')
1234
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D.keys()
dict_keys(['a', 'b', (1, 2, 3)])
>>> D[(1, 2, 3)]
'cd'
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D.pop[(1, 2, 3)]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    D.pop[(1, 2, 3)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D.pop[(1, 2, 3)]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    D.pop[(1, 2, 3)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> D.pop(1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    D.pop(1, 2, 3)
TypeError: pop expected at most 2 arguments, got 3
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D.keys()
dict_keys(['a', 'b', (1, 2, 3)])
>>> D.pop()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    D.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> dir(D)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> D.pop['a']
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    D.pop['a']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> dir(D)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> 
>>> D.pop('zz', 129)
129
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D
{'a': 456, 'b': 123, (1, 2, 3): 'cd'}
>>> D.popitem()
('a', 456)
>>> D
{'b': 123, (1, 2, 3): 'cd'}
>>> D
{'b': 123, (1, 2, 3): 'cd'}
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> 
>>> 
>>> D
{'b': 123, (1, 2, 3): 'cd'}
>>> dir(D)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> D.clear()
>>> D
{}
>>> dir(D)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> D.setdefault('de', 111)
111
>>> D
{'de': 111}
>>> D.clear()
>>> D
{}
>>> D.setdefault('de', 111)
111
>>> D = dict(name = 'harshil', surname = 'patel')
>>> D
{'name': 'harshil', 'surname': 'patel'}
>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D
{'a': 1, 'b': 2, 'c': 3}
>>> D.update(E)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    D.update(E)
NameError: name 'E' is not defined
>>> D
{'a': 1, 'b': 2, 'c': 3}
>>> D.update(E)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    D.update(E)
NameError: name 'E' is not defined
>>> 
>>> L = ['a', 'b', 'c']
>>> :
	
SyntaxError: invalid syntax
>>> L
['a', 'b', 'c']
>>> L1 = [1, 2, 3]
>>> type(L)
<class 'list'>
>>> type(L1)
<class 'list'>
>>> dict(zip(L, L1))
{'a': 1, 'b': 2, 'c': 3}
>>> L = ['a']
>>> L1 = [1, 2]
>>> dict(zip(L, L1))
{'a': 1}
>>> 
>>> dict.fromkeys([1, 2, 3])
{1: None, 2: None, 3: None}
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Returns a new dict with keys from iterable and values equal to value.

>>> 
