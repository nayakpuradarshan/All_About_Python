Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> value1 = input("enter a value: ")
enter a value: 10
>>> type(value)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(value)
NameError: name 'value' is not defined
>>> type(value1)
<class 'str'>
>>> value = int(value1)
>>> val;ue
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    val;ue
NameError: name 'val' is not defined
>>> vallue
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    vallue
NameError: name 'vallue' is not defined
>>> value
10
>>> type(value)
<class 'int'>
>>> value = int(input("enter a value: "))
enter a value: 20
>>> value
20
>>> type(value)
<class 'int'>
>>> 
