Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=92
>>> type(a)
<class 'int'>
>>> print(type(a))
<class 'int'>
>>> type(str(a))
<class 'str'>
>>> print(type(str(a)))
<class 'str'>
>>> str(42)
'42'
>>> int("42")
42
>>> float("2.3")
2.3
>>> str(2.3)
'2.3'
>>> a=92
>>> a
92
>>> float("1")
1.0
>>> float('1')
1.0
>>> #Lists....................................
>>> 
>>> easy_as = [1,2,3]
>>> easy_as
[1, 2, 3]
>>> [1, 2, 3]
[1, 2, 3]
>>> 
>>> empty = []
>>> empty
[]
>>> letters = ['a','b','c']
>>> letters
['a', 'b', 'c']
>>> numbers = [1,2,3,4,5]
>>> numbers
[1, 2, 3, 4, 5]
>>> mixed = [4,5, "seconds","third"]
>>> mixed
[4, 5, 'seconds', 'third']
>>> numbers.append(7)
>>> numbers
[1, 2, 3, 4, 5, 7]
>>> letters.append('k')
>>> letters
['a', 'b', 'c', 'k']
>>> numbers
[1, 2, 3, 4, 5, 7]
>>> numbers[0]
1
>>> numbers[1]
2
>>> numbers[-1]
7
>>> letters
['a', 'b', 'c', 'k']
>>> letters[:3]
['a', 'b', 'c']
>>> numbers
[1, 2, 3, 4, 5, 7]
>>> numbers[1:-1]
[2, 3, 4, 5]
>>> a=[1,2,3,4,5]
>>> b=['a','b','c','d','e']
>>> c=[a,b]
>>> print(c)
[[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
>>> c[0]
[1, 2, 3, 4, 5]
>>> c[1]
['a', 'b', 'c', 'd', 'e']
>>> c[0][4]
5
>>> 
