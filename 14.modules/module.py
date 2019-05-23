Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> type(math)
<class 'module'>
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> type(math.pi)
<class 'float'>
>>> type(math.sin)
<class 'builtin_function_or_method'>
>>> math.pi
3.141592653589793
>>> math.sqrt(9)
3.0
>>> from math import pi
>>> pi
3.141592653589793
>>> math.pi
3.141592653589793
>>> math.cos
<built-in function cos>
>>> from math import cos
>>> cos
<built-in function cos>
>>> cos(10)
-0.8390715290764524
>>> math.cos
<built-in function cos>

>>> 
>>> 
>>> 
>>> 
>>> from math import cos
>>> cos(90)
-0.4480736161291701
>>> from math import e, pow, log, tan
>>> e
2.718281828459045
>>> pow
<built-in function pow>
>>> log
<built-in function log>
>>> tan
<built-in function tan>
>>> pi=9
>>> from math import pi
>>> pi
3.141592653589793
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> pi=0
>>> pi=9
>>> pi
9
>>> from math import pi
>>> dir(builtins)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dir(builtins)
NameError: name 'builtins' is not defined
>>> 
