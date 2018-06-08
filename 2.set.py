Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
#Q.1- Create two set using user defined values.
>>> set1={1,2,3,4,5,6}
>>> set2={11,22,33,44,55,66}
>>> #1. Calculate difference between two sets.
>>> print(set1 - set2)
{1, 2, 3, 4, 5, 6}
>>> print(set2-set1)


>>> #3. Print the result of intersection of two sets.
{33, 66, 11, 44, 22, 55}
>>> print(set1 & set2)
set()
>>> det3={1,2,3,4,5,6}
>>> det4={2,3,4,5,6,7}
>>>
>>> print(det3 & det4)
{2, 3, 4, 5, 6}
>>>
>>>
>>>
>>> #2. Compare two sets.
>>> setA = 1,2,3,4,5
>>> setB = 1,2
>>> setC = setA >= setB
>>> print(setC)
True
>>> setD = setB >= setA
>>> print(setD)
False
