Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.random
<built-in method random of Random object at 0x000000000304BB58>
>>> random.random()
0.1794931533646441
>>> random.random()
0.5717005275019533
>>> random.random()
0.9350205273205755
>>> random.random(10)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    random.random(10)
TypeError: random() takes no arguments (1 given)
>>> random.ranrange
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    random.ranrange
AttributeError: 'module' object has no attribute 'ranrange'
>>> random.randrange
<bound method Random.randrange of <random.Random object at 0x000000000304BB58>>
>>> random.randrange(10)
3
>>> random.randrange(10)
3
>>> random.randrange(10)
7
>>> random.randrange(10)
3
>>> random.randrange(10)
9
>>> random.randrange(10)
2
>>> 
>>> random.chice
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    random.chice
AttributeError: 'module' object has no attribute 'chice'
>>> random.choice
<bound method Random.choice of <random.Random object at 0x000000000304BB58>>
>>> random.choice(10)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    random.choice(10)
  File "C:\Python34\lib\random.py", line 253, in choice
    i = self._randbelow(len(seq))
TypeError: object of type 'int' has no len()
>>> random.randint
<bound method Random.randint of <random.Random object at 0x000000000304BB58>>
>>> random.randint(20)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    random.randint(20)
TypeError: randint() missing 1 required positional argument: 'b'
>>> random.randint(20, 40)
33
>>> random.randint(20, 40)
28
>>> random.randint(20, 40)
32
>>> random.randint(20, 40)
32
>>> random.randint(20, 40)
36
>>> 
