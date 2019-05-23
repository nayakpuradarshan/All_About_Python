Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> print("hello python")
hello python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print('hello python', end='$')
hello python$
>>> print('hello', 'python', end='$')
hello python$
>>> print('hello', 'python', sep='*', end='$')
hello*python$
>>> 
>>> 
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 
>>> for i in range(10):
	print(i, end=' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> 
